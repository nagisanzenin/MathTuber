"""Run with the media Python to check real Manim profile behavior."""
import json
import sys
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1] / 'plugins/mathtuber'
sys.path.insert(0, str(ROOT))
try:
 import components
 from manim import tempconfig, Square, RIGHT, ManimColor
except ImportError:
 components = None

@unittest.skipIf(components is None, 'Requires the Manim media runtime')
class SceneIdentityTests(unittest.TestCase):
 def setUp(self):
  self.profile=json.loads((ROOT/'profiles/ivisualizethings-workshop.json').read_text())
  components.configure_profile(self.profile)
 def tearDown(self): components.configure_profile(None)
 def test_legacy_base_uses_bound_identity(self):
  scene=components.NarratedScene();scene.setup()
  self.assertEqual(ManimColor(scene.camera.background_color).to_hex().upper(), self.profile['identity']['colors']['background'])
  self.assertEqual(components.BLUE,self.profile['identity']['colors']['primary'])
  self.assertIn(scene.profile_font, [self.profile['identity']['type'][k] for k in ('font','fallback')])
 def test_safe_region_rejects_cropped_object(self):
  with tempconfig({'frame_width':8,'frame_height':128/9}):
   scene=components.WorkshopScene();scene.setup()
   scene.assert_safe(Square())
   with self.assertRaises(ValueError): scene.assert_safe(Square().shift(RIGHT*4))
 def test_legacy_reset_does_not_leak_previous_channel(self):
  components.configure_profile(None)
  self.assertEqual(components.BG,'#10121B')
