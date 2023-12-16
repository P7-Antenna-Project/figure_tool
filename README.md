# EIT6 Figure Tool
[![build figures](https://github.com/EIT6-Beacon/figure_tool/actions/workflows/build.yml/badge.svg)](https://github.com/EIT6-Beacon/figure_tool/actions/workflows/build.yml)

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

this will rebuild all the figures in publication quality. If instead you want a faster build, you can use draft mode. This will only build those figures initialized with `@collection.plot_figure(..., only_build_this=True)`. Keep in mind that if no figure has this flag set, draft mode is completely equivalent to the standard build mode, and all figures will be built.

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
@collection.plot_figure(only_build_this=True)
def figure1(fig, ax):
    # Some example data to display
    x = np.linspace(0, 2 * np.pi, 400)
    y = np.sin(x**2)

    ax.plot(x, y)
    ax.set_title("A single plot")

    return fig
```

### Scaling figures
By default, the width of a figure is equal to the width of an A4 page with 2.54 cm margins (453pt). The height is automatically calculated such that the ratio between the width and height is the golden ratio. The default settings, equivalent to omitting both the `height` and `width` settings are
```python
@collection.plot_figure(width=1.0, height=1.0)
def figure1(fig, ax):
```

There are a couple options when you want to scale a figure. Both `width` and `height` can be specified as a float, in which case the size is relative to the default size. Note that the `height` scaling is always applied _after_ the figure height has been calculated to conform to the golden ratio, i.e. when `height=1.0` the ratio between the width and the height is the golden ratio.

For example, setting the width of a figure to half of a standard page (omitting the height setting, such that it is automatically calculated)
```python
@collection.plot_figure(width=0.5)
def figure1(fig, ax):
```

Setting the width of a figure to half of a standard page, and cutting the height in half
```python
@collection.plot_figure(width=0.5, height=0.5)
def figure1(fig, ax):
```

If the relative sizing and the automatic calculation are prohibitive to what you're trying to achieve, both dimensions can be specified absolutely in a string. The supported units are `mm`, `cm`, `pt` and `in`:
```python
@collection.plot_figure(width="3cm", height="30mm")
def figure1(fig, ax):
```


