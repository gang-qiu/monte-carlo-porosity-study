from percolation_monte_carlo.quicker_union import QuickerUnion


class QuickestUnion(QuickerUnion):
    def union(self, n1, n2):
        root1, root2 = self._get_ids_for_nums(n1, n2)
        weight1, weight2 = self._get_weights_for_nums(root1, root2)

        if root1 != root2:
            new_weight = weight1 + weight2
            new_root = None
            sub_root = None
            node_to_compress = None

            # insert the smaller tree into the larger one
            # increment the weight of the larger tree
            if weight1 >= weight2:
                new_root = root1
                sub_root = root2
                node_to_compress = n1
            else:
                new_root = root2
                sub_root = root1
                node_to_compress = n2

            self._set_id_for_num(sub_root, new_root)
            self._set_weight(new_root, new_weight)
            self._set_id_for_num(node_to_compress, new_root)

