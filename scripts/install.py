#!/usr/bin/env python3
"""Install the same full plugin on a supported host without copying skills alone."""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import time
repo=Path(__file__).resolve().parents[1]
plugin=repo/'plugins/mathtuber'
p=argparse.ArgumentParser()
p.add_argument('platform',choices=['codex','claude','pi','zcode','opencode','gemini','skills'])
p.add_argument('--skills-dir',help='Explicit directory for the generic skills route')
a=p.parse_args()
def run(*args): subprocess.run([str(x) for x in args],check=True)
if a.platform=='codex':
    run('codex','plugin','marketplace','add',repo)
    run('codex','plugin','add','mathtuber@mathtuber')
elif a.platform=='claude':
    run('claude','plugin','marketplace','add',repo)
    run('claude','plugin','install','mathtuber@mathtuber')
elif a.platform=='pi': run('pi','install',repo)
elif a.platform=='gemini': run('gemini','extensions','link',plugin)
elif a.platform=='zcode':
    # ZCode's documented inline directories avoid guessing undocumented installer flags.
    path=Path.home()/'.zcode/cli/config.json'
    data=json.loads(path.read_text()) if path.exists() else {}
    dirs=data.setdefault('plugins',{}).setdefault('dirs',[])
    if str(plugin) not in dirs:
        if path.exists(): shutil.copy2(path,path.with_name('config.mathtuber-backup-'+str(int(time.time()))+'.json'))
        dirs.append(str(plugin))
        path.parent.mkdir(parents=True,exist_ok=True)
        tmp=path.with_suffix('.mathtuber.tmp')
        tmp.write_text(json.dumps(data,indent=2)+'\n');os.chmod(tmp,0o600);os.replace(tmp,path)
    print('Registered ZCode inline plugin directory:',plugin)
else:
    if a.platform == 'opencode': a.skills_dir = str(Path.home()/'.config/opencode/skills')
    if not a.skills_dir: raise SystemExit('--skills-dir is required for a generic host')
    dest=Path(a.skills_dir).expanduser()/'mathtuber'
    target=plugin/'skills/mathtuber'
    dest.parent.mkdir(parents=True,exist_ok=True)
    if dest.is_symlink() and dest.resolve()==target.resolve(): pass
    elif dest.exists() or dest.is_symlink(): raise SystemExit('Existing skill differs; refusing to overwrite '+str(dest))
    else: dest.symlink_to(target,target_is_directory=True)
    print('Linked full-repo skill:',dest)
