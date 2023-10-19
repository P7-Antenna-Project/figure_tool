from figurelib.figure import FigureCollection
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from figures.cst_loader import load_cst_filePOLAR, load_cst_file



collection = FigureCollection("Antenna_design")

@collection.plot_figure()
def MIFA_s11():
    data = np.loadtxt(open('Data/MIFA_s11_data.txt'), delimiter='\t', skiprows=1, unpack=True)
    fig, ax = plt.subplots()    
    ax.plot(data[0], data[1])    
    plt.xlabel('Frequency [MHz]')
    plt.ylabel('S11 [dB]')
    plt.title('S11 of MIFA antenna')
    plt.grid()
    return fig


@collection.plot_figure()
def MIFA_sweep_s11():
    runs = 13
    data = load_cst_file("Data/MIFA_sweep_data.txt",runs,2)
    
    fig, ax = plt.subplots()
    line_length = np.linspace(4,10,13,endpoint=True)
    
    
    for i in range(runs):
        ax.plot(np.transpose(data[i])[0], np.transpose(data[i])[1], label=f"{line_length[i]} mm")

    ax.grid()
    plt.xticks(np.linspace(500,5000,10,endpoint=True))
    plt.xlabel("Frequency [MHz]")
    plt.ylabel("S$_{1,1}$-Parameter [dB]")
    fig.legend()
    plt.show()
    
    return fig

