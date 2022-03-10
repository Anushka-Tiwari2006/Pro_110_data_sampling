import pandas as pd
import csv
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
import random

df = pd.read_csv("medium_data.csv")
data = df["id"].to_list()

mean_of_population = statistics.mean(data)
print(mean_of_population)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean


def show_figure(mean_list):
    df = mean_list
    fig = ff.create_distplot([df],["id"],show_hist=False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)
        show_figure(mean_list)

setup()


