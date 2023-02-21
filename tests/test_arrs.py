import unittest
from utils import arrs


class TestArrs(unittest.TestCase):
    #
    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)

    def test_get_two(self):
        self.assertEqual(arrs.get([1, 2, 3], 0, "test"), 1)

    def test_get_three(self):
        self.assertEqual(arrs.get([1, 2, 3], -1, "test"), "test")

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])

    def test_slice_one(self):
        self.assertEqual(arrs.my_slice([1, 2, 3], -2), [2, 3])

    def test_slice_two(self):
        self.assertEqual(arrs.my_slice([]), [])

    def test_slice_three(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], -3), [3, 4, 5])

    def test_slice_four(self):
        self.assertEqual(arrs.my_slice([1, 2, 3], -4), [1, 2, 3])
