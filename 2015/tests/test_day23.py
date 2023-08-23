import unittest
from textwrap import dedent

from src.day23 import Day23


class TestDay23(unittest.TestCase):
    def test_part_one(self):
        test_input = dedent(
            """\
                inc a
                jio a, +2
                tpl a
                inc a"""
        )

        self.assertEqual(Day23(test_input).part_one("a"), 2)

    def test_part_two(self):
        pass


if __name__ == "__main__":
    unittest.main()
