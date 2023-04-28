import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([1, 2, 3, 4], -1, 'test'), 'test')

        with self.assertRaises(IndexError):
            arrs.get([], 0, "test")

        with self.assertRaises(IndexError):
            arrs.get([1, 2, 3, 4], 18, "test")

        with self.assertRaises(TypeError):
            arrs.get([1, 2, 3], '2', "test")

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice(['1', '2', '3'], 2, 6), ['3'])
        self.assertEqual(arrs.my_slice([], 2, 6), [])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -6, -6), [])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4]), [1, 2, 3, 4])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 6, -6), [])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -1, 6), [4])
        self.assertEqual(arrs.my_slice([1, 2, 3], -1), [3])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 6, 6), [])

        with self.assertRaises(TypeError):
            arrs.my_slice(['1', '2', '3'], 2, '6')

        with self.assertRaises(TypeError):
            arrs.my_slice([1, 2, 3], '2', 6)

        with self.assertRaises(TypeError):
            arrs.my_slice([1, 2, 3], '2', '6')

        with self.assertRaises(TypeError):
            arrs.my_slice({1, 2, 3}, 2, 6)


if __name__ == '__main__':
    unittest.main()
