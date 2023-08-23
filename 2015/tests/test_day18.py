import unittest
from textwrap import dedent

from src.day18 import Day18


class TestDay18(unittest.TestCase):
    def test_part_one(self):
        test_input = dedent(
            """\
            .#.#.#
            ...##.
            #....#
            ..#...
            #.#..#
            ####.."""
        )
        self.assertEqual(Day18(test_input).part_one(4), 4)

    def test_part_two(self):
        test_input = dedent(
            """\
            ##.#.#
            ...##.
            #....#
            ..#...
            #.#..#
            ####.#"""
        )
        self.assertEqual(Day18(test_input).part_two(5), 17)


if __name__ == "__main__":
    unittest.main()
