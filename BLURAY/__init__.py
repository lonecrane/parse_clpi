"""
A Python module containing a bunch of random functions that I have written over
the years.
"""

# Import standard modules ...
import sys

# Import sub-functions ...
from .parse_clpi_file import parse_clpi_file


# Ensure that this module is only imported by Python 3.x ...
if sys.version_info.major != 3:
    raise Exception("the Python module \"pyguymer3\" must only be used with Python 3.x, if you want a Python 2.x version then use \"pyguymer\" instead")
