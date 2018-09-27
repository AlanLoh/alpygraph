#! /usr/bin/python3.5
# -*- coding: utf-8 -*-

"""
Base parameters for own matplotlib plots
"""

import matplotlib as mpl

__author__ = 'Alan Loh'
__copyright__ = 'Copyright 2018, alpygraph'
__credits__ = ['Alan Loh']
__license__ = 'MIT'
__version__ = '0.0.1'
__maintainer__ = 'Alan Loh'
__email__ = 'alan.loh@obspm.fr'
__status__ = 'WIP'
# __all__ = ['Plot2D']
      
params = {
      'axes.formatter.limits' : [-5, 5],
      'axes.grid': False,
      'axes.labelsize': 9,
      'axes.titlesize': 9,
      'axes.linewidth': 1,
      'axes.titlesize': 'large',
      # 'axes.prop_cycle': cycler('color', ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']),
      'errorbar.capsize': 0,
      # 'figure.figsize': [xsize/2.54, ysize/2.54],
      'font.family': 'serif',
      'font.size': 9,
      'image.origin': 'lower',
      'image.interpolation': 'nearest',
      'image.cmap': 'bone',
      'legend.fontsize': 6,
      'legend.loc': 'best',
      'legend.markerscale': 1,
      'legend.numpoints': 1,
      'lines.linewidth': 0.5,
      'lines.marker': '',
      'lines.markeredgewidth': 0,
      'lines.markersize': 4,
      'lines.antialiased': True,
      'patch.edgecolor': 'none',
      'patch.facecolor': '0.8',
      'savefig.directory': '',
      'savefig.dpi': 150,
      'savefig.facecolor': 'none',
      'savefig.edgecolor': 'none',
      'savefig.bbox': 'tight',
      'savefig.transparent': True,
      'text.usetex': True,
      'text.latex.preamble': ['\\usepackage{gensymb}\\usepackage{amssymb}\\usepackage{amsmath}'],
      'xtick.labelsize': 6,
      'xtick.major.width': 1,
      'xtick.minor.width': 0.5,
      'xtick.minor.visible': True,
      'xtick.direction': 'out',
      'ytick.labelsize': 6,
      'ytick.major.width': 1,
      'ytick.minor.width': 0.5,
      'ytick.minor.visible': True,
      'ytick.direction': 'out',
      }
mpl.rcParams.update(params)