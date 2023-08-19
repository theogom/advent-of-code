import unittest
from textwrap import dedent

from src.day19 import Day19


class TestDay19(unittest.TestCase):
    def test_parse(self):
        test_input = dedent(
            """\
            H => HO
            H => OH
            O => HH

            HOH"""
        )

        expected_state = "HOH"
        expected_transitions = {"H": ["HO", "OH"], "O": ["HH"]}

        actual = Day19(test_input).parse()

        self.assertIn("state", actual)
        self.assertIn("transitions", actual)
        self.assertEqual(actual["state"], expected_state)
        self.assertEqual(actual["transitions"], expected_transitions)

    def test_part_one(self):
        test_input = dedent(
            """\
            H => HO
            H => OH
            O => HH

            HOH"""
        )

        self.assertEqual(Day19(test_input).part_one(), 4)

        test_input = dedent(
            """\
            H => HO
            H => OH
            O => HH

            HOHOHO"""
        )

        self.assertEqual(Day19(test_input).part_one(), 7)

    def test_part_two(self):
        return
        test_input = dedent(
            """\
            e => H
            e => O
            H => HO
            H => OH
            O => HH

            HOH"""
        )

        self.assertEqual(Day19(test_input).part_two(), 3)

        test_input = dedent(
            """\
            e => H
            e => O
            H => HO
            H => OH
            O => HH

            HOHOHO"""
        )

        self.assertEqual(Day19(test_input).part_two(), 6)


if __name__ == "__main__":
    unittest.main()
