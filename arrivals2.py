import math
import random
import csv
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.transforms import Bbox

random.seed(23)

def save_time_series(data, query, load_pattern):
    file_name = query + "_" + load_pattern
    with open(file_name +'.txt', "w") as text_file:
        row = ""
        for val in data:
            row += str(val) + ","
        row = row[:len(row) - 1]
        text_file.write(row)

def cosine_plot(time, query):
    cosine_period = 60
    if query == "query-1":
        amplitude = 1000
        yshift = 1000


    values = []
    indices = []
    for i in range(0, time):
        period = (2 * math.pi / cosine_period)
        val = yshift + amplitude * math.cos(period * i)
        val += random.randrange(-200, 200)
        values.append(val)
        indices.append(i)
    values = [int(val) for val in values]
    values = [-1*val if val < 0 else val for val in values]
    return indices, values

def random_walk(time, query):
    if query == "query-1":
        val = 1000

    values = []
    indices = []
    for i in range(0, time):
        val += random.randrange(-250, 250)
        values.append(val)
        indices.append(i)
    values = [int(val) for val in values]
    values = [-1*val if val < 0 else val for val in values]
    return indices, values






def main():
    experiment_time = 140
    queries = ["query-1", "query-3", "query-11"]
    #queries = ["query-1"]


    for query in queries:
        print("Generating load patterns for query: " + query)
        indices1, values1 = cosine_plot(experiment_time, query)
        indices2, values2 = random_walk(experiment_time, query)
        # indices3, values3 = increasing(experiment_time, query)
        # indices4, values4 = decreasing(experiment_time, query)

    print("length cosine: {} negative values: {}".format(len(values1), min(values1)))
    print("length random: {} negative values: {}".format(len(values1), min(values2)))


    save_time_series(values1, query, "cosine")
    save_time_series(values2, query, "random")



    all_values = [values1, values2]
    titles = ["Cosine", "Random"]

    fig, axs = plt.subplots(2,1, figsize=(30, 20), facecolor='w', edgecolor='k', sharex='all')
    fig.subplots_adjust(hspace = .5, wspace=.001)

    for i in range(0, 2):
        axs[i].title.set_text(titles[i])
        axs[i].plot(indices1, all_values[i], color="red")
        axs[i].grid()
        axs[i].set_ylabel("Records per second")

    axs[1].set_xlabel("Minutes")
    plt.show()

if __name__ == '__main__':
    #simulate()
    main()