from contextlib import nullcontext
import importlib.util
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

SCRIPT=Path(__file__).resolve().parents[1]/'plugins/mathtuber/scripts/publication_status.py'
spec=importlib.util.spec_from_file_location('publication_status',SCRIPT)
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)


class PublicationStatusTests(unittest.TestCase):
    def test_readback_requires_both_actual_visibility_and_processing(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);entries=[]
            for name in ('a','b','c'):
                p=root/name;(p/'.mathtuber').mkdir(parents=True)
                identity=module.digest({'sha256':name,'channel_id':'fixture'})
                (p/'.mathtuber'/f'upload-{identity}.json').write_text('{}')
                (root/f'{name}.json').write_text(json.dumps({'channel_id':'fixture','privacy':'public'}))
                entries.append({'project':name,'intent':f'{name}.json'})
            batch=root/'batch.json';batch.write_text(json.dumps({'projects':entries}))
            def project(path):
                return SimpleNamespace(root=path,lock=nullcontext,artifact=lambda *args:{'sha256':path.name})
            results=iter([{'state':'observed','privacy':'public','processing':'succeeded'},
                          {'state':'observed','privacy':'private','processing':'succeeded'},
                          {'state':'observed','privacy':'public','processing':'processing'}])
            def run(command,**kw):
                request=json.loads(Path(command[-1]).read_text())
                self.assertIs(request['status_only'],True)
                return json.dumps(next(results)),0
            with patch.object(module,'Project',side_effect=project),patch.object(module.media,'assembly_fingerprint',return_value='fp'),patch.object(module.media,'run',side_effect=run):
                result=module.inspect(batch,root/'unused-config')
            self.assertFalse(result['complete']);self.assertEqual(result['completed'],1)
            self.assertEqual(result['total'],3)

    def test_no_receipt_does_not_contact_youtube(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);(root/'intent.json').write_text(json.dumps({'channel_id':'fixture','privacy':'public'}))
            batch=root/'batch.json';batch.write_text(json.dumps({'projects':[{'project':'a','intent':'intent.json'}]}))
            project=SimpleNamespace(root=root/'a',lock=nullcontext,artifact=lambda *args:{'sha256':'fixture'})
            with patch.object(module,'Project',return_value=project),patch.object(module.media,'assembly_fingerprint',return_value='fp'),patch.object(module.media,'run') as run:
                result=module.inspect(batch,'unused-config');run.assert_not_called()
            self.assertEqual(result['videos'][0]['state'],'not_uploaded')


if __name__=='__main__':unittest.main()
