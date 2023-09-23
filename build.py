#!/usr/bin/env python
import argparse
import os
from figures.index import main_container
from figurelib.figure import FigureContainer
from figurelib.building import FigureBuilder
import shutil
from figurelib.custom_types import SimulationResults, SNRResults, EGCResults, SingleRunResults


def build_handler(args, container: FigureContainer):
    print("Building figure collections")

    builder = FigureBuilder(container, vars(args).get("draft", False))
    builder.build()


def clean_handler(args):
    print("Cleaning build directory.")

    if os.path.isdir('./build'):
        shutil.rmtree('./build')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog="Figure Generator",
        description="Description"
    )

    # Defining subcommands
    subparsers = parser.add_subparsers(help="sub-command help", dest="cmd")

    parser_clear = subparsers.add_parser("clean", help="clear -h")
    parser_build = subparsers.add_parser("build", help="build -h")

    # Adding options to subcommands
    parser_build.add_argument("-d", "--draft", help="builds the figures in draft mode, results in faster rendering", action="store_true")

    args = parser.parse_args()

    match args.cmd:
        case "clean":
            clean_handler(args)
        case "build":
            build_handler(args, main_container)
        case _:
            build_handler(args, main_container)
