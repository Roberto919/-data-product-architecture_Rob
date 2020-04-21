import unittest
from featureforge.validate import BaseFeatureFixture, EQ, IN, APPROX, RAISES
from featureforge.feature import input_schema, output_schema

class TestBodyLength(unittest.TestCase, BaseFeatureFixture):

    @output_schema(int, lambda i: i >= 0)
    def body_length(message):
        return len(message["body"])

    feature = body_length
    fixtures = dict(
            test_eq=({"body": u"hello"}, EQ, 5),
            test_approx=({"body": "world!"}, APPROX, 6.00001),
            test_in=({"body": u"x"}, IN, [1,3,7]),
            test_raise=({}, RAISES, ValueError),
        )