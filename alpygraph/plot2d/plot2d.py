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
    def __init__(self, fsize=(10, 10)):
        fsize = tuple(dim/2.54 for dim in fsize) # cm --> inch
        self._fig, self._ax = plt.subplots(figsize=fsize)
        self.xlabel = 'xlabel'
        self.ylabel = 'ylabel'
        self.clabel = 'clabel'
        self.title  = ''
        self.xmode  = 'linear'
        self.ymode  = 'linear'

    def imshow(self, image, **kwargs):
        """ 2D plot
            Accept the same option keywords as plt.imshow

            Parameters:
            image (2D ndarray)
        """
        if not isinstance(image, np.ndarray):
            image = np.array(image)
        if len(image.shape) != 2:
            raise ValueError("\t=== image should be a 2D array ===")
        self._evalkwargs(kwargs)
        im  = plt.imshow(image, origin='lower', interpolation='none', aspect='auto', **kwargs)
        self._cb = self._colorbar(im)
    def hexabin(self, x, y, z=None, nbin=100, mincnt=1, bins=None, **kwargs):
        """ Make a 2D histogram with hexagonal pixels
            
            Parameters:
            x (ndarray)
            y (ndarray)
            z (ndarray)
            nbin (int): gridsize
            mincnt (float): minimal value plotted
            bins (str): 'log' or 'linear'
        """
        self._evalkwargs(kwargs)
        hbins = self.ax.hexbin(x, y, C=z, gridsize=nbin, mincnt=mincnt, bins=bins,
            xscale=self.xmode, yscale=self.ymode, edgecolor='none', **kwargs)
        self._ax.margins(0)
        self._cb = self._colorbar(hbins)

    # ================================================================= #
    # =========================== Finishing =========================== #
    def show(self):
        """ Show the 2D plot
        """
        self._labels()
        plt.show()
        return
    def save(self, name=None):
        self._labels()
        if name is None:
            name = 'myplot.pdf'
        name = os.path.abspath(name)   
        self._fig.savefig(name)
        # self._clear()
        print("\t=== Created {} ===".format(name))
        return

    # ================================================================= #
    # =========================== Internal ============================ #
    def _colorbar(self, mappable):
        """ Plot a colorbar next to the 2D plot
        """
        from mpl_toolkits.axes_grid1 import make_axes_locatable
        ax = mappable.axes
        fig = ax.figure
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size=0.15, pad=0.2)
        return fig.colorbar(mappable, cax=cax)
    def _labels(self):
        self._ax.set_title(r'{}'.format(self.title))
        self._ax.set_xlabel(r'{}'.format(self.xlabel))
        self._ax.set_ylabel(r'{}'.format(self.ylabel))
        if hasattr(self, '_cb'):
            self._cb.set_label(self.clabel)
        handles, labels = self._ax.get_legend_handles_labels()
        if len(labels) != 0:
            self._ax.legend()
        return
    def _evalkwargs(self, kwargs):
        for key, value in kwargs.items():
            if   key == 'xlabel': self.xlabel = value
            elif key == 'ylabel': self.ylabel = value
            elif key == 'clabel': self.clabel = value
            elif key == 'title':  self.title = value
            elif key == 'xmode':  self.xmode = value
            elif key == 'ymode':  self.ymode = value
            else:
                pass
        return
