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

    #print(data.keys())
    #print(data["S1,1"].shape)

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

@collection.plot_figure(only_build_this=False,width=.75, height=.75)
def sigmoidWeightedLosses():
    fig, ax = plt.subplots(1, 1, figsize=(5, 3))
    # plot sigmoid function 2*sigmoid(-x)+2
    x = np.linspace(-10,10,100)
    y_sigmoid2 = 2*(1/(1+np.exp(-x)))
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

@collection.plot_figure(only_build_this=False,width=1, height=.75)
def arbitraryS11Curve_discussion():
    # Define the parameters
   # Define the parameters
    f_start = 1000  # Start frequency in MHz
    f_stop = 2500  # Stop frequency in MHz
    f_center = 1900  # Center frequency in MHz
    bw = 100  # Bandwidth in MHz
    points = 1001  # Number of points
    s11_min = -30  # Minimum S11 in dB

    # Generate the frequency array
    frequencies = np.linspace(f_start, f_stop, points)

    # Generate the S11 values
    s11 = s11_min * np.exp(-((frequencies - f_center) / bw) ** 2)

    # Plot the S11 curve
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(frequencies, s11,linewidth = 2)
    # ax.set_title('S11 Curve')
    ax.set_xlabel('Frequency (MHz)')
    ax.set_ylabel('S11 (dB)')
    ax.set_xlim(f_start, f_stop)
    ax.grid(True)
    
    return fig


@collection.plot_figure(only_build_this=False,width=.75, height=.75)
def costFunctionExample():
    x1 = np.linspace(0, 8, 100)
    x2 = np.linspace(8, 10, 100)
    x3 = np.linspace(10, 14, 100)
    x4 = np.linspace(14, 20, 100)

    # Define the y values for each segment
    y1 = np.ones_like(x1)
    y2 = 6 * (np.exp((x2 - x2[0])) - 1) / (np.exp(2) - 1) + 1  # Faster exponential increase, max value of 7

    # Make sure y3 starts where y2 ends and ends at 2
    start_y3 = y2[-1]
    end_y3 = 2
    rate_y3 = (start_y3 - end_y3) / (x3[-1] - x3[0])
    y3 = start_y3 - rate_y3 * (x3 - x3[0])  # Exponential decrease

    # Make sure y4 starts where y3 ends
    start_y4 = y3[-1]
    y4 = start_y4 * np.ones_like(x4)

    # Concatenate the x and y values
    x = np.concatenate((x1, x2, x3, x4))
    y = np.concatenate((y1, y2, y3, y4))
    fig, ax = plt.subplots(figsize=(8, 4))
    
    # Plot the curve
    ax.plot(x, y,linewidth = 2)
    # ax.set_title('Cost Function')
    ax.set_xlabel('S1,1 [dB]')
    ax.set_ylabel('Error weight')
    ax.set_xlim(0, 17)
    ax.set_ylim(0, 8)
    ax.grid(True)
    return fig

    
    
@collection.plot_figure(only_build_this=False)
def wire_verification_plot():
   # load .txt file:
    skiprows = 2
    data = np.loadtxt("Data/wire_verification.txt", skiprows=skiprows)
    
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(data[:,0],data[:,1],linewidth = 2)
    # ax.set_title('S11 Curve')
    ax.set_xlabel('Frequency [MHz]')
    ax.set_ylabel('S11 [dB]')

    ax.plot(1900*np.ones_like([-10]), [-15.34], marker='o', markersize=5, color="black")
    ax.plot((1846)*np.ones_like([-10]), [-10], marker='o', markersize=5, color="black")
    ax.plot((1959)*np.ones_like([-10]), [-10], marker='o', markersize=5, color="black")
    #add text to the markers:
    ax.text(1900, -16.7, "1900 MHz",horizontalalignment='center',verticalalignment='bottom')
    ax.text(1900-100, -10, "1846 MHz",horizontalalignment='right',verticalalignment='bottom')
    ax.text(1900+350, -10, "1959 MHz",horizontalalignment='right',verticalalignment='bottom')
    ax.set_xlim(500,3000)
    ax.set_ylim(-20,0)    
    ax.grid(True)
    # plt.show()
    return fig

@collection.plot_figure(only_build_this=False)
def MIFA_verification_plot():
   # load .txt file:
    skiprows = 2
    data = np.loadtxt("Data/MIFA_verification.txt", skiprows=skiprows)
    
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(data[:,0],data[:,1],linewidth = 2)
    # ax.set_title('S11 Curve')
    ax.set_xlabel('Frequency [MHz]')
    ax.set_ylabel('S11 [dB]')

    ax.plot(2412*np.ones_like([-10]), [-20.09], marker='o', markersize=5, color="black")
    ax.plot((2345)*np.ones_like([-10]), [-10], marker='o', markersize=5, color="black")
    ax.plot((2489)*np.ones_like([-10]), [-10], marker='o', markersize=5, color="black")
    #add text to the markers:
    ax.text(2412, -22, "2412 MHz",horizontalalignment='center',verticalalignment='bottom')
    ax.text(2345-100, -10, "2345 MHz",horizontalalignment='right',verticalalignment='bottom')
    ax.text(2489+350, -10, "2489 MHz",horizontalalignment='right',verticalalignment='bottom')
    ax.set_xlim(500,3000)
    ax.set_ylim(-25,0)    
    ax.grid(True)
    # plt.show()
    return fig