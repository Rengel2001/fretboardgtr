from dataclasses import dataclass

from fretboardgtr.constants import INTERVAL_MAPPING, WHITE

TEXT_OFFSET = "0.3em"
TEXT_STYLE = "text-anchor:middle"
from fretboardgtr.base import ConfigIniter


@dataclass
class NoteColors(ConfigIniter):
    """Dataclass containing the mapping of colors and intervals."""

    root: str = "rgb(255, 0, 0)"          # Red
    second: str = "rgb(255, 165, 0)"      # Orange
    third: str = "rgb(255, 255, 0)"       # Yellow
    fourth: str = "rgb(0, 255, 0)"        # Green
    fifth: str = "rgb(0, 128, 255)"       # Bright Blue 
    sixth: str = "rgb(135, 206, 235)"     # Light Blue
    seventh: str = "rgb(128, 0, 128)"     # Deep Purple 
    eighth: str = "rgb(221, 160, 221)"    # Light Pink-Purple
    ninth: str = "rgb(255, 20, 147)"      # Deep Neon Pink
    tenth: str = "rgb(210, 105, 30)"      # Light Brown
    eleventh: str = "rgb(192, 192, 192)"  # Light Gray
    twelfth: str = "rgb(50, 255, 127)"    # Bright Aqua Green

    def from_short_interval(self, interval: str) -> str:
        """Get color for the given short interval.

        Parameters
        ----------
        interval : str
            String representing the interval

        Returns
        -------
        str
            RGB color as string

        Example
        -------
        from fretboardgtr.constants import Interval
        >>> NoteColors().from_short_interval(Interval.MINOR_SIXTH)
        "rgb(168, 107, 98)"
        """
        color = WHITE
        for long, short in INTERVAL_MAPPING.items():
            if interval != short:
                continue
            if hasattr(self, long):
                color = getattr(self, long)
        return color

    def from_interval(self, interval: int) -> str:
        """Get color for the given long interval name.

        Parameters
        ----------
        interval : str
            String representing the long interval

        Returns
        -------
        str
            RGB color as string

        Example
        -------
        from fretboardgtr.constants import LongInterval
        >>> NoteColors().from_short_interval(LongInterval.MINOR_SIXTH)
        "rgb(168, 107, 98)"
        """
        cls_keys = list(self.__annotations__)
        color = getattr(self, cls_keys[interval % 12])
        return color
