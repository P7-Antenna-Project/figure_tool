from figurelib.figure import FigureContainer

from . import Introduction1
from . import appendix_Antenna_design
from . import Technical03
from . import appendix_Simple_model
main_container = FigureContainer(
    [
        Introduction1.collection,
        Technical03.collection,
        appendix_Antenna_design.collection,
        appendix_Simple_model.collection,
    ]
)
