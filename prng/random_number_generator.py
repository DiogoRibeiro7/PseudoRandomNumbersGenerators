# coding: utf-8

import time
import matplotlib.pyplot as plt

class RandomNumbersGenerator(object):

    def __init__(self):
        self.name = "Random Numbers Generator"
        self.seed = int(time.time()*(10**7))  # The default seed is a timestamp.

    def rand(self):
        raise NotYetImplemented("Please override this method.")

    def benchmark(self, iteration_count=1000000):
        print("Benchmarking {}...".format(self.name))
        print(self)

        begin_time = time.time()

        # It's a benchmark so it has to be fast in order to perform a lot of operations.
        # That's why I have used a dictionnary instead of a list because testing if a value exists is way faster.
        values = {}
        x_points_diagram = []
        y_points_diagram = []

        period_found = False

        for i in range(iteration_count):
            value = self.rand()
            # print(value)

            if value in values:
                values[value] += 1

                if not period_found:
                    print("Found period : ", i)
                    period_found = True

            else:
                values[value] = 1

            if i % 2 == 0:
                x_points_diagram.append(value)
            else:
                y_points_diagram.append(value)

        end_time = time.time()
        print("Done in {0:.2f} seconds.\n".format(end_time-begin_time))

        values_list = []

        # Convert dict into list, because matplotlib needs it.
        for item in values:
            for _ in range(values[item]):
                values_list.append(item)

        plt.hist(values_list, 50)
        plt.title(self.name)
        plt.xlabel("Value")
        plt.ylabel("Frequency")

        fix, ax = plt.subplots()
        ax.plot(x_points_diagram, y_points_diagram, 'o')
        ax.set_xlabel("Xk")
        ax.set_ylabel("Xk+1")
        ax.set_title(self.name)
        plt.show()

