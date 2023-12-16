import termcolor
from figurelib.figure import FigureContainer
import pathlib
import matplotlib.pyplot as plt
import itertools
import pathlib


class FigureBuilder:
    def __init__(self, figure_container: FigureContainer, draft_mode=False):
        self.figure_container = figure_container

        # Using draft style for faster rendering
        self.only_build_some = self._any_has_only_build_this() and draft_mode

        # Setting stylesheet for all figures
        plt.style.use("./figurelib/styles/eit6_publication.mplstyle")

    def _get_figure_build_txt(self, figure):
        figure_txt = f"{figure}"

        if self.only_build_some and not figure.only_build_this:
            figure_txt += termcolor.colored(" [SKIPPING]", "yellow")

        return figure_txt

    def _any_has_only_build_this(self):
        collections = self.figure_container.collections
        figure_lists = [col.figures for col in collections]
        figures = itertools.chain(*figure_lists)

        return any([fig.only_build_this for fig in figures])

    def build(self):
        figure_count = 0
        for collection in self.figure_container.collections:
            print(
                f"Building {termcolor.colored(len(collection), 'green')} figures in {termcolor.colored(collection, 'green')}:"
            )
            for figure in collection.figures:
                print("\t" + self._get_figure_build_txt(figure))

                if self.only_build_some and not figure.only_build_this:
                    # If only some figures should be built but this isn't one of them, skip to next figure
                    continue

                output_path = pathlib.Path("build", collection.name, f"{figure.name}")
                output_path.parent.mkdir(exist_ok=True, parents=True)

                try:
                    figure.build(output_path)
                    figure_count += 1
                except Exception as e:
                    print(
                        termcolor.colored(
                            f"Failed to build {collection}:{figure.name}. Error: {e}",
                            "red",
                        )
                    )

        print(f"Built {figure_count} figures.")