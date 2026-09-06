from pathlib import Path
import sys
import unittest
from unittest.mock import patch
import json
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'plugins/mathtuber'))
from mathtuber.environment import capabilities, PACKAGES
from mathtuber.cli import doctor


class CapabilityTests(unittest.TestCase):
    def test_render_packages_do_not_imply_speech_or_upload(self):
        commands={x:'/fixture/'+x for x in ('ffmpeg','ffprobe','latex','dvisvgm','espeak-ng')}
        result=capabilities(commands,{'manim':'fixture','numpy':'fixture'},True)
        self.assertTrue(result['render']['dependencies_ready'])
        self.assertFalse(result['narration']['dependencies_ready'])
        self.assertFalse(result['youtube']['dependencies_ready'])

    def test_optional_asr_is_separate_and_timezone_is_checked(self):
        packages={x:'fixture' for x in PACKAGES};packages['faster-whisper']=None
        result=capabilities({},packages,False)
        self.assertFalse(result['independent_asr']['dependencies_ready'])
        self.assertTrue(result['imported_audio']['dependencies_ready'])
        self.assertFalse(result['youtube']['dependencies_ready'])
        self.assertTrue(any('timezone:' in x for x in result['youtube']['missing']))

    def test_doctor_does_not_report_render_only_runtime_ready(self):
        report={'packages':{'manim':'fixture','numpy':'fixture'},'pacific_timezone':True}
        with patch('mathtuber.cli.shutil.which',return_value='/fixture'),patch('mathtuber.cli.media.run',return_value=(json.dumps(report),0)):
            result=doctor()
        self.assertFalse(result['ready'])
        self.assertTrue(result['capabilities']['render']['dependencies_ready'])


if __name__=='__main__':unittest.main()
