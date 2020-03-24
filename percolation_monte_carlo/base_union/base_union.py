class BaseUnion:
    def __init__(self, num_elems):
        self._ids = [x for x in range(num_elems)]

    def union(self, n1, n2):
        pass

    def is_connected(self, n1, n2):
        pass

    def __get_ids_for_nums(self, num1, num2):
        pass

    def __get_id_for_num(self, num):
        pass

    def __set_id_for_num(self, num, val):
        pass