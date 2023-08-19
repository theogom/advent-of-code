import unittest
from textwrap import dedent

from src.day15 import Day15


class TestDay15(unittest.TestCase):
    def test_part_one(self):
        test_input = dedent(
            """\
            Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
            Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"""
        )

        self.assertEqual(
            Day15(test_input).part_one(),
            62842880,
        )

    def test_part_two(self):
        test_input = dedent(
            """\
            Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
            Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"""
        )

        self.assertEqual(
            Day15(test_input).part_two(),
            57600000,
        )


if __name__ == "__main__":
    unittest.main()
