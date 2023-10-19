
from figurelib.figure import FigureCollection
import matplotlib.pyplot as plt
from figures.cst_loader import load_cst_filePOLAR, load_cst_file
import numpy as np

# Some example data to display

collection = FigureCollection("Introduction1")


@collection.table(header=["Col 1", "Col 2", "Col 3"], header_spec="l|l|l")
def test_table():
    header = ["Col 1", "Col 2", "Col 3"]
    data = []

    for _ in range(10):
        data_row = {col: np.random.randint(0, 99) for col in header}
        data.append(data_row)

    return data

@collection.plot_figure()
def SAR_test_dipole_S_param():
    fig, ax = plt.subplots(1, 1)
    runids = 6

    file_to_load = "Data/SAR_test_S_parameters.txt"

    data = load_cst_file(file_to_load, runids, 2)
    
    distance = ["d = 0 mm", "d = 3 mm","d = 30 mm","d = 50 mm","d = 80 mm","Ref"]
    for i in range(runids):
        ax.plot(np.transpose(data[i])[0], np.transpose(data[i])[1], label=f"{distance[i]}")

    ax.grid()
    plt.xlabel("Frequency [GHz]")
    plt.ylabel("S$_{1,1}$-Parameter [dB]")
    fig.legend()
    
    return fig


@collection.plot_figure(only_build_this=True)
def SAR_test_dipole_FFcuts():
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    runids = 4

    # Load the files
    file_to_load = "Data/SAR_test_dipole_FFcuts.txt"
    data = load_cst_filePOLAR(file_to_load,runids,8)

    # Convert the degress to radians
    for k in range(runids):
        for i in range(data.shape[1]):
            data[k][i][1] = data[k][i][1]/180*np.pi 

    # Plot the figures
    distance = ["d = 0 mm", "d = 10 mm","d = 80 mm","Ref"]
    for i in range(runids):
        ax.plot(np.transpose(data[i])[1], np.transpose(data[i])[2], label=f"{distance[i]}")

    ax.set_rlabel_position(-22.5)
    ax.grid(True)
    fig.legend()
    #plt.show()
    
    return fig

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np

    r = np.arange(0, 2, 0.01)
    theta = 2 * np.pi * r

    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(theta, r)
    ax.set_rmax(2)
    ax.set_rticks([0.5, 1, 1.5, 2])  # Less radial ticks
    ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
    ax.grid(True)

    ax.set_title("A line plot on a polar axis", va='bottom')
    plt.show()
