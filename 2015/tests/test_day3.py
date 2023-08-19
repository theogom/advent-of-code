import unittest

from src.day3 import Day3


class TestDay3(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(Day3(">").part_one(), 2)
        self.assertEqual(Day3("^>v<").part_one(), 4)
        self.assertEqual(Day3("^v^v^v^v^v").part_one(), 2)

    def test_part_two(self):
        self.assertEqual(Day3("^v").part_two(), 3)
        self.assertEqual(Day3("^>v<").part_two(), 3)
        self.assertEqual(Day3("^v^v^v^v^v").part_two(), 11)


if __name__ == "__main__":
    unittest.main()
