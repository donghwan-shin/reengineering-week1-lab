import unittest
import hello


class TestAutograder(unittest.TestCase):
    def test_result(self):
        # check if the file `causal_testing.png` exists
        self.assertEqual("Hello Reengineering", hello.say_hello())

