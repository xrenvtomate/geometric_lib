import unittest

from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    def test_area_zero_radius(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_positive_radius(self):
        res = area(2)
        self.assertAlmostEqual(res, 12.566370614359172, places=5)

    def test_perimeter_zero_radius(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_positive_radius(self):
        res = perimeter(1)
        self.assertAlmostEqual(res, 6.283185307179586, places=5)
