import copy,json,sys,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'plugins/mathtuber'))
from mathtuber import profiles
from mathtuber.state import Project,create,ProductionError,atomic_json
from mathtuber.media import render_fingerprint
from unittest.mock import patch

class ProfileTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name)
  create(self.root,{'schema_version':1,'brief':{'topic':'fixture'},'scenes':[{'id':'s1','source':'scenes/a.py','class_name':'A','narration':'hello'}]})
  (self.root/'scenes/a.py').write_text('class A: pass')
  self.p=Project(self.root);self.original=profiles.catalog()[0]
 def tearDown(self): self.tmp.cleanup()
 def test_binding_is_portable_idempotent_and_tracks_changes(self):
  profiles.bind(self.p,self.original['id']);first=self.p.snapshot()
  self.assertTrue(profiles.bind(self.p,self.original['id'])['cached'])
  self.assertEqual(profiles.load(Project(self.root)),self.original)
  changed=copy.deepcopy(self.original);changed['identity']['colors']['ink']='#112233'
  source=self.root/'custom.json';atomic_json(source,changed)
  with self.assertRaises(ProductionError):profiles.bind(self.p,str(source))
  profiles.bind(self.p,str(source),replace=True)
  self.assertNotEqual(first,self.p.snapshot());source.unlink()
  self.assertEqual(profiles.load(self.p),changed)
 def test_tampering_and_escape_rejected(self):
  profiles.bind(self.p,self.original['id'])
  path=self.root/self.p.data['channel_profile']['path'];path.write_text(path.read_text()+' ')
  with self.assertRaises(ProductionError):profiles.load(self.p)
  self.p.data['channel_profile']['path']='../outside.json'
  with self.assertRaises(ProductionError):profiles.load(self.p)
 def test_profile_change_invalidates_render_but_not_other_projects(self):
  fake_audio={'sha256':'audio'}
  with patch('mathtuber.media.audio_for',return_value=fake_audio),patch('mathtuber.media.runtime_versions',return_value={}):
   profiles.bind(self.p,self.original['id']);before=render_fingerprint(self.p,self.p.scene('s1'),'preview','native')
   changed=copy.deepcopy(self.original);changed['promise']='New promise';source=self.root/'custom.json';atomic_json(source,changed)
   profiles.bind(self.p,str(source),replace=True)
   self.assertNotEqual(before,render_fingerprint(self.p,self.p.scene('s1'),'preview','native'))
 def test_application_requires_episode_choices(self):
  self.assertFalse(profiles.check(self.p)['present']);profiles.bind(self.p,self.original['id'])
  with self.assertRaises(ProductionError):profiles.check(self.p)
  self.p.data['creative']={'profile_application':{'format':'investigation','signature':'Tactile objects','episode_variation':'An original mechanism','exceptions':[]}}
  self.assertTrue(profiles.check(self.p)['present'])
  self.p.data['creative']['profile_application']['format']='undefined'
  with self.assertRaises(ProductionError):profiles.check(self.p)
 def test_required_identity_cannot_be_missing_or_different(self):
  self.p.data['required_profile']=self.original['id']
  with self.assertRaises(ProductionError): profiles.check(self.p)
  profiles.bind(self.p,self.original['id'])
  self.p.data['required_profile']='another-channel'
  with self.assertRaises(ProductionError): profiles.check(self.p)
 def test_init_pins_required_profile(self):
  from mathtuber.cli import parser,perform
  dest=self.root/'new'
  result=perform(parser().parse_args(['init','--project',str(dest),'--manifest',str(self.root/'project.json'),'--profile',self.original['id']]))
  project=Project(dest)
  self.assertEqual(project.data['required_profile'],self.original['id'])
  self.assertEqual(profiles.load(project),self.original)
 def test_bad_shapes_and_sizes_rejected(self):
  for key,value in [('identity',[]),('examples',[{}]),('formats',{}),('status','proven-best')]:
   d=copy.deepcopy(self.original);d[key]=value
   with self.assertRaises(ProductionError):profiles.validate(d)
  for size in [True,float('nan'),0]:
   d=copy.deepcopy(self.original);d['identity']['type']['roles']['claim']=size
   with self.assertRaises(ProductionError):profiles.validate(d)
if __name__=='__main__':unittest.main()
