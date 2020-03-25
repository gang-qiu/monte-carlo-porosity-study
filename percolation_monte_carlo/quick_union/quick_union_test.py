from percolation_monte_carlo.base_union import BaseTestCases
from percolation_monte_carlo.quick_union import QuickUnion


class QuickUnionTest(BaseTestCases.BaseUnionTest):
    _UNION_TEST_CLASS = QuickUnion

