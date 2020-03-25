from percolation_monte_carlo.union_utils.base_union import BaseTestCases
from percolation_monte_carlo.union_utils.quickest_union import QuickestUnion


class QuickestUnionTest(BaseTestCases.BaseUnionTest):
    _UNION_TEST_CLASS = QuickestUnion

    def test_path_compressions(self):
        uf = self._UNION_TEST_CLASS(8)

        uf.union(0, 1)
        uf.union(0, 2)
        uf.union(3, 4)
        uf.union(3, 5)
        uf.union(3, 6)
        uf.union(0, 3)
        self.assertListEqual(uf._ids, [3, 0, 0, 3, 3, 3, 3, 7])

        uf.union(2, 7)
        self.assertListEqual(uf._ids, [3, 0, 3, 3, 3, 3, 3, 3])
        #                                    ^ this is the new change. The supplied node was flattened to point to the node


