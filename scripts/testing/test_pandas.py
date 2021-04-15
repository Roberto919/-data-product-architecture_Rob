import pandas as pd
import unittest

class TestPandas(unittest.TestCase):

    def test_pandas_dataframes_equals(self):
        df_1 = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
        df_2 = pd.DataFrame({'a': [1, 2], 'b': [3.0, 4.0]})

        pd.testing.assert_frame_equal(df_1, df_2)
