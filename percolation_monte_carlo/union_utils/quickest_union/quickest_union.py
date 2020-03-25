from percolation_monte_carlo.union_utils.quicker_union import QuickerUnion


class QuickestUnion(QuickerUnion):
    def union(self, n1, n2):
        node_to_compress, new_root = super().union(n1,n2)

        if new_root is not None:
            self._set_id_for_num(node_to_compress, new_root)
