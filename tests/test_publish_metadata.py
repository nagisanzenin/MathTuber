"""Reject YouTube-invalid metadata before credentials or upload are touched."""
import sys
from pathlib import Path
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'plugins/mathtuber'))
from mathtuber.cli import publish
from mathtuber.state import ProductionError


class MetadataTests(unittest.TestCase):
    def plan(self, **metadata):
        project = SimpleNamespace(artifact=Mock(return_value={'sha256': 'test-export'}))
        intent = dict(channel_id='test-channel', title='A gentle inequality', privacy='public', authorized=True)
        intent.update(metadata)
        with patch('mathtuber.cli.status', return_value={'accepted': True}), patch('mathtuber.cli.media.assembly_fingerprint', return_value='test'), patch('mathtuber.cli.media.run') as run:
            try:
                return publish(project, intent, None, True)
            finally:
                run.assert_not_called()

    def test_inequality_rejected_during_dry_run(self):
        for description in ['0<phi<pi', 'x > y', None]:
            with self.subTest(description=description), self.assertRaisesRegex(ProductionError, 'Description must'):
                self.plan(description=description)

    def test_description_limit_counts_utf8_bytes(self):
        self.assertTrue(self.plan(description='é'*2500)['dry_run'])
        with self.assertRaisesRegex(ProductionError, 'Description must'):
            self.plan(description='é'*2501)

    def test_plain_language_math_and_newlines_are_preserved(self):
        text = 'Angle φ lies between zero and π.\nArea = πr².'
        self.assertEqual(self.plan(description=text)['intent']['description'], text)

    def test_invalid_utf8_rejected(self):
        with self.assertRaisesRegex(ProductionError, 'valid UTF-8'):
            self.plan(description='\ud800')

    def test_title_validation_keeps_unicode_but_rejects_brackets(self):
        self.assertTrue(self.plan(title='A curve: φ and π')['dry_run'])
        for title in ['x < y', 'x > y', '', 'a'*101, None]:
            with self.subTest(title=title), self.assertRaisesRegex(ProductionError, 'Title must'):
                self.plan(title=title)


if __name__ == '__main__':
    unittest.main()
