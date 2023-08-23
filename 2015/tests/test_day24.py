import unittest

from src.day24 import Day24


class TestDay23(unittest.TestCase):
    def test_part_one(self):
        test_input = "\n".join(["1", "2", "3", "4", "5", "7", "8", "9", "10", "11"])

        self.assertEqual(Day24(test_input).part_one(), 99)

    def test_part_two(self):
        test_input = "\n".join(["1", "2", "3", "4", "5", "7", "8", "9", "10", "11"])

        self.assertEqual(Day24(test_input).part_two(), 44)


if __name__ == "__main__":
    unittest.main()
