from figurelib.figure import FigureCollection
import matplotlib.pyplot as plt
from figures.cst_loader import load_cst_filePOLAR, load_cst_file
import numpy as np
import pickle
import random

from matplotlib.ticker import FuncFormatter

# Some example data to display

collection = FigureCollection("system_design")


@collection.plot_figure(only_build_this=False)
def S11_plot_for_parameterize():
    fig, ax = plt.subplots(1, 1, figsize=(5, 3))
    runids = 10

    file_to_load = "Data/Simple_wire_2_short.pkl"

    data = pickle.load(open(file_to_load, "rb"))

    print(data.keys())
    print(data["S1,1"].shape)

    # Make a list of random samples
    #random_indexes = random.sample(range(1880), runids)
    random_indexes = [55,1852,108,1266]

    #print(data["Parameter combination"][300] == data["Parameter combination"][301])


    for i in random_indexes:
        ax.plot(data["Frequency"],data["S1,1"][i])
    #plt.legend()

    ax.set_xlabel("Frequency [MHz]")
    ax.set_ylabel("S11 [dB]")

    plt.grid()
    # plt.show()

    return fig

@collection.plot_figure(only_build_this=False)
def sigmoidWeightedLosses():
    fig, ax = plt.subplots(1, 1, figsize=(5, 3))
    # plot sigmoid function 2*sigmoid(-x)+2
    x = np.linspace(-10,10,100)
    y_sigmoid2 = 2*(1/(1+np.exp(-x+5)))
    # plot normal sigmoid   
    y_sigmoid = 1/(1+np.exp(-x))
    plt.plot(x,y_sigmoid,linewidth=2,color="black")
    plt.plot(x,y_sigmoid2,linewidth=2,color="red")

    plt.grid()
    # make legend correct:
    plt.xlim(-5,10)
    plt.legend(["f(x)","2 $\cdot$ f(-x)"])
    # plt.legend("f(x)","2*f(-x)+2")
    
    plt.xlabel("x")
    plt.ylabel("y")
    # plt.show()
    return fig
