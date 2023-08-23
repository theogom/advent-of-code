import unittest

from src.day25 import Day25


class TestDay25(unittest.TestCase):
    def test_parse(self):
        self.assertEqual(
            list(
                Day25(
                    "To continue, please consult the code grid in the manual.  Enter the code at row 3010, column 3019."
                ).parse()
            ),
            [3009, 3018],
        )

    def test_part_one(self):
        self.assertEqual(
            Day25(
                "To continue, please consult the code grid in the manual.  Enter the code at row 1, column 3."
            ).part_one(),
            17289845,
        )

        self.assertEqual(
            Day25(
                "To continue, please consult the code grid in the manual.  Enter the code at row 6, column 5."
            ).part_one(),
            1534922,
        )

    def test_part_two(self):
        pass


if __name__ == "__main__":
    unittest.main()
