import random
from percolation_monte_carlo.union_utils import QuickestUnion


class Grid():
    """
    The class that encapsulates the grid on which we'll be performing the percolation simulation

    Grid is initialized with porosity = 0 (meaning it's all `1` or walls)
    We will randomly add pores to match `initial_porosity` if given
    """

    def __init__(self, width=None, height=None, porosity=0, grid_matrix=None):
        self._width = None
        self._height = None

        # 2D array of 0/1 corresponding to the grid of pores/walls
        # This is for visualization purposes only
        self._grid_matrix = None

        # 1D list of 0/1 corresponding to the grid of pores/walls
        # For calculations it is more efficient to deal with a vector than a matrix
        self._grid_vector = None

        # Sets that contain the vector indices for pores and walls
        self._pores_vector_indices_set = None
        self._walls_vector_indices_set = None

        # create a graph representation of the grid with the QuickestUnion module
        self._union_graph = None

        if grid_matrix is None:
            # Set up a blank matrix based on porosity
            self.__set_grid_matrix(width=width, height=height)
            self.__setup_grid_to_match_porosity(porosity)
        else:
            # Set up grid based on the input matrix
            self.__set_grid_matrix(matrix=grid_matrix)

        self.__set_union_graph()
        self.__percolate()

    # loop through entire matrix to get the porosity (slow, used for testing purposes)
    def get_porosity_by_matrix(self):
        total_pores = 0

        for row in self._grid_matrix:
            for cell in row:
                if cell == 0:
                    total_pores += 1

        return total_pores/self.area

    # use the graph representation to determine if the top and bottom are connected
    @property
    def is_connected(self):
        entrance_index = self.__get_virtual_node_index(entrance_node=True)
        exit_index = self.__get_virtual_node_index(exit_node=True)
        return self._union_graph.is_connected(entrance_index, exit_index)

    # get porosity by calculating len of pore/wall vectors (fast)
    @property
    def porosity(self):
        total_pores = len(self._pores_vector_indices_set)
        return total_pores / self.area

    @property
    def area(self):
        return self._width * self._height

    # loop through entire vector and union the pores
    def __percolate(self):
        # loop through the entrance and exit and union the pores to the virtual nodes
        self.__union_pores_to_virtual_node(is_entrance=True)
        self.__union_pores_to_virtual_node(is_exit=True)

        for cell_index in range(len(self._grid_vector)):
            self.__union_pore_to_neighboring_pores(cell_index)

    def __setup_grid_to_match_porosity(self, porosity):
        while self.porosity < porosity:
            self.__add_random_pore()


    def __add_random_pore(self):
        '''
        adds a random pore to the grid. updates sets, vector, and grid
        :return: vector index of the pore added
        '''
        new_pore_index = random.sample(self._walls_vector_indices_set, 1)[0]
        self._walls_vector_indices_set.remove(new_pore_index)
        new_pore_row, new_por_col = self.__vector_to_grid_coords(new_pore_index)

        self._pores_vector_indices_set.add(new_pore_index)
        self._grid_vector[new_pore_index] = 0
        self._grid_matrix[new_pore_row][new_por_col] = 0

    def __set_grid_matrix(self, matrix=None, width=None, height=None):
        if matrix is None:
            if width is None or height is None:
                raise ValueError(f"Must have numeric width and height. Got {width}, {height}")

            self._width = width
            self._height = height
            self._grid_matrix = [[1 for col in range(width)] for row in range(height)]
        else:
            self._height = len(matrix)
            self._width  = len(matrix[0])
            self._grid_matrix = matrix

        self.__set_grid_vector()

    def __set_grid_vector(self):
        self._grid_vector = []
        self._pores_vector_indices_set = set([])
        self._walls_vector_indices_set = set([])

        for row_index, row in enumerate(self._grid_matrix):
            for col_index, cell in enumerate(row):
                vector_index = len(self._grid_vector)
                self._grid_vector.append(cell)
                vector_index_set = self._pores_vector_indices_set if cell == 0 else self._walls_vector_indices_set
                vector_index_set.add(vector_index)

    def __set_union_graph(self):
        graph_size = len(self._grid_vector) + 2   # two for virtual nodes at the entrance and exit
        self._union_graph = QuickestUnion(graph_size)

    def __vector_to_grid_coords(self, vector_index):
        '''
        :param vector_index: int of index in self._map_vector
        :return: tuple of i,j coords cooresponding to self._grid

        width = 4, height = 2
        _map_vector => [0,1,2,3,4,5,6,7]
        _grid => [[(0,0),(0,1),(0,2),(0,3)], [(1,0),(1,1),(1,2),(1,3)]]

        a vector of 2 should return (0,2)
        '''

        row_index = vector_index // self._width  # Integer floor division
        col_index = vector_index % self._width    # modulo width
        return (row_index, col_index)

    def __grid_coords_to_vector_index(self, coords_tuple):
        # Reverse operation from __vector_to_grid_coords()
        if coords_tuple is None:
            return None

        row_index, col_index = coords_tuple
        return row_index * self._height + col_index

    def __get_virtual_node_index(self, entrance_node=False, exit_node=False):
        return len(self._grid_vector) + (0 if entrance_node else 1)

    def __union_pore_to_virtual_node(self, pore_vector_index, entrance_node=False, exit_node=False):
        # union the pore at the vector index with the entrance of exit node
        self._union_graph.union(self.__get_virtual_node_index(entrance_node, exit_node), pore_vector_index)

    def __union_pores_to_virtual_node(self, is_entrance=False, is_exit=False):
        virtual_node = self.__get_virtual_node_index(is_entrance, is_exit)
        row_index = 0 if is_entrance else self._height - 1
        matrix_row = self._grid_matrix[row_index]

        for col_index, cell in enumerate(matrix_row):
            if cell == 0:
                vector_index = self.__grid_coords_to_vector_index((row_index, col_index))
                self.__union_pore_to_virtual_node(vector_index, is_entrance, is_exit)

    def __union_pore_to_neighboring_pores(self, pore_vector_index):
        # examine 4 neighbors of a pore. If any are pores then union them in the graph
        for neighbor_vector_index in self.__get_neighboring_cell_vector_indices(pore_vector_index):
            if neighbor_vector_index is None:
                continue

            cell = self._grid_vector[neighbor_vector_index]

            if cell == 0:  # pore
                self._union_graph.union(pore_vector_index, neighbor_vector_index)


    def __get_neighboring_cell_vector_indices(self, pore_vector_index):
        # for a given pore, return a tuple containing the coordinates of all its neighboring cells

        # convert vector index to grid coordinates
        (row, col) = self.__vector_to_grid_coords(pore_vector_index)
        coords = [
            (row - 1, col) if row > 0 else None,
            (row + 1, col) if row < self._height - 1 else None,
            (row, col - 1) if col > 0 else None,
            (row, col + 1) if col < self._width - 1 else None,
        ]

        return map(self.__grid_coords_to_vector_index, coords)

