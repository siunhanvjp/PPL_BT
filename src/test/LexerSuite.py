import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("192.168.0.1", "Error Token 1", 101))
