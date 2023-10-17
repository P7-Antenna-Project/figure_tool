from figurelib.figure import FigureContainer

from . import Introduction1
from . import appendix_Antenna_design

main_container = FigureContainer(
    [
        Introduction1.collection,
        appendix_Antenna_design.collection,
    ]
)
