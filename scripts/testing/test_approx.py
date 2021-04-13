import unittest
import numpy as np

class TestAproxs(unittest.TestCase):

    def test_approx(self):
        a = 0.1 + 0.2
        # comparar a con b, cuántos decimales
        self.assertAlmostEqual(a, 0.3, 5, msg="un mensaje para el failure")

    def test_np_approx(self):
        a = np.array([0.54, 0.33])
        b = np.array([0.13, 0.22])

        np.testing.assert_almost_equal(a + b, np.array([0.678, 0.557]), 3, err_msg="A message in here")
