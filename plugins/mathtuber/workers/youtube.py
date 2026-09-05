"""Credential-bearing publisher. Never imported by renderer or portable engine."""
import json
import os
from pathlib import Path
import sys
import time
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

req=json.loads(Path(sys.argv[1]).read_text())
config=json.loads(Path(req["credentials_config"]).read_text())
receipt=Path(req["receipt"])
def save(data):
    tmp=receipt.with_suffix(".tmp")
    tmp.write_text(json.dumps(data,indent=2))
    os.chmod(tmp,0o600)
    os.replace(tmp,receipt)
state=json.loads(receipt.read_text()) if receipt.exists() else {}
creds=Credentials.from_authorized_user_file(config["token_path"])
if creds.expired and creds.refresh_token:
    creds.refresh(Request())
    token=Path(config["token_path"])
    tmp=token.with_suffix(".refresh.tmp")
    tmp.write_text(creds.to_json())
    os.chmod(tmp,0o600)
    os.replace(tmp,token)
if not creds.valid:
    raise RuntimeError("NEEDS_AUTH: refresh or reconnect your existing YouTube account")
youtube=build("youtube","v3",credentials=creds,cache_discovery=False)
channels=youtube.channels().list(part="id",mine=True).execute().get("items",[])
intent=req["intent"]
if intent["channel_id"] not in [x["id"] for x in channels]:
    raise RuntimeError("CHANNEL_MISMATCH: credentials do not own the requested channel")
video_id=state.get("video_id")
if not video_id:
    if state.get("state") == "starting" and not state.get("session_uri"):
        raise RuntimeError("UPLOAD_UNCERTAIN: prior upload initiation was interrupted; reconcile before retry")
    upload=youtube.videos().insert(part="snippet,status",body={
        "snippet":{"title":intent["title"],"description":intent.get("description",""),"categoryId":"27","tags":intent.get("tags",[])},
        "status":{"privacyStatus":"private","selfDeclaredMadeForKids":intent.get("made_for_kids",False)}},
        media_body=MediaFileUpload(req["video"],mimetype="video/mp4",chunksize=8*1024*1024,resumable=True))
    if state.get("session_uri"):
        upload.resumable_uri=state["session_uri"]
        # Force the client to ask the server for acknowledged bytes before resuming.
        upload._in_error_state=True
    else:
        save({"state":"starting","intent_id":req["intent_id"]})
    response=None
    while response is None:
        _,response=upload.next_chunk(num_retries=3)
        state={"state":"uploading","session_uri":upload.resumable_uri,"intent_id":req["intent_id"]}
        if response:
            video_id=response["id"]
            state.update(state="uploaded_private",video_id=video_id)
        save(state)
for _ in range(60):
    items=youtube.videos().list(part="status,processingDetails",id=video_id).execute().get("items",[])
    if not items: raise RuntimeError("UPLOADED_VIDEO_NOT_FOUND")
    processing=items[0].get("processingDetails",{}).get("processingStatus")
    if processing == "succeeded": break
    if processing in ("failed","terminated"): raise RuntimeError(f"PROCESSING_FAILED: {processing}")
    time.sleep(5)
else:
    state.update(state="processing",video_id=video_id)
    save(state)
    print(json.dumps(state))
    sys.exit(0)
youtube.videos().update(part="snippet,status",body={"id":video_id,
    "snippet":{"title":intent["title"],"description":intent.get("description",""),"categoryId":"27","tags":intent.get("tags",[])},
    "status":{"privacyStatus":intent["privacy"],"selfDeclaredMadeForKids":intent.get("made_for_kids",False)}}).execute()
actual=youtube.videos().list(part="status",id=video_id).execute()["items"][0]["status"]["privacyStatus"]
state={"state":"published" if actual==intent["privacy"] else "visibility_restricted",
       "video_id":video_id,"url":f"https://www.youtube.com/watch?v={video_id}","privacy":actual,"intent_id":req["intent_id"]}
save(state)
print(json.dumps(state))
