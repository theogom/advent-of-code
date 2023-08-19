import unittest

from src.day1 import Day1


class TestDay1(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(Day1("(())").part_one(), 0)
        self.assertEqual(Day1("()()").part_one(), 0)
        self.assertEqual(Day1("(((").part_one(), 3)
        self.assertEqual(Day1("(()(()(").part_one(), 3)
        self.assertEqual(Day1("))(((((").part_one(), 3)
        self.assertEqual(Day1("())").part_one(), -1)
        self.assertEqual(Day1("))(").part_one(), -1)
        self.assertEqual(Day1(")))").part_one(), -3)
        self.assertEqual(Day1(")())())").part_one(), -3)

    def test_part_two(self):
        self.assertEqual(Day1(")").part_two(), 1)
        self.assertEqual(Day1("()())").part_two(), 5)


if __name__ == "__main__":
    unittest.main()
