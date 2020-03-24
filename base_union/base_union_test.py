import unittest

class BaseTestCases:
    class BaseUnionTest(unittest.TestCase):
        _UNION_TEST_CLASS = None

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            if self._UNION_TEST_CLASS is None:
                raise Exception("Need to set self._UNION_TEST_CLASS")

        def test_case1(self):
            uf2 = self._UNION_TEST_CLASS(10)

            union_coords = [
                [1, 2], [3, 4], [5, 6], [7, 8],
                [7, 9], [2, 8], [0, 5], [1, 9],
            ]

            for coords in union_coords:
                uf2.union(*coords)

            self.assertTrue(uf2.is_connected(0, 6))
            self.assertTrue(uf2.is_connected(5, 6))
            self.assertTrue(uf2.is_connected(3, 4))
            self.assertTrue(uf2.is_connected(1, 2))
            self.assertTrue(uf2.is_connected(1, 7))
            self.assertTrue(uf2.is_connected(1, 8))
            self.assertTrue(uf2.is_connected(2, 9))

            self.assertFalse(uf2.is_connected(0, 3))
            self.assertFalse(uf2.is_connected(0, 4))
            self.assertFalse(uf2.is_connected(5, 4))
            self.assertFalse(uf2.is_connected(5, 1))
            self.assertFalse(uf2.is_connected(5, 7))
            self.assertFalse(uf2.is_connected(5, 9))
            self.assertFalse(uf2.is_connected(4, 8))

        def test_union_find_case2(self):
            uf = self._UNION_TEST_CLASS(10)

            union_coords = [
                [0,5], [5,6], [6,1], [1,2],
                [4,9], [3,4], [3,8], [2,7],
            ]

            for coords in union_coords:
                uf.union(*coords)

            self.assertTrue(uf.is_connected(0,6))
            self.assertTrue(uf.is_connected(5,6))
            self.assertTrue(uf.is_connected(1,2))
            self.assertTrue(uf.is_connected(1,7))
            self.assertTrue(uf.is_connected(2,1))

            self.assertFalse(uf.is_connected(0,3))
            self.assertFalse(uf.is_connected(0,4))
            self.assertFalse(uf.is_connected(7,8))
            self.assertFalse(uf.is_connected(5,9))


if __name__ == '__main__':
    unittest.main()