from percolation_monte_carlo.grid import Grid


class Engine:
    def __init__(self, width=None, height=None):
        if width is None or height is None:
            raise ValueError("width and height must be given")

        self._width = width
        self._height = height

    def get_average_percolation_rates_for_porosity_list(self, porosity_list):
        '''

        :param porosity_list: a list of porosity values between 0 and 1
        :return: a dict keyed by the porosity (str) and valued by the average percolation rate
        '''
        if type(porosity_list) is not list:
            raise ValueError("Need to pass a list of porosity values")

        result = {}
        for porosity in porosity_list:
            result[str(porosity)] = self.get_average_percolation_rate_for_porosity(porosity)

        return result

    def get_average_percolation_rate_for_porosity(self, porosity=None, num_times=10):
        if type(porosity) is not float or porosity < 0 or porosity > 1:
            raise ValueError("Must provide a porosity as floating point number between 0 and 1")

        grids = self._simulate_many_grids(porosity, num_times)
        num_connected_grids = 0
        for grid in grids:
            num_connected_grids += 1 if grid.is_connected else 0

        return num_connected_grids/len(grids)

    def _simulate_many_grids(self, porosity, num_times):
        return [self._simulate_one_grid(porosity=porosity) for _ in range(num_times)]

    def _simulate_one_grid(self, porosity):
        return Grid(width=self._width, height=self._height, porosity=porosity)
