#!/usr/bin/python3

# chaotic: 3D phase space visualization of an n-dimensional dataset
#
# copyright 2020 Gregory V. Perry || GregoryVPerry@pm.me
#
# LICENSE: you are free to use this source code in any way you want, as long as you give me a shout out with
#          my email address on any deriviative code implementation and/or published research that follows.
#

import argparse, numpy as np
from itertools import islice
from mayavi import mlab


parser = argparse.ArgumentParser(description = 'chaotic: 3D phase space visualization of an n-dimensional dataset',
        usage = 'python3 %(prog)s [-h] FILE [-i/-f] [-l N] [-e N] [-v]',
        formatter_class = argparse.RawTextHelpFormatter)

parser.add_argument('file', metavar = 'FILE', type = str, nargs = '+',
                    help = 'dataset to analyze, one value per line')

group = parser.add_mutually_exclusive_group(required = True)
group.add_argument('-i', '--int', action = 'store_true', dest = 'intpoints', help = 'integer valued dataset')
group.add_argument('-f', '--float', action = 'store_true', dest = 'floatpoints', help = 'float valued dataset')

parser.add_argument('-l', '--lag', action = 'store', dest = 'lag',
                    default = 2, help = 'lag length, default 2', type = int)

parser.add_argument('-e', '--embed', action = 'store', dest = 'embed',
                    default = 3, help = 'embedding dimension, default 3', type = int)

parser.add_argument('-v', '--verbose', action = 'store_true', default = False,
                    dest = 'verbose',
                    help = 'verbose mode')

parser._optionals.title = "flag options"
results = parser.parse_args()

def plot_points(points):
    x = points[results.lag-2:len(points):results.embed]
    y = points[results.lag-1:len(points):results.embed]
    z = points[results.lag:len(points):results.embed]
    min_size = min(x.size, y.size, z.size)
    x = x[:min_size]
    y = y[:min_size]
    z = z[:min_size]
    return mlab.points3d(x, y, z, mode = 'point')

if results.verbose == True:
    print('file        = ', results.file[0])
    print('intpoints   = ', results.intpoints)
    print('floatpoints = ', results.floatpoints)
    print('laglength   = ', results.lag)
    print('embeddim    = ', results.embed)
    print('verbose     = ', results.verbose)

if results.intpoints == True:
    points = np.loadtxt(results.file[0], dtype = 'int')
    x = np.array([], dtype = 'int')
    y = np.array([], dtype = 'int')
    z = np.array([], dtype = 'int')
else:
    points = np.loadtxt(results.file[0], dtype = 'float')
    x = np.array([], dtype = 'float')
    y = np.array([], dtype = 'float')
    z = np.array([], dtype = 'float')

mlab.figure(results.file[0], size=(896, 896), fgcolor=(1, 1, 1), bgcolor=(0, 0, 0))
plot_points(points)
mlab.show()
