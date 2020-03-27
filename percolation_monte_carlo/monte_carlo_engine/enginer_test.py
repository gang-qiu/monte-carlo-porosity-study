import unittest
from percolation_monte_carlo.monte_carlo_engine import Engine
from percolation_monte_carlo.grid import Grid


class EngineTest(unittest.TestCase):
    def setUp(self):
        self.engine = Engine(width=50, height=50)

    def test_simulate_one_grid(self):
        grid_not_connected = self.engine._simulate_one_grid(0.01)
        grid_connected = self.engine._simulate_one_grid(0.99)

        self.assertIsInstance(grid_connected, Grid)
        self.assertIsInstance(grid_not_connected, Grid)
        self.assertFalse(grid_not_connected.is_connected)
        self.assertTrue(grid_connected.is_connected)

    def test_simulate_many_grids(self):
        num_times = 5
        grids = self.engine._simulate_many_grids(num_times=num_times, porosity=0.99)

        self.assertEqual(len(grids), num_times)
        for grid in grids:
            self.assertTrue(grid.is_connected)

    def test_get_average_percolation_rate_for_porosity(self):
        average_percolation_rate = self.engine.get_average_percolation_rate_for_porosity(porosity=0.6)
        self.assertTrue(0 <= average_percolation_rate and average_percolation_rate <= 1, f"Expected average between 0 - 1. Got {average_percolation_rate}")