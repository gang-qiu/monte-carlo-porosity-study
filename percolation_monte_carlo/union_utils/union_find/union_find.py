class UnionFind:
    def __init__(self, num_elems):
        self._ids = [x for x in range(num_elems)]

    def union(self, n1, n2):
        # get ids of two numbers
        id1, id2 = self.__get_ids_for_nums(n1, n2)

        # if mismatch, convert all ids == id2 -> id1
        for idx, id in enumerate(self._ids):
            if id == id2:
                self._ids[idx] = id1

    def is_connected(self, n1, n2):
        id1, id2 = self.__get_ids_for_nums(n1, n2)
        return id1 == id2

    def __get_ids_for_nums(self, num1, num2):
        return (self.__get_id_for_num(num1), self.__get_id_for_num(num2),)

    def __get_id_for_num(self, num):
        return self._ids[num]

    def __set_id_for_num(self, num, val):
        self._id[num] = val