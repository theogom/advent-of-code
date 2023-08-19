import unittest
from textwrap import dedent

from src.day20 import Day20


class TestDay20(unittest.TestCase):
    def test_parse(self):
        self.assertEqual(Day20("2000").parse(), 2000)

    def test_part_one(self):
        self.assertEqual(Day20("10").part_one(), 1)
        self.assertEqual(Day20("30").part_one(), 2)
        self.assertEqual(Day20("40").part_one(), 3)
        self.assertEqual(Day20("60").part_one(), 4)
        self.assertEqual(Day20("70").part_one(), 4)
        self.assertEqual(Day20("80").part_one(), 6)
        self.assertEqual(Day20("120").part_one(), 6)
        self.assertEqual(Day20("130").part_one(), 8)
        self.assertEqual(Day20("150").part_one(), 8)

    def test_part_two(self):
        pass


if __name__ == "__main__":
    unittest.main()
