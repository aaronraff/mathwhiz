import unittest
from backend.questions import generate
from ddt import ddt, data


@ddt
class TestGenerate(unittest.TestCase):
    @data(0, 1, 4, 100)
    def test_generate_returns_correct_count(self, count):
        res = generate.Generator().generate(count)
        self.assertEqual(len(res), count)
