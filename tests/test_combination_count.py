import unittest
from tools.combination_count import run


class CombinationCountTests(unittest.TestCase):
    def test_example(self):
        self.assertEqual("10", run("5", "3"))

    def test_empty_selection_and_empty_set(self):
        self.assertEqual("1", run("0", "0"))
        self.assertEqual("1", run("9", "0"))

    def test_all_items_and_selection_larger_than_set(self):
        self.assertEqual("1", run("5", "5"))
        self.assertEqual("0", run("5", "6"))

    def test_large_result_is_exact(self):
        self.assertEqual("100891344545564193334812497256", run("100", "50"))

    def test_symmetry(self):
        self.assertEqual(run("20", "3"), run("20", "17"))

    def test_invalid_input(self):
        for args in (("-1", "2"), ("5", "-1"), ("5.0", "2"), ("five", "2"), (), ("5",), ("5", "2", "extra")):
            with self.subTest(args=args), self.assertRaises(ValueError):
                run(*args)
