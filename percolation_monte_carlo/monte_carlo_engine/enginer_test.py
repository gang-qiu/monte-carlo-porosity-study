import unittest
from percolation_monte_carlo.monte_carlo_engine import Engine
from percolation_monte_carlo.grid import Grid


class EngineTest(unittest.TestCase):
    def setUp(self):
        self.engine = Engine(width=20, height=20)

    def _assert_value_is_between(self, val, lower, upper):
        self.assertTrue(lower <= val and val <= upper, f"Expected value to be between {lower} - {upper}. Got {val}")

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
        self._assert_value_is_between(average_percolation_rate, 0, 1)

    def test_get_average_percolation_rate_for_porosity_list(self):
        porosity_list = [
            (0.1,  1),
            (0.2,  2),
            (0.3,  3),
            (0.4,  4),
            (0.5,  7),
            (0.55, 8),
            (0.6,  7),
            (0.7,  3),
            (0.8,  2),
            (0.9,  1),
        ]
        percolation_rates = self.engine.get_average_percolation_rates_for_porosity_list(porosity_list)

        self.assertEqual(len(porosity_list), len(percolation_rates))
        for porosity, _ in porosity_list:
            rate = percolation_rates[str(porosity)]
            self._assert_value_is_between(rate, 0, 1)

