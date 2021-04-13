import marbles.core
import pandas as pd

from marbles.mixins import mixins


class MyTestCase(marbles.core.TestCase, mixins.CategoricalMixins):
    note = "Some note here to put as context for the failure assert."

    def test_that_all_weekdays_are_present(self):
        df = pd.DataFrame({'weekday': ['monday','tuesday','wednesday','thursday']})
        self.assertCategoricalLevelsEqual(df['weekday'], self.WEEKDAYS, note= self.note)