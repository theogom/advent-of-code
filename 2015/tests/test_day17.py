import unittest

from src.day17 import Day17


class TestDay17(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(Day17("\n".join(["20", "15", "10", "5", "5"])).part_one(25), 4)

    def test_part_two(self):
        self.assertEqual(Day17("\n".join(["20", "15", "10", "5", "5"])).part_two(25), 3)


if __name__ == "__main__":
    unittest.main()
