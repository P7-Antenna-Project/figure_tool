from figurelib.figure import FigureCollection
import matplotlib.pyplot as plt
from figures.cst_loader import load_cst_filePOLAR, load_cst_file, load_cst_filePOLARwhenASCIIExport
import numpy as np
import pickle
from matplotlib.ticker import FuncFormatter

collection = FigureCollection("Appendix_para")

@collection.plot_figure(only_build_this=False)
def forward_model_loss():
    fig, ax = plt.subplots(1,2)

    # Load the data
    data = np.load("Data/forward_model_parametric_loss.npy")
    # Plot the data
    ax[0].set_title("Error")
    ax[0].plot(data[0])
    ax[1].set_title("Mean squared error")
    ax[1].plot(data[1])

    return fig

@collection.plot_figure(only_build_this=False)
def inverse_model_loss():
    fig, ax = plt.subplots(1,2)

    # Load the data
    data = np.load("Data/inverse_model_parametric_loss.npy")
    # Plot the data
    ax[0].set_title("Error")
    ax[0].plot(data[0])
    ax[1].set_title("Mean squared error")
    ax[1].plot(data[1])

    return fig

@collection.plot_figure(only_build_this=False)
def inverse_model_predict():

    data = np.load("Data\inverse_model_parametric_predict.npy")
    fig = plt.figure(figsize=(15, 15))
    #fig.set_figheight(20)
    # Plot the data
    width = 0.1
    labels = ["Wire length", "Wire height", "Wire thickness"]
    for i in range(6):
        plt.subplot(3, 2, i+1)
        plt.grid(True)
        #maximum = np.max([data[0][i][0], data[1][i][0]]),np.max([data[1][i][1], data[0][i][1]]),np.max([data[1][i][2], data[0][i][2]])
        
        data[0][i] = data[0][i]/data[1][i]
        data[1][i] = data[1][i]/data[1][i] 
        
        bars1 = plt.bar(np.arange(1,4) - width/2, data[0][i], width)
        bars2 = plt.bar(np.arange(1,4) + width/2, data[1][i], width)
        plt.xticks(np.arange(1,4), labels)
        if i == 1:
            plt.legend([bars1, bars2], ['Pred', 'Test'])

    
    return fig
