"""
Do some simple stuff
====================

Do some simple plotting using some of the test functions
"""
#########################################################################
# Import modules
# --------------
#

import numpy as np
import matplotlib.pyplot as plt
from test_package import SimpleBase, ExtraSimple, do_something

# sphinx_gallery_thumbnail_number = 3


#############################################
# Using the simple classes
# ------------------------
#
# Create the simple classes
#

simp1 = SimpleBase('This info')
simp1.write()

# Create the extra simple class

simp2 = ExtraSimple("Other info")
simp2.write()

#########################
# Plot
# ----
#
# Do some plotting

x = np.linspace(0, 10)
y = 0.1*np.random.rand(*x.shape)
z = x**2

out = do_something(x, y, z)

plt.plot(x, out)


#######################
# Plotly plotting
# ---------------
#
# Do some plotting with plotly

import plotly as ply

ply.sc