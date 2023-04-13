"""
========================================================
Utility Classes and Functions (:mod:`test_package`)
========================================================
.. currentmodule:: test_package

The ``utils`` package contains utilities for helping with common operations involving
discrete meshes

Classes
=======
.. autosummary::
  :toctree: generated/

  SimpleBase
  ExtraSimple

Functions
=========

Simple Utilities
--------------
.. autosummary::
  :toctree: generated/

  do_something
"""
from importlib.metadata import version, PackageNotFoundError
from .simple import SimpleBase, ExtraSimple, do_something

try:
    __version__ = version("test-package")
except PackageNotFoundError:
    # package is not installed
    pass