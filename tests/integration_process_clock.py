"""Run with the media runtime; verifies phase across actual Manim play/wait."""
from pathlib import Path
import sys,tempfile,unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'plugins/mathtuber'))
from components import NarratedScene, Dot, RED, tempconfig
class ClockIntegration(unittest.TestCase):
 def test_real_render_continuity_pause_and_resume(self):
  rows=[]
  class Check(NarratedScene):
   def construct(self):
    c=self.process_clock(2)
    dot=Dot();dot.add_updater(lambda m:m.move_to([c.value/4,0,0]));self.add(dot)
    self.wait(1);rows.append(c.value)
    self.play(dot.animate.set_color(RED),run_time=1);rows.append(c.value)
    c.pause();self.wait(1);rows.append(c.value)
    c.resume();self.wait(1);rows.append(c.value)
  with tempfile.TemporaryDirectory() as directory:
   with tempconfig(dict(pixel_width=180,pixel_height=320,frame_rate=15,media_dir=directory,disable_caching=True,verbosity='ERROR')):Check().render()
  for actual,expected in zip(rows,[2,4,4,6]):self.assertAlmostEqual(actual,expected)
if __name__=='__main__':unittest.main()
