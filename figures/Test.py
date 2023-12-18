from figurelib.figure import FigureCollection
import matplotlib.pyplot as plt
from figures.cst_loader import load_cst_filePOLAR, load_cst_file, load_cst_filePOLARwhenASCIIExport
import numpy as np
import pickle
from matplotlib.ticker import FuncFormatter

collection = FigureCollection("Test")

@collection.plot_figure(only_build_this=True)
def plot_centre_frequency():
    # Load data
    FC = np.load("Data/Test_data/Wire_testing_inverse2_pred_FC.npy")
    straight_frequency = np.linspace(1000, 2500, 31, endpoint=True)

    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # Upper bound
    ax.plot(straight_frequency, straight_frequency+0.05*straight_frequency, color = "g", linestyle = "--")
    # Lower bound
    ax.plot(straight_frequency, straight_frequency-0.05*straight_frequency, color = "g", linestyle = "--", label = r"5% error bound")
    # Centre frequency
    ax.plot(straight_frequency, FC[:31], "o",color = "b", label= "BW: 50" , markersize=4)
    ax.plot(straight_frequency, FC[31:],'o' , color = "r", label = "BW: 100", markersize=4)
    ax.set_xlabel("Centre frequency [MHz]")
    ax.set_ylabel("Achieved centre frequency [MHz]")
    plt.grid(True)
    plt.legend()
    # plt.show()

    return fig

@collection.plot_figure(only_build_this=True)
def bandwidth_and_centre_frequency():
    # Load data
    tested_FC = np.linspace(100, 2500, 31, endpoint=True)
    BW_achieved = np.load("Data/Test_data/Wire_testing_inverse2_pred_BW.npy")
    
    fig, axs = plt.subplots(2)
    # BW: 50
    axs[0].axhline(50, color='b', linestyle='--', label="50 MHz bandwidth")
    axs[0].plot(tested_FC, BW_achieved[:31], 'o', label="Achieved bandwidth", color='b', markersize=4)
    axs[0].grid(True)
    axs[0].legend()

    # BW: 100
    axs[1].axhline(100, color='r', linestyle='--', label="100 MHz bandwidth")
    axs[1].plot(tested_FC, BW_achieved[31:], 'o', label="Achieved bandwidth", color='r', markersize=4)
    axs[1].grid(True)
    axs[1].legend()

    # plt.show()

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
    ax[0].set_xlabel("Centre frequency [MHz]")
    ax[0].set_ylabel("Bandwidth [MHz]")
    ax[1].set_xlabel("Centre frequency [MHz]")
    ax[1].set_ylabel("Bandwidth [MHz]")

    return fig