"""Real Pi loader/tool transport, simulated model endpoint; no account required."""
import argparse
import json
import os
from pathlib import Path
import shlex
import subprocess
import tempfile
import threading
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args()
repo=Path(__file__).resolve().parents[1];engine=repo/'plugins/mathtuber/scripts/engine.py'
payloads=[]
class Handler(BaseHTTPRequestHandler):
    def log_message(self,*args):pass
    def do_POST(self):
        body=json.loads(self.rfile.read(int(self.headers['Content-Length'])))
        payloads.append(body)
        has_tool=any(m.get('role')=='tool' for m in body['messages'])
        if not has_tool:
            delta={'role':'assistant','tool_calls':[{'index':0,'id':'call_doctor','type':'function','function':{'name':'bash','arguments':json.dumps({'command':f'python3 {shlex.quote(str(engine))} doctor'})}}]}
            reason='tool_calls'
        else: delta={'role':'assistant','content':'Transport check complete.'};reason='stop'
        self.send_response(200);self.send_header('Content-Type','text/event-stream');self.end_headers()
        for d,finish in [(delta,None),({},reason)]:
            packet={'id':'fixture','object':'chat.completion.chunk','created':int(time.time()),'model':'fixture','choices':[{'index':0,'delta':d,'finish_reason':finish}]}
            self.wfile.write(('data: '+json.dumps(packet)+'\n\n').encode())
        self.wfile.write(b'data: [DONE]\n\n');self.wfile.flush()
server=HTTPServer(('127.0.0.1',0),Handler)
thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
with tempfile.TemporaryDirectory() as folder:
    config=Path(folder)/'config';config.mkdir()
    (config/'settings.json').write_text(json.dumps({'packages':[str(repo)]}))
    (config/'models.json').write_text(json.dumps({'providers':{'fixture':{'baseUrl':f'http://127.0.0.1:{server.server_port}/v1','api':'openai-completions','apiKey':'local-test-only','models':[{'id':'fixture','input':['text','image'],'contextWindow':32768,'maxTokens':1024,'reasoning':False}]}}}))
    env=os.environ.copy();env['PI_CODING_AGENT_DIR']=str(config);env['PI_OFFLINE']='1'
    result=subprocess.run(['pi','--print','--no-session','--offline','--provider','fixture','--model','fixture','/skill:mathtuber Check local production readiness.'],cwd=folder,env=env,text=True,capture_output=True,timeout=45)
server.shutdown()
text=json.dumps(payloads)
checks={'process_success':result.returncode==0,'skill_discovered':'mathtuber/SKILL.md' in text,'skill_expanded':'You are the filmmaker' in text,'real_bash_result':any(m.get('role')=='tool' and 'reasoning_api_required' in str(m.get('content')) for b in payloads for m in b['messages']),'two_model_requests':len(payloads)>=2}
report={'platform':'pi','version':subprocess.check_output(['pi','--version'],text=True).strip(),'verification':'real loader and bash transport; simulated model','checks':checks,'passed':all(checks.values()),'stderr':result.stderr[-1200:]}
Path(a.output).parent.mkdir(parents=True,exist_ok=True);Path(a.output).write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
raise SystemExit(0 if report['passed'] else 1)
