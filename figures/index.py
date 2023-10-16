from figurelib.figure import FigureContainer

from . import collection1
from . import Introduction1


main_container = FigureContainer(
    [
        collection1.collection,
        Introduction1.collection,
    ]
)
