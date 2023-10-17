from figurelib.figure import FigureCollection
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


collection = FigureCollection("Antenna_design")

@collection.plot_figure(only_build_this=False)
def MIFA_s11():
    data = np.loadtxt(open('Data\MIFA_s11_data.txt'), delimiter='\t', skiprows=1, unpack=True)
    fig, ax = plt.subplots()    
    ax.plot(data[0], data[1])    
    plt.xlabel('Frequency [MHz]')
    plt.ylabel('S11 [dB]')
    plt.title('S11 of MIFA antenna')
    plt.grid()
    return fig
