import unittest

from src.day4 import Day4


class TestDay4(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(Day4("abcdef").part_one(), 609043)
        self.assertEqual(Day4("pqrstuv").part_one(), 1048970)

    def test_part_two(self):
        pass


if __name__ == "__main__":
    unittest.main()
