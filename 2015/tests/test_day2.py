import unittest

from src.day2 import Day2


class TestDay2(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(Day2("2x3x4").part_one(), 58)
        self.assertEqual(Day2("1x1x10").part_one(), 43)

    def test_part_two(self):
        self.assertEqual(Day2("2x3x4").part_two(), 34)
        self.assertEqual(Day2("1x1x10").part_two(), 14)


if __name__ == "__main__":
    unittest.main()
