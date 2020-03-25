import random

class Grid():
    """
    The class that encapsulates the grid on which we'll be performing the percolation simulation

    Grid is initialized with porosity = 0 (meaning it's all `1` or walls)
    We will randomly add pores to match `initial_porosity` if given
    """
    def __init__(self, width=None, height=None, initial_porosity=0):
        if width is None or height is None:
            raise ValueError(f"Must have numeric width and height. Got {width}, {height}")

        self._width = width
        self._height = height

        # 2D array of 0/1 corresponding to the grid of pores/walls
        # This is for visualization purposes only
        self._grid_matrix = self.__set_grid_matrix(width, height)

        # 1D list of 0/1 corresponding to the grid of pores/walls
        # For calculations it is more efficient to deal with a vector than a matrix
        self._grid_vector = self.__set_grid_vector(self._grid_matrix)

        # Sets that contain the vector indices for pores and walls
        self._pores_vector_indices_set = set([])
        self._walls_vector_indices_set = set([i for i in range(len(self._grid_vector))])

        # If porosity is given, add a new pore to increase porosity
        self._initialize_grid_to_match_porosity(initial_porosity)

    # loop through entire matrix to get the porosity (slow, used for testing purposes)
    def get_porosity_by_matrix(self):
        total_pores = 0

        for row in self._grid_matrix:
            for cell in row:
                if cell == 0:
                    total_pores += 1

        return total_pores/self.area

    # get porosity by calculating len of pore/wall vectors (fast)
    @property
    def porosity(self):
        total_pores = len(self._pores_vector_indices_set)
        return total_pores / self.area

    @property
    def area(self):
        return self._width * self._height

    def _initialize_grid_to_match_porosity(self, porosity):
        while self.porosity < porosity:
            self.add_random_pore()
            print(self.porosity)
            print(self._grid_matrix)

    def add_random_pore(self):
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

    def __set_grid_matrix(self, width, height):
        matrix = [[1 for col in range(width)] for row in range(height)]

        return matrix

    def __set_grid_vector(self, grid_matrix):
        vector = []

        for row in grid_matrix:
            for cell in row:
                vector.append(cell)

        return vector

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

    def __grid_coords_to_vector_index(self, row_index=None, col_index=None):
         # Reverse operation from __vector_to_grid_coords()

        return row_index * self._height + col_index
