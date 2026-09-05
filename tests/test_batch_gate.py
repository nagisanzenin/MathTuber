"""A bad later member must block the batch before any upload is attempted."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

SCRIPT=Path(__file__).resolve().parents[1]/'plugins/mathtuber/scripts/publish_batch.py'
spec=importlib.util.spec_from_file_location('publish_batch',SCRIPT)
batch=importlib.util.module_from_spec(spec);spec.loader.exec_module(batch)

class BatchGateTests(unittest.TestCase):
    def fixture(self,root):
        entries=[]
        for name in ('a','b'):
            (root/name).mkdir()
            record={k:'Observed; audience outcomes unmeasured' for k in ('opening','mechanism','readability','pacing','sound','remaining_weaknesses','audience_evidence')}
            record.update(snapshot=name,export_sha256=name,decision='release')
            (root/f'{name}-editorial.json').write_text(json.dumps(record))
            (root/f'{name}-intent.json').write_text('{}')
            entries.append(dict(project=name,intent=f'{name}-intent.json',editorial=f'{name}-editorial.json'))
        path=root/'batch.json';path.write_text(json.dumps(dict(projects=entries)));return path
    def test_later_unreviewed_member_blocks_without_upload(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);manifest=self.fixture(root)
            def state(project):return dict(accepted=project.root.name=='a',export=dict(sha256=project.root.name),snapshot=project.root.name)
            with patch.object(batch,'Project',side_effect=lambda path:type('P',(),{'root':path})()),patch.object(batch,'status',side_effect=state),patch.object(batch,'publish',return_value={}) as publish:
                with self.assertRaises(batch.ProductionError):batch.prepare(manifest)
                self.assertEqual(publish.call_count,1)
                self.assertTrue(publish.call_args.args[3])
    def test_stale_editorial_blocks_even_with_technical_acceptance(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);manifest=self.fixture(root)
            with patch.object(batch,'Project',side_effect=lambda path:type('P',(),{'root':path})()),patch.object(batch,'status',return_value=dict(accepted=True,export=dict(sha256='changed'),snapshot='changed')),patch.object(batch,'publish') as publish:
                with self.assertRaises(batch.ProductionError):batch.prepare(manifest)
                publish.assert_not_called()
    def test_empty_batch_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'batch.json';path.write_text('{"projects":[]}')
            with self.assertRaises(batch.ProductionError):batch.prepare(path)

if __name__=='__main__':unittest.main()
