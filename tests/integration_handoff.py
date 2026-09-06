"""Check the committed repository through an isolated generic skill install and media fixture.

Requires the existing media runtime and system dependencies. No model/account calls.
The archive intentionally excludes uncommitted files.
"""
import argparse
import io,json,os,subprocess,sys,tarfile,tempfile
from pathlib import Path
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output',type=Path)
args=parser.parse_args()
repo=Path(__file__).resolve().parents[1]
temporary=tempfile.TemporaryDirectory(prefix='MathTuber handoff ')
root=Path(temporary.name);checkout=root/'clean checkout';checkout.mkdir()
archive=subprocess.check_output(['git','-C',str(repo),'archive','HEAD'])
with tarfile.open(fileobj=io.BytesIO(archive)) as tar:tar.extractall(checkout,filter='data')
head=subprocess.check_output(['git','-C',str(repo),'rev-parse','HEAD'],text=True).strip()
env={k:v for k,v in os.environ.items() if not k.startswith('MATHTUBER_')}
python=sys.executable
engine=checkout/'plugins/mathtuber/scripts/engine.py';installer=checkout/'scripts/install.py'
def run(args):
 r=subprocess.run([str(x) for x in args],cwd=root,env=env,text=True,capture_output=True)
 if r.returncode:raise RuntimeError(r.stderr[-2000:]+r.stdout[-2000:])
 return r.stdout
skills=root/'host skills'
run([python,installer,'skills','--skills-dir',skills]);run([python,installer,'skills','--skills-dir',skills])
skill=(skills/'mathtuber').resolve();plugin=skill.parents[1]
assert plugin==(checkout/'plugins/mathtuber').resolve()
doctor=json.loads(run([python,plugin/'scripts/engine.py','doctor']))['result'];assert doctor['ready']
for name in ('audio_review.py','visual_review.py','publication_status.py','publish_batch.py'):
 run([python,plugin/'scripts'/name,'--help'])
fixture=root/'film project'
integration=json.loads(run([python,checkout/'tests/integration_media.py','--project',fixture]))
assert integration['passed']
state=json.loads(run([python,engine,'status','--project',fixture]))['result'];assert not state['accepted']
audio=json.loads(run([python,plugin/'scripts/audio_review.py','--project',fixture,'--no-asr','--final']))
report=json.loads(Path(audio['path']).read_text());assert not report['automatic_acceptance'];assert report['scenes'][0]['transcription_status']=='unavailable'
summary={'commit':head,'scope':'Clean tracked-file archive, generic skill install and cross-directory native media smoke on existing macOS shared runtime; not clean OS/bootstrap or real host-model test.',
'checks':{'tracked_archive_only':True,'paths_with_spaces':True,'generic_install_idempotent':True,'skill_resolves_full_plugin':True,'doctor_ready':doctor['ready'],'portable_tool_help':True,**integration['checks'],'unreviewed_export_not_accepted':not state['accepted'],'audio_review_without_asr_honest':True},'limitations':['Existing media runtime and system dependencies reused.','No authentication, publication, or model call performed.','Installer tested through generic skill adapter, not native vendor plugin caches.','Imported sine-tone fixture is not speech or film-quality validation.']}
if args.output:
 args.output.parent.mkdir(parents=True,exist_ok=True)
 args.output.write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))

temporary.cleanup()
