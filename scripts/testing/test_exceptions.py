import unittest

class TestExceptions(unittest.TestCase):

    def some_funtion(self):
        raise ValueError("some excpetion 404 raised")

    def test_raise_404_exception(self):
        with self.assertRaises(ValueError, match=r".* 404 .*"):
            self.some_fun()

