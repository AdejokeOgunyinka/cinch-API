from unittest import TestCase


class TestSample(TestCase):
    def test_sample(self):
        self.assertIsInstance('Payment', str)
