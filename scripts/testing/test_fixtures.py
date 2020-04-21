import unittest
import pandas as pd

class TestFixtures(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._df = pd.DataFrame({'a': [1,2,3,4],
                           'b': [5,6,7,8],
                           'c': [0,1,2,3]})

    @classmethod
    def TearDownClass(cls):
        cls._df.destroy()


    def test_fixtures(self):
        print(self._df.a.mean())
        self.assertEqual((4,3), self._df.shape)