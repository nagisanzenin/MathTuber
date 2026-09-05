import copy
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'plugins/mathtuber'))
from mathtuber.state import Project, ProductionError, create, digest, file_hash, validate_manifest, within, atomic_json
from mathtuber.cli import record_review, publish
from mathtuber import media

class EngineTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name)
        self.manifest={'schema_version':1,'brief':{'topic':'Odd squares'},'scenes':[{'id':'s01','source':'scenes/main.py','class_name':'Main','narration':'One plus three is four.'}]}
        create(self.root,self.manifest)
        (self.root/'scenes/main.py').write_text('class Main: pass\n')
        self.project=Project(self.root)
    def tearDown(self): self.temp.cleanup()
    def test_duplicate_scene_rejected(self):
        m=copy.deepcopy(self.manifest);m['scenes'].append(m['scenes'][0])
        with self.assertRaises(ProductionError): validate_manifest(m)
    def test_path_escape_rejected(self):
        with self.assertRaises(ProductionError): within(self.root,'../outside')
    def test_absolute_source_rejected(self):
        m=copy.deepcopy(self.manifest);m['scenes'][0]['source']='/tmp/evil.py'
        with self.assertRaises(ProductionError): validate_manifest(m)
    def test_invalid_format_rejected(self):
        m=copy.deepcopy(self.manifest);m['format']={'width':0}
        with self.assertRaises(ProductionError): validate_manifest(m)
    def test_existing_project_preserved(self):
        with self.assertRaises(ProductionError): create(self.root,self.manifest)
    def test_artifact_tampering_invalidates(self):
        path=self.root/'audio/test.wav';path.write_bytes(b'original')
        self.project.record('audio:s01','fingerprint',path,{})
        self.assertIsNotNone(self.project.artifact('audio:s01','fingerprint'))
        path.write_bytes(b'changed')
        self.assertIsNone(self.project.artifact('audio:s01','fingerprint'))
    def test_wrong_fingerprint_invalidates(self):
        path=self.root/'audio/test.wav';path.write_bytes(b'data')
        self.project.record('audio:s01','one',path,{})
        self.assertIsNone(self.project.artifact('audio:s01','two'))
    def test_changed_narration_invalidates_audio(self):
        before=media.audio_fingerprint(self.project,self.project.scene('s01'))
        self.project.data['scenes'][0]['narration']='Different narration'
        self.assertNotEqual(before,media.audio_fingerprint(self.project,self.project.scene('s01')))
    def test_source_change_does_not_invalidate_audio(self):
        before=media.audio_fingerprint(self.project,self.project.scene('s01'))
        (self.root/'scenes/main.py').write_text('new source')
        self.assertEqual(before,media.audio_fingerprint(self.project,self.project.scene('s01')))
    def test_unrelated_scene_keeps_render_fingerprint(self):
        scene=self.project.scene('s01')
        with patch.object(media,'audio_for',return_value={'sha256':'audio'}), patch.object(media,'runtime_versions',return_value={}):
            before=media.render_fingerprint(self.project,scene,'final','native')
            (self.root/'scenes/other.py').write_text('changed unrelated scene')
            self.assertEqual(before,media.render_fingerprint(self.project,scene,'final','native'))
            scene['dependencies']=['scenes/other.py']
            before=media.render_fingerprint(self.project,scene,'final','native')
            (self.root/'scenes/other.py').write_text('changed shared dependency')
            self.assertNotEqual(before,media.render_fingerprint(self.project,scene,'final','native'))
    def test_dependency_escape_rejected(self):
        scene=self.project.scene('s01');scene['dependencies']=['../outside.py']
        with self.assertRaises(ProductionError):media.render_fingerprint(self.project,scene,'final','native')
    def test_source_change_invalidates_snapshot(self):
        before=self.project.snapshot();(self.root/'scenes/main.py').write_text('new source')
        self.assertNotEqual(before,self.project.snapshot())
    def test_asset_change_invalidates_snapshot(self):
        before=self.project.snapshot();(self.root/'assets/config.json').write_text('{}')
        self.assertNotEqual(before,self.project.snapshot())
    def test_project_lock_blocks_other_writer(self):
        with self.project.lock():
            with self.assertRaises(ProductionError):
                with self.project.lock(): pass
        with self.project.lock(): pass
    def test_lock_released_on_failure(self):
        with self.assertRaises(RuntimeError):
            with self.project.lock(): raise RuntimeError('test')
        with self.project.lock(): pass
    def test_missing_scene_cannot_assemble(self):
        with self.assertRaises(ProductionError): media.assemble(self.project)
    def test_missing_audio_cannot_render(self):
        with self.assertRaises(ProductionError): media.render(self.project,'s01','preview','native')
    def review(self):
        path=self.root/'reviews/frame.png';path.write_bytes(b'fixture')
        return {'snapshot':self.project.snapshot(),'scope':'s01','reviewer':'test','verdict':'accept',
                'evidence':[{'path':str(path),'sha256':file_hash(path)}],
                'checks':dict.fromkeys(['math','visual','timing','audio'],'pass'),'findings':[]}
    def test_stale_review_rejected(self):
        review=self.review();(self.root/'scenes/main.py').write_text('changed')
        with self.assertRaises(ProductionError): record_review(self.project,review)
    def test_missing_modality_not_pass(self):
        review=self.review();review['checks']['audio']='unavailable'
        with self.assertRaises(ProductionError): record_review(self.project,review)
    def test_findings_prevent_acceptance(self):
        review=self.review();review['findings']=['Wrong equation']
        with self.assertRaises(ProductionError): record_review(self.project,review)
    def test_tampered_evidence_rejected(self):
        review=self.review();review['evidence'][0]['sha256']='wrong'
        with self.assertRaises(ProductionError): record_review(self.project,review)
    def test_publish_requires_final_review(self):
        with self.assertRaises(ProductionError): publish(self.project,{},'',True)
    def test_final_acceptance_requires_actual_export(self):
        review=self.review();review['scope']='final'
        with self.assertRaises(ProductionError): record_review(self.project,review)
    def test_atomic_json_replaces(self):
        path=self.root/'test.json';atomic_json(path,{'a':1});atomic_json(path,{'b':2})
        self.assertEqual(json.loads(path.read_text()),{'b':2})
    def test_srt_rounding(self):
        self.assertEqual(media.srt_time(59.9996),'00:01:00,000')

if __name__=='__main__':unittest.main()
