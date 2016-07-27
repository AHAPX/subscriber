import unittest

from src import add_params


class TestSubscriber(unittest.TestCase):

    def test_add_params(self):

        @add_params(a=2)
        def func(message, a=1):
            return a

        self.assertEqual(func('test'), 2)
