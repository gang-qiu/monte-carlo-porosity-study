from percolation_monte_carlo.quick_union import QuickUnion


class QuickerUnion(QuickUnion):
    _id_weights = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._id_weights = [1 for _ in range(len(self._ids))]

    def union(self, n1, n2):
        root1, root2 = self._get_ids_for_nums(n1, n2)
        weight1, weight2 = self._get_weights_for_nums(root1, root2)
        new_root = None
        sub_root = None
        node_in_new_root = None

        if root1 != root2:
            new_weight = weight1 + weight2

            # insert the smaller tree into the larger one
            # increment the weight of the larger tree
            if weight1 >= weight2:
                new_root = root1
                sub_root = root2
                node_in_new_root = n1
            else:
                new_root = root2
                sub_root = root1
                node_in_new_root = n2

            self._set_id_for_num(sub_root, new_root)
            self._set_weight(new_root, new_weight)

        return (node_in_new_root, new_root)

    def _get_weights_for_nums(self, num1, num2):
        return (
            self._get_weight(num1),
            self._get_weight(num2)
        )

    def _get_weight(self, root):
        # Assumes that the input is the root node
        return self._id_weights[root]

    def _set_weight(self, root, val):
        self._id_weights[root] = val