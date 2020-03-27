import unittest
from percolation_monte_carlo.grid.grid import Grid

class GridTest(unittest.TestCase):
    def test_matrix(self):
        grid = Grid(width=4, height=2)
        expected_grid = [
            [1,1,1,1],
            [1,1,1,1],
        ]

        self.assertListEqual(grid._grid_matrix, expected_grid)

    def test_vector(self):
        grid = Grid(width=4, height=2)
        expected_vector = [1,1,1,1,1,1,1,1]
        self.assertListEqual(grid._grid_vector, expected_vector)

    def test_grid_porosity(self):
        grid1 = Grid(width=4, height=4, porosity=0.5)
        self.assertAlmostEqual(grid1.porosity, 0.5)
        self.assertAlmostEqual(grid1.get_porosity_by_matrix(), 0.5)

        grid2 = Grid(width=40, height=40, porosity=0.5)
        self.assertAlmostEqual(grid2.porosity, 0.5)
        self.assertAlmostEqual(grid2.get_porosity_by_matrix(), 0.5)

    def test_grid_connection(self):
        grid1 = Grid(width=10, height=10, porosity=0)
        self.assertFalse(grid1.is_connected)

        grid2 = Grid(width=10, height=10, porosity=1)
        self.assertTrue(grid2.is_connected)
        # [print(row) for row in grid2._grid_matrix]

    def test_connected_grids(self):
        grid_1 = [
            [0, 0, 1, 1],
            [1, 0, 1, 1],
            [1, 0, 0, 1],
            [0, 1, 0, 1],
        ]

        grid_2 = [
            [0, 1, 1, 1],
            [0, 1, 1, 1],
            [0, 0, 0, 0],
            [1, 1, 1, 0],
        ]

        self.assertTrue(Grid(grid_matrix=grid_1).is_connected)
        self.assertTrue(Grid(grid_matrix=grid_2).is_connected)

    def test_not_connected_grids(self):
        grid_1 = [
            [0, 1, 1, 1],
            [1, 1, 0, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 0],
        ]
        grid_2 = [
            [0, 0, 1, 0],
            [1, 0, 1, 0],
            [1, 0, 1, 0],
            [1, 1, 0, 1],
        ]

        self.assertFalse(Grid(grid_matrix=grid_1).is_connected)
        self.assertFalse(Grid(grid_matrix=grid_2).is_connected)

    def test_irregular_connected_grids(self):
        grid_1 = [
            [0, 0, 0],
            [1, 0, 0],
            [1, 0, 0],
            [1, 1, 0],
        ]
        grid_2 = [
            [0, 0, 1, 1],
            [1, 0, 1, 1],
            [1, 0, 0, 1],
        ]
        grid_3 = [
            [0, 0, 1, 1],
            [1, 0, 1, 1],
            [1, 0, 0, 1],
            [1, 1, 0, 1],
            [1, 0, 0, 1],
            [1, 0, 1, 1],
        ]
        self.assertTrue(Grid(grid_matrix=grid_1).is_connected)
        self.assertTrue(Grid(grid_matrix=grid_2).is_connected)
        self.assertTrue(Grid(grid_matrix=grid_3).is_connected)

    def test_irregular_not_connected_grids(self):
        grid_1 = [
            [0, 0, 1, 1],
            [0, 0, 0, 0],
            [1, 1, 1, 1],
        ]
        grid_2 = [
            [0, 0, 1, 1],
            [0, 0, 1, 1],
            [1, 1, 0, 0],
        ]
        grid_3 = [
            [0, 0, 1, 1, 0, 1],
            [0, 0, 1, 0, 0, 1],
            [0, 0, 1, 0, 1, 0],
            [1, 1, 0, 1, 0, 1],
        ]
        self.assertFalse(Grid(grid_matrix=grid_1).is_connected)
        self.assertFalse(Grid(grid_matrix=grid_2).is_connected)
        self.assertFalse(Grid(grid_matrix=grid_3).is_connected)
