"""
A simple module within the test package
"""

class SimpleBase():
    r"""A simple base class that doesn't do too much

    Parameters
    ----------
    info : str
        The information about the class

    Notes
    -----
    Here's some math

    .. math::
        x = \nabla \cdot \vec{y}
    """
    def __init__(self, info):
        self._info = info

    @property
    def info(self):
        """The information.

        Returns
        -------
        str
        """
        return self._info

    def write(self):
        """Prints the information to the screen.
        """
        print(self.info)


class ExtraSimple(SimpleBase):
    def write(self):
        print("A little extra special", self.info)

def do_something(x, y, z):
    """Add x, y, and z.

    Parameters
    ----------
    x, y, z : float or array_like

    Returns
    -------
    float or array_like
    """

    return x + y + z