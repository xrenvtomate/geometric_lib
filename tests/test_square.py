import unittest

from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    def test_area_zero_side(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_positive_side(self):
        res = area(4)
        self.assertEqual(res, 16)

    def test_perimeter_zero_side(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_positive_side(self):
        res = perimeter(4)
        self.assertEqual(res, 16)
