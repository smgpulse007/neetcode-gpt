"""Regression checks for the implemented exercise and scaffold imports."""

import importlib
import unittest

from foundations import Solution
from foundations.gradient_descent import Solution as ExerciseSolution


class FoundationsTests(unittest.TestCase):
    def test_package_exports_existing_exercise(self):
        self.assertIs(Solution, ExerciseSolution)

    def test_placeholder_packages_are_importable(self):
        for name in ("model", "data"):
            with self.subTest(package=name):
                importlib.import_module(name)

    def test_documented_example(self):
        self.assertEqual(Solution().get_minimizer(10, 0.1, 5), 0.53687)

    def test_converges_toward_zero_from_either_sign(self):
        for initial in (-5, 5):
            with self.subTest(initial=initial):
                result = Solution().get_minimizer(100, 0.1, initial)
                self.assertAlmostEqual(result, 0, places=5)

    def test_zero_iterations_preserves_initial_value(self):
        self.assertEqual(Solution().get_minimizer(0, 0.1, 5), 5)


if __name__ == "__main__":
    unittest.main()
