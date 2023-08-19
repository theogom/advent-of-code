import unittest

from src.day8 import Day8


class TestDay8(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(
            Day8("\n".join([r'""', r'"abc"', r'"aaa\"aaa"', r'"\x27"'])).part_one(),
            12,
        )

    def test_part_two(self):
        self.assertEqual(
            Day8("\n".join([r'""', r'"abc"', r'"aaa\"aaa"', r'"\x27"'])).part_two(), 19
        )


if __name__ == "__main__":
    unittest.main()
