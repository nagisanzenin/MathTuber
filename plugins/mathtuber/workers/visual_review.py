"""Render paginated evidence sheets, preserving aspect ratio; never accept a film."""
import argparse
import json
from pathlib import Path
import subprocess
import sys
from PIL import Image, ImageDraw
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from mathtuber.state import atomic_json, file_hash


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('request')
    request=json.loads(Path(parser.parse_args().request).read_text())
    if file_hash(Path(request['export']))!=request['export_sha256']:
        raise SystemExit('STALE_EXPORT: final changed after evidence request')
    out=Path(request['output']);out.mkdir(parents=True,exist_ok=True)
    groups=[]
    for index,group in enumerate(request['groups']):
        records=[];sheets=[];tiles=[]
        for i,timestamp in enumerate(group['times']):
            frame=out/f'group-{index:03}-frame-{i:03}.jpg'
            subprocess.run(['ffmpeg','-v','error','-y','-ss',str(timestamp),'-i',request['export'],
                '-frames:v','1','-vf','scale=360:640:force_original_aspect_ratio=decrease,pad=360:640:(ow-iw)/2:(oh-ih)/2,format=yuvj420p',str(frame)],check=True)
            tile=Image.new('RGB',(360,667),'white')
            with Image.open(frame) as picture:tile.paste(picture,(0,27))
            ImageDraw.Draw(tile).text((8,7),f'{timestamp:.3f}s',fill='black');tiles.append(tile)
            records.append({'path':str(frame),'sha256':file_hash(frame),'time':timestamp})
        for page,start in enumerate(range(0,len(tiles),8)):
            subset=tiles[start:start+8]
            sheet=Image.new('RGB',(360*min(4,len(subset)),667*((len(subset)+3)//4)),'white')
            for i,tile in enumerate(subset):sheet.paste(tile,((i%4)*360,(i//4)*667))
            path=out/f'group-{index:03}-page-{page+1}.jpg';sheet.save(path,quality=92)
            sheets.append({'path':str(path),'sha256':file_hash(path),'frames':len(subset)})
        groups.append({k:v for k,v in group.items() if k!='times'}|{'frames':records,'sheets':sheets})
    report=out/'evidence.json'
    atomic_json(report,{'schema_version':1,'fingerprint':request['fingerprint'],
        'export_sha256':request['export_sha256'],'automatic_acceptance':False,'groups':groups,
        'coverage':'Distributed frames, opening, every authored cue, each declared critical interval through completion, and final decodable frame. Sampled evidence only; not continuous audiovisual inspection or a verdict.'})
    print(json.dumps({'cached':False,'path':str(report),'automatic_acceptance':False}))


if __name__=='__main__':main()
