import unittest

from src.day5 import Day5


class TestDay5(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(Day5("ugknbfddgicrmopn").part_one(), 1)
        self.assertEqual(Day5("aaa").part_one(), 1)
        self.assertEqual(Day5("jchzalrnumimnmhp").part_one(), 0)
        self.assertEqual(Day5("haegwjzuvuyypxyu").part_one(), 0)
        self.assertEqual(Day5("dvszwmarrgswjxmb").part_one(), 0)

    def test_part_two(self):
        self.assertEqual(Day5("qjhvhtzxzqqjkmpb").part_two(), 1)
        self.assertEqual(Day5("xxyxx").part_two(), 1)
        self.assertEqual(Day5("uurcxstgmygtbstg").part_two(), 0)
        self.assertEqual(Day5("ieodomkazucvgmuy").part_two(), 0)


if __name__ == "__main__":
    unittest.main()
