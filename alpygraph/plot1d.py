#! /usr/bin/python3.5
# -*- coding: utf-8 -*-

"""
Class to make 1D graphs
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
__all__ = ['Plot1D']


class Plot1D():
    def __init__(self, fsize=(10, 10)):
        fsize = tuple(dim/2.54 for dim in fsize) # cm --> inch
        self._fig, self._ax = plt.subplots(figsize=fsize)
        self.xlabel = 'xlabel'
        self.ylabel = 'ylabel'
        self.title  = ''
        self.xmode  = 'linear'
        self.ymode  = 'linear'

    def plot(self, x, y, label=None, **kwargs):
        """ Regular plot, accept all pylab.plot keywords

            Parameters:
            x (ndarray)
            y (ndarray)
            label (str): legend
        """
        self._evalkwargs(kwargs)
        self._axesmode()
        self._ax.plot(x, y, label=label, **kwargs)
        self._updatelimits(x, y)
        return

    def errorbar(self, x, y, xerr=None, yerr=None, label=None, **kwargs):
        """ Regular error plot, accept all pylab.errorplot keywords

            Parameters:
            x (ndarray)
            y (ndarray)
            xerr (ndarray): x errors
            yerr (ndarray): y errors
            label (str): legend
        """
        self._evalKwargs(kwargs)
        self._axesmode()
        self._ax.errorbar(x, y, xerr=xerr, yerr=yerr, linestyle='', marker='o', label=label)
        self._updatelimits(x, y)
        return

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
        print("\t=== Created {} ===".format(name))
        return

    # ================================================================= #
    # =========================== Internal ============================ #
    def _updatelimits(self, x, y, offset=True):
        """ 
            Parameters:
            x (ndarray)
            y (ndarray) 
            offset (bool): add a 10 per cent offset in x and y directions
        """
        if offset:
            dx = max(x) - min(x)
            dy = max(y) - min(y)
            xmin, xmax = (min(x) - 0.1*dx, max(x) + 0.1*dx)
            ymin, ymax = (min(y) - 0.1*dy, max(y) + 0.1*dy)
        else:
            xmin, xmax = min(x), max(x)
            ymin, ymax = min(y), max(y)
        if hasattr(self, '_xmin'): self._xmin = min(self._xmin, xmin)
        else: self._xmin = xmin
        if hasattr(self, '_xmax'): self._xmax = max(self._xmax, xmax)
        else: self._xmax = xmax
        if hasattr(self, '_ymin'): self._ymin = min(self._ymin, ymin)
        else: self._ymin = ymin
        if hasattr(self, '_ymax'): self._ymax = max(self._ymax, ymax)
        else: self._ymax = ymax
        if hasattr(self, 'xmin'): self._xmin = self.xmin
        if hasattr(self, 'xmax'): self._xmax = self.xmax
        if hasattr(self, 'ymin'): self._ymin = self.ymin
        if hasattr(self, 'ymax'): self._ymax = self.ymax
        self._ax.set_xlim(self._xmin, self._xmax)
        self._ax.set_ylim(self._ymin, self._ymax)
        return
    
    def _axesmode(self):
        if self.ymode.lower() == 'log':
            self._ax.set_yscale('log', nonposx='clip')
        else:
            self._ax.set_yscale('linear')
        if self.xmode.lower() == 'log':
            self._ax.set_xscale('log', nonposx='clip')   
        else:
             self._ax.set_xscale('linear')
        return
    
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
            elif key == 'title':  self.title  = value
            elif key == 'xmode':  self.xmode  = value
            elif key == 'ymode':  self.ymode  = value
            elif key == 'xmin':   self.xmin   = value
            elif key == 'xmax':   self.xmax   = value
            elif key == 'ymin':   self.ymin   = value
            elif key == 'ymax':   self.ymax   = value
            else:
                pass
        return




