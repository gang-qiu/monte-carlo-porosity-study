import unittest
from percolation_monte_carlo.percolation_generator.grid import Grid

class GridTest(unittest.TestCase):
    def test_matrix(self):
        grid = Grid(width=4, height=2)
        expected_grid = [
            [0,0,0,0],
            [0,0,0,0],
        ]

        self.assertListEqual(grid._grid_matrix, expected_grid)

    def test_vector(self):
        grid = Grid(width=4, height=2)
        expected_vector = [0,0,0,0,0,0,0,0]
        self.assertListEqual(grid._grid_vector, expected_vector)

    def test_grid_porosity(self):
        grid = Grid(width=4, height=4, porosity=0.5)
        self.assertAlmostEquals(grid.porosity, 0.5)