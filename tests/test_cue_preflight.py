from contextlib import nullcontext
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import tempfile
import sys
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'plugins/mathtuber'))
from scripts import compile_cues
from mathtuber.state import ProductionError

class CuePreflightTests(unittest.TestCase):
    def test_reports_all_missing_and_repeated_cues_together(self):
        with self.assertRaises(ProductionError) as raised:
            compile_cues.resolve_cues("self.at('repeat'); self.at('absent')",[{'text':'repeat then repeat','start':1}])
        self.assertIn("'repeat': 2 matches",str(raised.exception))
        self.assertIn("'absent': 0 matches",str(raised.exception))

    def test_preflight_never_reads_audio_or_replaces_real_timing(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);(root/'scene.py').write_text("self.at('Start here')")
            (root/'assets').mkdir();timing=root/'assets/timing.json';timing.write_text('{"real": 12.5}')
            project=SimpleNamespace(root=root,data={'scenes':[{'id':'s01','source':'scene.py','narration':'Start here. Then finish.'}]},lock=lambda:nullcontext())
            with patch.object(compile_cues,'Project',return_value=project),patch.object(compile_cues,'audio_for') as audio,patch.object(compile_cues,'atomic_json') as write,patch.object(sys,'argv',['compile_cues','--project',tmp,'--check-only']):
                compile_cues.main()
            audio.assert_not_called();write.assert_not_called()
            self.assertEqual(timing.read_text(),'{"real": 12.5}')

if __name__=='__main__':unittest.main()
