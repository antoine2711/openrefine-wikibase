
import unittest
from suggest import SuggestEngine
from config import redis_client

class SuggestEngineTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = SuggestEngine(redis_client)

    # Helpers

    def query(self, typ, query_string, **kwargs):
        kwargs['prefix'] = query_string
        if typ == 'type':
            return self.r.suggest_type(kwargs)
        elif typ == 'property':
            return self.r.suggest_property(kwargs)
        elif typ == 'entity':
            return self.r.suggest_entity(kwargs)

    def results(self, *args, **kwargs):
        return self.query(*args, **kwargs)['result']

    def best_match_id(self, *args, **kwargs):
        return self.results(*args, **kwargs)[0]['id']

    # Tests start here

    def test_exact(self):
        self.assertEqual(
            self.best_match_id('entity', 'Recumbent bicycle'),
            'Q750483')
        self.assertEqual(
            self.best_match_id('property', 'Ringgold identifier'),
            'P3500')
