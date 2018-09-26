#! /usr/bin/python3.5
# -*- coding: utf-8 -*-

"""
Class to make 2D graphs
"""

import os
import sys
import numpy as np
import matplotlib.pylab as plt


__author__ = 'Alan Loh'
__copyright__ = 'Copyright 2018, alpygraph'
__credits__ = ['Alan Loh']
__license__ = 'MIT'
__version__ = '0.0.1'
__maintainer__ = 'Alan Loh'
__email__ = 'alan.loh@obspm.fr'
__status__ = 'WIP'
__all__ = ['Plot2D']


class Plot2D():
    def __init__(self):
        self.fig, self.ax = plt.subplots()

    def imshow(self, image):
        """ 2D plot
        """
        im  = plt.imshow(image, origin='lower', interpolation='none')
        self._colorbar(im)

    def show(self):
        """ Show the 2D plot
        """
        plt.show()
        return

    def _colorbar(self, mappable):
        """ Plot a colorbar next to the 2D plot
        """
        from mpl_toolkits.axes_grid1 import make_axes_locatable
        ax = mappable.axes
        fig = ax.figure
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size=0.15, pad=0.2)
        return fig.colorbar(mappable, cax=cax)
    