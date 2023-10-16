from figurelib.figure import FigureContainer

from . import collection1
from . import 01Introduction


main_container = FigureContainer(
    [
        collection1.collection,
        01Introduction.collection,
    ]
)
