from percolation_monte_carlo.monte_carlo.simulator import Simulator
from pprint import pprint


def main():
    porosity_and_frequency_list = [
        (0.0,  1), (0.1,  2), (0.2,  3), (0.3,  4), (0.4,  5), (0.5,  10),
        (0.51, 11), (0.52, 12), (0.53, 20), (0.54, 20), (0.55, 20), (0.56, 25),
        (0.57, 35), (0.58, 50), (0.59, 100), (0.60, 70), (0.61, 50), (0.62, 40),
        (0.63, 30), (0.64, 26), (0.65, 25), (0.66, 24), (0.67, 22), (0.68, 16),
        (0.7,  4), (0.8,  3), (0.9,  2), (1.0,  1),
    ]
    engine = Simulator(width=40, height=40)
    result = engine.get_average_percolation_rates_for_porosity_list(porosity_and_frequency_list)
    pprint(result)

if __name__ == '__main__':
    main()