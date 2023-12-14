from figurelib.figure import FigureCollection
import matplotlib.pyplot as plt
from figures.cst_loader import load_cst_filePOLAR, load_cst_file, load_cst_filePOLARwhenASCIIExport
import numpy as np
import pickle
from matplotlib.ticker import FuncFormatter

collection = FigureCollection("04Technical")

@collection.plot_figure(only_build_this=False)
def cuts_in_3d_theta():
    fig = plt.figure(figsize=plt.figaspect(0.5))
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    # Define the look
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_title("")

    # Define the data Cut 1
    x = np.sin(np.linspace(0,2*np.pi,100))
    y = np.zeros(100)
    z = np.cos(np.linspace(0,2*np.pi,100))

    d = ax.plot(x,y,z, label="$\\theta=0^\circ$")

    #print(d[0].get_color())

    # Define the data Cut 2
    x = -0.6*np.cos(np.linspace(0,2*np.pi,100))-0.37*np.sin(np.linspace(0,2*np.pi,100))
    y = 0.6*np.cos(np.linspace(0,2*np.pi,100))+0.37*np.sin(np.linspace(0,2*np.pi,100))
    z = 0.52*np.cos(np.linspace(0,2*np.pi,100))-0.85*np.sin(np.linspace(0,2*np.pi,100))

    d = ax.plot(x,y,z, label="$\\theta=45^\circ$")

    #print(d[0].get_color())

    # Define the data Cut 3
    x = np.zeros(100)
    y = -np.sin(np.linspace(0,2*np.pi,100))
    z = -np.cos(np.linspace(0,2*np.pi,100))

    d = ax.plot(x,y,z, label="$\\theta=90^\circ$")
    #print(d[0].get_color())


    # Define the data Cut 4
    x = -0.71*np.sin(np.linspace(0,2*np.pi,100))
    y = -0.71*np.sin(np.linspace(0,2*np.pi,100))
    z = np.cos(np.linspace(0,2*np.pi,100))

    d = ax.plot(x,y,z, label="$\\theta=135^\circ$")
    #print(d[0].get_color())

    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

    ax.view_init(25, 45)

    return fig

@collection.plot_figure(only_build_this=False)
def cuts_in_3d_phi():
    fig = plt.figure(figsize=plt.figaspect(0.5))
    ax2 =fig.add_subplot(1, 1, 1, projection='3d')

    ax2.set_xlabel("x")
    ax2.set_ylabel("y")
    ax2.set_zlabel("z")

    # Define the data Cut 1 in phi
    y = np.sin(np.linspace(0,2*np.pi,100))
    z = np.zeros(100)
    x = np.cos(np.linspace(0,2*np.pi,100))

    ax2.plot(x,y,z, label="$\\phi=0^\circ$")

    # Define the data cut 2 in phi
    y = -0.6*np.cos(np.linspace(0,2*np.pi,100))-0.37*np.sin(np.linspace(0,2*np.pi,100))
    z = 0.6*np.cos(np.linspace(0,2*np.pi,100))+0.37*np.sin(np.linspace(0,2*np.pi,100))
    x = 0.52*np.cos(np.linspace(0,2*np.pi,100))-0.85*np.sin(np.linspace(0,2*np.pi,100))

    ax2.plot(x,y,z, label="$\\phi=45^\circ$")

    # Define the data cut 3 in phi
    y=  np.zeros(100)
    z = -np.sin(np.linspace(0,2*np.pi,100))
    x = -np.cos(np.linspace(0,2*np.pi,100))

    ax2.plot(x,y,z, label="$\\phi=90^\circ$")

    # Define the data cut 4 in phi
    y = -0.71*np.sin(np.linspace(0,2*np.pi,100))
    z = -0.71*np.sin(np.linspace(0,2*np.pi,100))
    x = np.cos(np.linspace(0,2*np.pi,100))

    ax2.plot(x,y,z, label="$\phi=135^\circ$")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

    ax2.view_init(25, 45)

    return fig
    