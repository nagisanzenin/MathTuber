import copy
from pathlib import Path
import sys
import tempfile
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'plugins/mathtuber'))
from mathtuber.state import Project,create,ProductionError,file_hash
from mathtuber.creative import validate_plan,validate_delivery,soundtrack
from mathtuber.cli import record_review
class CreativeTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name)
  self.data={'schema_version':1,'brief':{'topic':'test'},'scenes':[{'id':'s01','source':'scenes/a.py','class_name':'A','narration':'hello'}]}
  create(self.root,self.data);self.p=Project(self.root)
 def tearDown(self):self.tmp.cleanup()
 def test_explicit_shorts_limit(self):
  self.p.data['delivery']={'kind':'youtube_short'}
  validate_delivery(self.p,180)
  with self.assertRaises(ProductionError):validate_delivery(self.p,180.01)
  self.p.data['delivery']['kind']='youtube_video';validate_delivery(self.p,300)
 def test_landscape_not_short(self):
  self.p.data.update(delivery={'kind':'youtube_short'},format={'width':1920,'height':1080})
  with self.assertRaises(ProductionError):validate_delivery(self.p,60)
 def test_legacy_and_incomplete_contract(self):
  self.assertFalse(validate_plan(self.p)['present']);self.p.data['creative']={}
  with self.assertRaises(ProductionError):validate_plan(self.p)
 def test_sound_asset_hash_tracks_change(self):
  f=self.root/'assets/score.wav';f.write_bytes(b'one')
  self.p.data['soundtrack']={'path':'assets/score.wav','license':'original CC0'}
  old=soundtrack(self.p)['sha256'];f.write_bytes(b'two');self.assertNotEqual(old,soundtrack(self.p)['sha256'])
 def test_sound_escape_and_nan_rejected(self):
  self.p.data['soundtrack']={'path':'../score.wav','license':'original'}
  with self.assertRaises(ProductionError):soundtrack(self.p)
  self.p.data['soundtrack']['gain_db']=float('nan')
  with self.assertRaises(ProductionError):soundtrack(self.p)
 def test_contract_order_and_completeness(self):
  plan=dict.fromkeys(['audience','learning_goal','question','payoff','transfer_prompt','duration_rationale','novelty_audit'],'explicit')
  beat=dict.fromkeys(['viewer_question','visual_action','new_understanding','sound_intent'],'explicit');beat['scene']='s01';plan['beats']=[beat]
  self.p.data['creative']=plan;self.assertTrue(validate_plan(self.p)['passed'])
  beat['scene']='wrong'
  with self.assertRaises(ProductionError):validate_plan(self.p)
 def test_creative_review_requires_provenance(self):
  self.p.data['creative']={'audience':'curious viewers'}
  f=self.root/'reviews/evidence.json';f.write_text('{}')
  review={'snapshot':self.p.snapshot(),'scope':'s01','reviewer':'fixture','verdict':'accept','evidence':[{'path':str(f),'sha256':file_hash(f)}],'checks':dict.fromkeys(['math','visual','timing','audio'],'pass'),'findings':[]}
  with self.assertRaises(ProductionError):record_review(self.p,review)
  review['methods']={domain:{'method':'fixture measurement','coverage':'fixture','limitations':['No human audience']} for domain in review['checks']}
  review['audience_validation']='Not measured'
  self.assertTrue(record_review(self.p,review)['recorded'])
if __name__=='__main__':unittest.main()
