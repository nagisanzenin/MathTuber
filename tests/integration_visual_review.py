"""Real FFmpeg frame extraction with landscape aspect ratio and final-frame coverage."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from PIL import Image

WORKER=Path(__file__).resolve().parents[1]/'plugins/mathtuber/workers/visual_review.py'


class VisualEvidenceTests(unittest.TestCase):
    def test_extraction_preserves_shape_and_does_not_accept(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);video=root/'fixture.mp4';out=root/'evidence';request=root/'request.json'
            subprocess.run(['ffmpeg','-v','error','-y','-f','lavfi','-i','color=white:s=320x180:r=30:d=1',
                            '-c:v','libx264','-pix_fmt','yuv420p',str(video)],check=True)
            data={'export':str(video),'export_sha256':hashlib.sha256(video.read_bytes()).hexdigest(),
                  'fingerprint':'fixture','output':str(out),
                  'groups':[{'id':'ending','purpose':'Check final frame','times':[i/30 for i in range(0,30,3)]+[29/30]}]}
            request.write_text(json.dumps(data))
            subprocess.run([sys.executable,str(WORKER),str(request)],check=True,capture_output=True)
            report=json.loads((out/'evidence.json').read_text());group=report['groups'][0]
            self.assertFalse(report['automatic_acceptance'])
            self.assertEqual(len(group['frames']),11)
            self.assertEqual(len(group['sheets']),2)
            self.assertAlmostEqual(group['frames'][-1]['time'],29/30)
            for record in group['frames']+group['sheets']:
                self.assertEqual(hashlib.sha256(Path(record['path']).read_bytes()).hexdigest(),record['sha256'])
            with Image.open(group['frames'][0]['path']) as frame:
                self.assertEqual(frame.size,(360,640))
                self.assertLess(max(frame.getpixel((180,100))),10)
                self.assertGreater(min(frame.getpixel((180,320))),240)
                # 16:9 image spans about 202 pixels high inside a portrait tile.
                bright=sum(min(frame.getpixel((180,y)))>240 for y in range(640))
                self.assertTrue(200<=bright<=204)


if __name__=='__main__':unittest.main()
