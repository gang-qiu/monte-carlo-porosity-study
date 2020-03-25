class Grid():
    """
    The class that encapsulates the grid on which we'll be performing the percolation simulation

    grid = Grid(
    """
    def __init__(self, width=None, height=None, porosity=0):
        if width is None or height is None:
            raise ValueError(f"Must have numeric width and height. Got {width}, {height}")

        self._width = width
        self._height = height
        self._target_porosity = porosity
        self._grid_matrix = self.__set_grid_matrix(width, height)
        self._grid_vector = self.__set_grid_vector(self._grid_matrix)

    @property
    def porosity(self):
        total_pores = 0

        for row in self._grid_matrix:
            for cell in row:
                if cell == 1:
                    total_pores += 1

        return total_pores/self.area

    @property
    def area(self):
        return self._width * self._height

    def __set_target_porosity(self, porosity):
        pass

    def __set_grid_matrix(self, width, height):
        matrix = [[0 for col in range(width)] for row in range(height)]

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
