"""Exercise the actual publisher with fake Google transport; no network or account."""
import json
from pathlib import Path
import runpy
import sys
import tempfile
import types
import unittest
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch
WORKER=Path(__file__).resolve().parents[1]/'plugins/mathtuber/workers/youtube.py'
class FakeHttpError(Exception):
    def __init__(self, status=429, reason='rateLimitExceeded', message='Video Uploads per day exhausted'):
        self.resp=types.SimpleNamespace(status=status)
        self.content=json.dumps({'error':{'message':message,'errors':[{'reason':reason}]}})
class Response:
    def __init__(self,data):self.data=data
    def execute(self):return self.data
class Youtube:
    def __init__(self):self.inserts=0;self.updates=[];self.privacy='private'
    def channels(self):return self
    def videos(self):return self
    def list(self,**kw):
        if kw.get('mine'):return Response({'items':[{'id':'channel'}]})
        return Response({'items':[{'id':'video','status':{'privacyStatus':self.privacy},'processingDetails':{'processingStatus':'succeeded'}}]})
    def insert(self,**kw):
        self.inserts+=1
        return types.SimpleNamespace(resumable_uri='https://upload.example/session',next_chunk=lambda **kw:(None,{'id':'video'}))
    def update(self,**kw):
        self.updates.append(kw);self.privacy=kw['body']['status']['privacyStatus'];return Response({})
class PublisherTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name);self.api=Youtube()
        self.receipt=self.root/'receipt.json';config=self.root/'config.json';config.write_text(json.dumps({'token_path':'unused'}))
        self.request={'credentials_config':str(config),'receipt':str(self.receipt),'video':'fixture.mp4','intent_id':'id','intent':{'channel_id':'channel','title':'Proof','privacy':'public','authorized':True}}
    def tearDown(self):self.temp.cleanup()
    def invoke(self):
        request=self.root/'request.json';request.write_text(json.dumps(self.request))
        mods={name:types.ModuleType(name) for name in ['google','google.oauth2','google.oauth2.credentials','google.auth','google.auth.transport','google.auth.transport.requests','googleapiclient','googleapiclient.discovery','googleapiclient.http','googleapiclient.errors']}
        mods['googleapiclient.errors'].HttpError=FakeHttpError
        mods['google.oauth2.credentials'].Credentials=types.SimpleNamespace(from_authorized_user_file=lambda _:types.SimpleNamespace(expired=False,valid=True))
        mods['google.auth.transport.requests'].Request=lambda:None
        mods['googleapiclient.discovery'].build=lambda *a,**kw:self.api
        mods['googleapiclient.http'].MediaFileUpload=lambda *a,**kw:object()
        with patch.dict(sys.modules,mods),patch.object(sys,'argv',[str(WORKER),str(request)]),patch('time.sleep'):runpy.run_path(str(WORKER),run_name='__main__')
    def test_upload_then_repeat_reuses_video_and_updates_privacy(self):
        self.invoke();self.assertEqual(self.api.inserts,1)
        self.request['intent']['privacy']='private';self.request['intent']['title']='Revised title';self.invoke()
        self.assertEqual(self.api.inserts,1)
        self.assertEqual(self.api.updates[-1]['body']['snippet']['title'],'Revised title')
        self.assertEqual(json.loads(self.receipt.read_text())['privacy'],'private')
    def test_wrong_channel_cannot_upload(self):
        self.request['intent']['channel_id']='other'
        with self.assertRaisesRegex(RuntimeError,'CHANNEL_MISMATCH'):self.invoke()
        self.assertEqual(self.api.inserts,0)
    def test_uncertain_initialization_cannot_duplicate(self):
        self.receipt.write_text(json.dumps({'state':'starting'}))
        with self.assertRaisesRegex(RuntimeError,'UPLOAD_UNCERTAIN'):self.invoke()
        self.assertEqual(self.api.inserts,0)
    def test_lagging_visibility_readback_does_not_duplicate_upload(self):
        original=self.api.list;reads=[]
        def lagging(**kw):
            if kw.get('part')=='status':
                reads.append(1)
                if len(reads)<3:return Response({'items':[{'status':{'privacyStatus':'private'}}]})
            return original(**kw)
        self.api.list=lagging;self.invoke()
        self.assertEqual(len(reads),3)
        self.assertEqual(self.api.inserts,1)
        self.assertEqual(json.loads(self.receipt.read_text())['state'],'published')
    def test_unconfirmed_visibility_retains_video_for_reconciliation(self):
        original=self.api.list
        def pending(**kw):
            if kw.get('part')=='status':return Response({'items':[{'status':{'privacyStatus':'private'}}]})
            return original(**kw)
        self.api.list=pending;self.invoke();self.invoke()
        receipt=json.loads(self.receipt.read_text())
        self.assertEqual(receipt['state'],'visibility_pending')
        self.assertEqual(receipt['video_id'],'video')
        self.assertEqual(self.api.inserts,1)
    def reject_upload(self, session=None, error=None):
        original=self.api.insert
        def insert(**kw):
            upload=original(**kw);upload.resumable_uri=session
            def chunk(**kw):raise error or FakeHttpError()
            upload.next_chunk=chunk
            return upload
        self.api.insert=insert
        return original
    def test_daily_rejection_waits_without_restarting_or_leaking_session(self):
        self.reject_upload('https://upload.example/secret-session')
        output=StringIO()
        with redirect_stdout(output),self.assertRaises(SystemExit) as stopped:self.invoke()
        self.assertEqual(stopped.exception.code,0)
        state=json.loads(self.receipt.read_text())
        self.assertEqual(state['state'],'quota_wait')
        self.assertIn('session_uri',state)
        self.assertNotIn('secret-session',output.getvalue())
        with redirect_stdout(StringIO()),self.assertRaises(SystemExit):self.invoke()
        self.assertEqual(self.api.inserts,1)
    def test_definite_initial_rejection_can_retry_after_reset(self):
        original=self.reject_upload()
        with redirect_stdout(StringIO()),self.assertRaises(SystemExit):self.invoke()
        state=json.loads(self.receipt.read_text())
        self.assertNotIn('session_uri',state)
        state['retry_not_before']='2000-01-01T00:00:00+00:00'
        self.receipt.write_text(json.dumps(state));self.api.insert=original
        self.invoke()
        self.assertEqual(json.loads(self.receipt.read_text())['state'],'published')
        self.assertEqual(self.api.inserts,2)
    def test_generic_rate_limit_is_not_daily_quota_or_blindly_retryable(self):
        self.reject_upload(error=FakeHttpError(message='Temporary rate limit project-private-marker'))
        with self.assertRaisesRegex(RuntimeError,'YOUTUBE_HTTP_ERROR') as error:self.invoke()
        self.assertNotIn('project-private-marker',str(error.exception))
        self.assertEqual(json.loads(self.receipt.read_text())['state'],'starting')
        with self.assertRaisesRegex(RuntimeError,'UPLOAD_UNCERTAIN'):self.invoke()
    def test_quota_during_transfer_resumes_existing_session(self):
        original=self.reject_upload('https://upload.example/retained-session')
        with redirect_stdout(StringIO()),self.assertRaises(SystemExit):self.invoke()
        state=json.loads(self.receipt.read_text());state['retry_not_before']='2000-01-01T00:00:00+00:00'
        self.receipt.write_text(json.dumps(state))
        def resume(**kw):
            upload=original(**kw)
            def chunk(**kw):
                self.assertEqual(upload.resumable_uri,'https://upload.example/retained-session')
                self.assertTrue(upload._in_error_state)
                return None,{'id':'video'}
            upload.next_chunk=chunk
            return upload
        self.api.insert=resume;self.invoke()
        self.assertEqual(json.loads(self.receipt.read_text())['state'],'published')
if __name__=='__main__':unittest.main()
