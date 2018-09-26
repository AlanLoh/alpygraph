#! /usr/bin/python3.5
# -*- coding: utf-8 -*-

"""
Class to plot beautiful Dynamic Spectra
These are intended to be suited for radio astronomy purposes
"""

import os
import sys
import numpy as np

from astropy.time import Time

from ..plot2d import Plot2D 

__author__ = 'Alan Loh'
__copyright__ = 'Copyright 2018, alpygraph'
__credits__ = ['Alan Loh']
__license__ = 'MIT'
__version__ = '0.0.1'
__maintainer__ = 'Alan Loh'
__email__ = 'alan.loh@obspm.fr'
__status__ = 'WIP'
__all__ = ['DynSpec']


class DynSpec():

    def __init__(self, dynspec=None, time=None, frequency=None):
        self.dynspec = dynspec
        self.time = time
        self.frequency = frequency

    # ================================================================= #
    # ======================== Getter / Setter ======================== #
    @property
    def dynspec(self):
        """ Dynamic Spectrum, 2D array (frequency, time)
        """
        return self._dynspec
    @dynspec.setter
    def dynspec(self, ds):
        if ds is None:
            return
        if not isinstance(ds, np.ndarray):
            ds = np.array(ds)
        if len(ds.shape) != 2:
            raise ValueError("\t=== Dynamic Spectrum should be a 2D array ===")
        else:
            self._dynspec = ds
            return
    @property
    def frequency(self):
        """ Frequency, 1D array of floats
        """
        return self._frequency
    @frequency.setter
    def frequency(self, f):
        if f is None:
            return
        if not isinstance(f, np.ndarray):
            f = np.array(f)
        if len(f.shape) != 1:
            raise ValueError("\t=== Frequency should be a 1D array ===")
        else:
            self._frequency = f
            return
    @property
    def time(self):
        """ Time, 1D array of floats or time objects
        """
        return self._time
    @time.setter
    def time(self, t):
        if t is None:
            return
        if not isinstance(t, np.ndarray):
            t = np.array(t)
        if len(t.shape) != 1:
            raise ValueError("\t=== Time should be a 1D array ===")
        else:
            self._time = t
            return

    # ================================================================= #
    # =========================== Functions =========================== #
    def useme(self):
        image = np.random.rand(100, 50)

        dspec = Plot2D()
        dspec.imshow(image)
        dspec.show()
        return

    def save(self):
        """ 
        """
        return
    def show(self):
        return





