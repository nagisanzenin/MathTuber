from pathlib import Path
import json
import sys
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'plugins/mathtuber'))
from scripts.knowledge import retrieve,ROOT

class KnowledgeTests(unittest.TestCase):
    def setUp(self):self.entries=json.loads((ROOT/'knowledge/repairs.json').read_text())['entries']
    def test_specific_failure_ranks_before_generic_mentions(self):
        self.assertEqual(retrieve(self.entries,'Manim opacity fill')[0]['id'],'shape-fill')
        self.assertEqual(retrieve(self.entries,'PROJECT_BUSY lock')[0]['id'],'project-busy')
    def test_stage_and_no_match_do_not_invent_advice(self):
        self.assertEqual(retrieve(self.entries,'opacity',stage='publishing'),[])
        self.assertEqual(retrieve(self.entries,'unmatchedword'),[])
        self.assertLessEqual(len(retrieve(self.entries,'',limit=2)),2)
    def test_each_case_has_a_check_and_bundled_reference(self):
        self.assertEqual(len({e['id'] for e in self.entries}),len(self.entries))
        for e in self.entries:
            for k in ['symptom','cause','repair','verify','avoid']:self.assertTrue(e[k])
            path=(ROOT/e['reference']).resolve();self.assertTrue(path.is_relative_to(ROOT));self.assertTrue(path.is_file())

if __name__=='__main__':unittest.main()
