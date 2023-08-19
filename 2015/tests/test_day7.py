import unittest
from textwrap import dedent

from src.day7 import Day7


class TestDay7(unittest.TestCase):
    def test_part_one(self):
        test_input = dedent(
            """\
            123 -> x
            456 -> y
            x AND y -> d
            x OR y -> e
            x LSHIFT 2 -> f
            y RSHIFT 2 -> g
            NOT x -> h
            NOT y -> i"""
        )

        self.assertEqual(Day7(test_input).part_one("d"), 72)
        self.assertEqual(Day7(test_input).part_one("e"), 507)
        self.assertEqual(Day7(test_input).part_one("f"), 492)
        self.assertEqual(Day7(test_input).part_one("g"), 114)
        self.assertEqual(Day7(test_input).part_one("h"), 65412)
        self.assertEqual(Day7(test_input).part_one("i"), 65079)
        self.assertEqual(Day7(test_input).part_one("x"), 123)
        self.assertEqual(Day7(test_input).part_one("y"), 456)

    def test_part_two(self):
        test_input = dedent(
            """\
            123 -> x
            456 -> y
            x AND y -> d
            x OR y -> e
            x LSHIFT 2 -> f
            y RSHIFT 2 -> g
            NOT x -> h
            NOT y -> i"""
        )

        self.assertEqual(Day7(test_input).part_two("h", "x"), 123)
        self.assertEqual(Day7(test_input).part_two("i", "y"), 456)


if __name__ == "__main__":
    unittest.main()
