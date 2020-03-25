from percolation_monte_carlo.union_utils.base_union import BaseUnion


class QuickUnion(BaseUnion):
    def union(self, n1, n2):
        # Set the value for a node to be it's root
        root1, root2 = self._get_ids_for_nums(n1, n2)

        if root1 != root2:
            self._set_id_for_num(root1, root2)

    def is_connected(self, n1, n2):
        root1, root2 = self._get_ids_for_nums(n1, n2)
        return root1 == root2

    def _get_ids_for_nums(self, num1, num2):
        return (
            self._get_id_for_num(num1),
            self._get_id_for_num(num2)
        )

    def _get_id_for_num(self, num):
        # Get the "root" of an element
        parent = self._ids[num]

        if parent == num:
            # We found the root. Return
            return parent
        else:
            # Intermediate node. recurse one level
            return self._get_id_for_num(parent)

    def _set_id_for_num(self, num, val):
        self._ids[num] = val
