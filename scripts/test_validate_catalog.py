import copy
import datetime as dt
import json
from pathlib import Path
import unittest
from validate_catalog import validate

POLICY = json.loads((Path(__file__).resolve().parents[1] / 'config/research.json').read_text())
TODAY = dt.date(2026, 10, 25)

def card():
    result = {k: 'Reviewed with evidence' for k in ('concrete_problem','application_example','first_pilot','success_metric','requirements_and_costs','limitations','license_review','comparison')}
    result.update(url='https://github.com/example/project',status='ready',direction='video',verification_level='documentation',verification_date=TODAY.isoformat(),readme_source='https://github.com/example/project#readme',license_source='https://github.com/example/project/blob/main/LICENSE',scores={k: 4 for k in POLICY['dimensions']})
    return result

class CatalogTests(unittest.TestCase):
    def test_complete_card(self):
        self.assertEqual(validate([card()],POLICY,TODAY),[])
    def test_case_and_git_suffix_duplicates(self):
        a,b=card(),card(); b['url']='https://github.com/EXAMPLE/PROJECT.git/'
        self.assertTrue(any('duplicate' in e for e in validate([a,b],POLICY,TODAY)))
    def test_stale_and_future_evidence(self):
        for date in ('2026-10-01','2026-10-26'):
            c=card(); c['verification_date']=date
            self.assertTrue(any('date' in e for e in validate([c],POLICY,TODAY)))
    def test_incomplete_ready(self):
        c=card(); del c['license_review']; c['scores']['feasibility']=True
        errors=validate([c],POLICY,TODAY)
        self.assertTrue(any('license_review' in e for e in errors))
        self.assertTrue(any('numeric' in e for e in errors))
    def test_adopted_requires_pilot(self):
        c=card(); c['status']='adopted'
        self.assertTrue(any('pilot_passed' in e for e in validate([c],POLICY,TODAY)))
    def test_partial_discovery_allowed(self):
        self.assertEqual(validate([{'url':'https://github.com/example/project','status':'discovered','direction':'video'}],POLICY,TODAY),[])

if __name__ == '__main__': unittest.main()
