from cgitb import text
from operator import index
import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import csv

df=pd.read_csv("data.csv")
data=df["temp"].tolist()

population_mean=statistics.mean(data)
std_deviation=statistics.stdev(data)

def show_fig(mean_list):
    df=mean_list
    fig=ff.create_distplot([data],["temp"],show_hist=False)
    fig.show()


def random_set_of_mean(counter):
    dataset=[]
    for i in range (0,100):
        random_index=random.randint(0,len(data))
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

def setup():
    mean_list=[]
    for i in range (0,100):
        setoffmean=random_set_of_mean(100)
        mean_list.append(setoffmean)
    show_fig(mean_list)

setup()