import matplotlib.figure
import matplotlib.pyplot as plt
import io
import typing
import inspect
import pathlib
from jinja2 import Environment, FileSystemLoader
import re

# Jinja environment
def is_raw_latex(value):
    return isinstance(value, RawLatex)

env = Environment(
    block_start_string="\BLOCK{",
    block_end_string="}",
    variable_start_string="\VAR{",
    variable_end_string="}",
    trim_blocks=True,
    autoescape=False,
    loader=FileSystemLoader("./figurelib/templates"),
)

env.filters.update({
    "is_raw_latex": is_raw_latex
})

template = env.get_template("basic_table.tex")


class Table:
    def __init__(self, name, builder, header_spec, header_name, header, only_build_this):
        # Basic properties
        self.name = name
        self.header_spec = header_spec
        self.header_name = header_name
        self.header = header
        self.builder = builder

        # Build options
        self.only_build_this = only_build_this

    def _format_data(self, data: dict[str, typing.Any]):
        formatted_data = data

        return formatted_data

    def build(self, out_path: pathlib.Path):
        table_data = self.builder()
        formatted_data = self._format_data(table_data)

        # Add extension to output path
        out_path = out_path.with_suffix(".tex")

        with open(out_path, "w") as out_f:
            rendered_table = template.render(
                TABLE_HEADER_SPEC=self.header_spec,
                TABLE_HEADER_NAME=self.header_name,
                header=self.header,
                data=formatted_data,
            )
            out_f.write(rendered_table)

        return formatted_data

    def __str__(self) -> str:
        return self.name

class RawLatex:
    def __init__(self, latex_string) -> None:
        self.latex_string = latex_string

class Figure:
    def __init__(self, name, builder, width, height, subplots, only_build_this):
        # Basic properties
        self.name = name
        self.builder = builder

        # Build options
        self.width = width
        self.height = height
        self.subplots = subplots
        self.only_build_this = only_build_this

    def _apply_styles(self, figure: matplotlib.figure.Figure):
        fig_width, fig_height = self._get_figsize(self.width, self.height, self.subplots)
        figure.set_size_inches(fig_width, fig_height)
        figure.set_constrained_layout(True)

        return figure

    def build(self, out_path: pathlib.Path):
        fig = self.builder()
        styled_fig = self._apply_styles(fig)

        # Add extension to output path
        out_path = out_path.with_suffix(".pdf")

        buf = io.BytesIO()
        styled_fig.savefig(buf, format="pdf")
        buf.seek(0)
        out_path.write_bytes(buf.read())
        buf.close()

        plt.close(styled_fig)

        return styled_fig

    def _pt_to_in(self, pt):
        return pt * 1 / 72.27
    
    def _mm_to_in(self, mm):
        return mm * 1 / 25.4
    
    def _cm_to_in(self, cm):
        return cm * 1 / 2.54
    
    def _parse_dim_to_in(self, dim: str):
        dimension = re.search(r'^(\d+(?:\.\d*)?)\s*(mm|cm|pt|in)$', dim)

        if dimension is None:
            raise ValueError(f"Invalid dimension format: {dim}. The correct format is <float or int> <mm or cm or pt or int>.")
        
        try:
            value = float(dimension.group(1))
        except ValueError:
            raise ValueError(f"Invalid length specified: {dimension.group(1)}.")
        
        unit = dimension.group(2)            
        
        if unit == "mm":
            return self._mm_to_in(value)
        elif unit == "cm":
            return self._cm_to_in(value)
        elif unit == "pt":
            return self._pt_to_in(value)
        elif unit == "in":
            return value
        else:
            raise ValueError("Invalid unit specified. Valid units are mm, cm, pt and in.")

    def _get_figsize_base(self, base_width, subplots):
        golden_ratio = (5**0.5 - 1) / 2

        fig_width = base_width
        fig_height = fig_width * golden_ratio * (subplots[0] / subplots[1])

        return (fig_width, fig_height)
    
    def _get_figsize(self, width, height, subplots):
        # Determine base figure size
        if isinstance(width, float) or isinstance(width, int):
            # The default pagewidth of the report-class is 453pt
            base_width = width * self._pt_to_in(453)
        elif isinstance(width, str):
            base_width = self._parse_dim_to_in(width)
        else:
            raise ValueError("Invalid type for dimension, expected float, int or str.")
            
        fig_size = self._get_figsize_base(base_width, subplots)

        # Adjusting height
        if isinstance(height, float) or isinstance(height, int):
            # Keep same width, but scale the height by height-ratio
            fig_size = (fig_size[0], fig_size[1] * height)
        elif isinstance(height, str):
            # Keep same width, but overwrite the height by absolute length
            fig_size = (fig_size[0], self._parse_dim_to_in(height))
        else:
            raise ValueError("Invalid type for dimension, expected float, int or str.")
        
        return fig_size

    def __str__(self) -> str:
        return self.name


class FigureCollection:
    def __init__(self, name: str):
        self.name = name
        self.figures: list[Figure] = []

    def table(
        self,
        header: list[str] = [],
        header_spec: str = None,
        header_name: str = None,
        only_build_this: bool = False,
    ):
        """Declare that a function should be added to `FigureCollection` as a builder for a table.

        The builder function is expected to return a list of dictionaries, one for each row in the table.

        Parameters
        ----------
        only_build_this : boolean, optional
            if any figure has this set, only those with `only_build_this=True` will be built
        """

        if header_spec is None:
            header_spec = "c" * len(header)

        def wrapper(func):
            # Add table and the provided builder to the collection
            self.figures.append(
                Table(func.__name__, func, header_spec, header_name, header, only_build_this)
            )
            return func

        return wrapper

    def plot_figure(
        self,
        width: typing.Union[float, int, str] = 1.0,
        height: typing.Union[float, int, str] = 1.0,
        subplots: tuple[int, int] = (1, 1),
        only_build_this: bool = False,
    ):
        """Declare that a function should be added to `FigureCollection` as a builder.

        The builder function is expected to return a matplotlib `Figure`.
        The source of this figure/axes is very flexible; you can either
        construct them manually with `matplotlib.pyplot.subplots()` or
        use the figure/axes that are automatically injected into the builder
        arguments.

        Parameters
        ----------
        width : float, optional
            the width of the figure as a fraction of textwidth, by default 1.0
        subplots : tuple of (int, int), optional
            the number of rows and columns of subplots, see `matplotlib.pyplot.subplots`, by default (1,1)
        only_build_this : boolean, optional
            if any figure has this set, only those with `only_build_this=True` will be built

        Example
        -------
        Automatic figure/axes injection

        ```
        @my_collection.plot_figure(subplots=(1, 3))
        def my_figure(fig, ax):
            ax1, ax2, ax3 = ax
            ...
        ```
        """

        def outer(func):
            func_args = inspect.getfullargspec(func).args

            def inner_injector(*args, **kwargs):
                if "fig" in func_args and "ax" in func_args:
                    nrows, ncols = subplots
                    fig, ax = plt.subplots(nrows, ncols)

                    kwargs["fig"] = fig
                    kwargs["ax"] = ax

                return func(*args, **kwargs)

            # Add figure and the provided builder the the collection
            self.figures.append(
                Figure(func.__name__, inner_injector, width, height, subplots, only_build_this)
            )
            return inner_injector

        return outer

    def __len__(self):
        return len(self.figures)

    def __str__(self):
        return self.name


class FigureContainer:
    def __init__(self, collections: list[FigureCollection]):
        self.collections = collections
