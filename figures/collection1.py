from figurelib.figure import FigureCollection
import matplotlib.pyplot as plt
import numpy as np

# Some example data to display
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x**2)

collection = FigureCollection("collection1")


@collection.plot_figure(subplots=(1, 3))
def figure1():
    fig, ax = plt.subplots(1, 3)
    ax[0].plot(x, y)
    ax[0].set_title("A single plot")

    ax[1].plot(x, y)
    ax[1].set_title("A second plot")

    ax[2].plot(x, y)
    ax[2].set_title("A third plot")

    fig.set_constrained_layout(True)

    return fig


# A second way of achieving the same thing as in figure1 by using figure injection
@collection.plot_figure(subplots=(1, 3))
def figure2(fig, ax):
    ax0, ax1, ax2 = ax
    ax0.plot(x, y)
    ax0.set_title("A single plot")

    ax1.plot(x, y)
    ax1.set_title("A second plot")

    ax2.plot(x, y)
    ax2.set_title("A third plot")

    fig.set_constrained_layout(True)

    return fig


@collection.table(header=["Col 1", "Col 2", "Col 3"], header_spec="l|l|l")
def test_table():
    header = ["Col 1", "Col 2", "Col 3"]
    data = []

    for _ in range(10):
        data_row = {col: np.random.randint(0, 99) for col in header}
        data.append(data_row)

    return data

