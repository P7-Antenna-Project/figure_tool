from figurelib.figure import FigureCollection
import matplotlib.pyplot as plt
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