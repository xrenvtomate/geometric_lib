import unittest

from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    def test_area_zero_base_or_height(self):
        res = area(0, 3)
        self.assertEqual(res, 0.0)
        res = area(4, 0)
        self.assertEqual(res, 0.0)

    def test_area_positive_base_and_height(self):
        res = area(4, 3)
        self.assertEqual(res, 6.0)

    def test_perimeter_zero_side(self):
        res = perimeter(0, 4, 5)
        self.assertEqual(res, 9)

    def test_perimeter_positive_sides(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)
