from figurelib.figure import FigureCollection
import matplotlib.pyplot as plt
from figures.cst_loader import load_cst_filePOLAR, load_cst_file, load_cst_filePOLARwhenASCIIExport
import numpy as np
import pickle
from matplotlib.ticker import FuncFormatter

collection = FigureCollection("Test")

@collection.plot_figure(only_build_this=False)
def plot_centre_frequency():
    # Load data
    # data = np.load("data/centre_frequency.npy")
    straight_frequency = np.linspace(1000,2500,1500)

    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # Upper bound
    ax.plot(straight_frequency, straight_frequency+0.05*straight_frequency, color = "r", linestyle = "--")
    # Lower bound
    ax.plot(straight_frequency, straight_frequency-0.05*straight_frequency, color = "r", linestyle = "--")




    return fig

@collection.plot_figure(only_build_this=False)
def bandwidth_and_centre_frequency():
    # Load data
    # data = np.load("data/BW_freq.npy")
    BW_fifty = np.ones(1500)*50
    BW_hundred = np.ones(1500)*100

    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # Fifty bandwidth line
    ax.plot(BW_fifty, linestyle = "--", label = "50 MHz bandwidth")
    # Lower bound
    ax.plot(BW_hundred, linestyle = "--", label = "100 MHz bandwidth")



    #plt.show()

    return fig

@collection.plot_figure(only_build_this=True)
def bandwidth_and_centre_frequency_investigation():
    # Load data
    fig, ax = plt.subplots(1,2)

    with open("Data/BW_CS_CST/MIFA_real_cst_BW_center.pkl", "rb") as f:
        mifa_data = pickle.load(f)
    
    #print(mifa_data.keys())

    ax[0].scatter(mifa_data["centre_frequency"],mifa_data["bandwidth"] , label = "MIFA", s=1)
    ax[0].set_title("MIFA")
    with open("Data/BW_CS_CST/WIRE_real_cst_BW_center.pkl", "rb") as f:
        wire_data = pickle.load(f)

    ax[1].scatter(wire_data["centre_frequency"],wire_data["bandwidth"] , label = "WIRE", s=1)
    ax[1].set_title("WIRE")

    return fig