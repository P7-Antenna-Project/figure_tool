# EIT7 Figure Tool
[![build figures](https://github.com/P7-Antenna-Project/figure_tool/actions/workflows/build.yml/badge.svg)](https://github.com/P7-Antenna-Project/figure_tool/actions/workflows/build.yml)

This tools assists in creating consistent matplotlib figures with version-control. 

## Overview

Figures are organized into several substructures:

1. The highest level is the `FigureContainer`.
2. The `FigureContainer` consists of several `FigureCollection`s.
3. Each `FigureCollection` contains different subclasses of `Figure`.

The top-level `FigureContainer` defines global styling and handles top-level building. All child `Figure`s inherit the styles from the parent container, unless specifically overwritten in the figure-definition. Each instance of `FigureCollection` corresponds to a single folder in the final build. Each instance of `Figure` corresponds to a single diagram.

The default export format for figures is pdf.

## Running a build

You can run a build locally by running the following script in a terminal

```bash
python build.py
```

this will rebuild all the figures in publication quality. If instead you want a faster build, you can use draft mode. Keep in mind this might cause significant artifacts in the figures.

```bash
python build.py build -d
```

Alternatively, whenever you push to `main` a GitHub action will automatically build the figures and push them to Overleaf.


## Defining figures

If an appropriate `FigureCollection` doesn't already exist, you'll have to define one and register it in the collection index, `figures/index.py`.

```python
from figurelib.figure import FigureCollection

collection = FigureCollection("my_collection")
```

at which point you can start registering figure-builder functions in the collection

```python
import matplotlib.pyplot as plt
import numpy as np


@collection.plot_figure()
def figure1():
    # Some example data to display
    x = np.linspace(0, 2 * np.pi, 400)
    y = np.sin(x**2)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title("A single plot")

    return fig
```

An alternative syntax is

```python
@collection.plot_figure(only_build = True)
def figure1(fig, ax):
    # Some example data to display
    x = np.linspace(0, 2 * np.pi, 400)
    y = np.sin(x**2)

    ax.plot(x, y)
    ax.set_title("A single plot")

    return fig
```
