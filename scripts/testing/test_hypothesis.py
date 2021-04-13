from hypothesis import given

import unittest
import hypothesis.strategies as st

class TestHypothesis(unittest.TestCase):

    def encode(input_string):
        count = 1
        prev = ""
        lst = []
        for character in input_string:
            if character != prev:
                if prev:
                    entry = (prev, count)
                    lst.append(entry)
                count = 1
                prev = character
            else:
                count += 1
        entry = (character, count)
        lst.append(entry)
        return lst

    def decode(lst):
        q = ""
        for character, count in lst:
            q += character * count
        return q

    @given(st.text())
    def test_decode_inverts_encode(self, s):
        self.assertEqual(self.decode(self.encode(s)), s)
