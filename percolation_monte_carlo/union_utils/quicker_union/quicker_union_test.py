from percolation_monte_carlo.union_utils.base_union import BaseTestCases
from percolation_monte_carlo.union_utils.quicker_union import QuickerUnion


class QuickerUnionTest(BaseTestCases.BaseUnionTest):
    _UNION_TEST_CLASS = QuickerUnion

    def test_weights(self):
        # ensure that the weights array is being set correctly
        uf = self._UNION_TEST_CLASS(5)

        uf.union(0,1)
        self.assertListEqual(uf._id_weights, [2,1,1,1,1])
        self.assertListEqual(uf._ids, [0,0,2,3,4])
        uf.union(0,2)
        self.assertListEqual(uf._id_weights, [3,1,1,1,1])
        self.assertListEqual(uf._ids, [0,0,0,3,4])
        uf.union(3,4)
        self.assertListEqual(uf._id_weights, [3,1,1,2,1])
        self.assertListEqual(uf._ids, [0,0,0,3,3])
        uf.union(2,4)
        self.assertListEqual(uf._id_weights, [5,1,1,2,1])
        self.assertListEqual(uf._ids, [0,0,0,0,3])




