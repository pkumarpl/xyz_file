#!/usr/bin/env python
# -*- coding=utf-8 -*-

"""
read_xyz_write_xyz
NAME     
        xyz.py - extract geometry from a xyz file
SYNTAX
        ./xyz.py <input xyz filename>
DESCRIPTION
        scripy for reading from and writing to .xyz files and  perform translation
    
AUTHOR
        Prashant Kumar <prashantkbio@gmail.com>
"""

__author__ = "Prashant Kumar"
__email__ = "prashantkbio@gmail.com"
__licence__ = "GPL"



import numpy as np
from itertools import cycle
from collections import namedtuple
import sys
import os

def usage(code):
    """ xyz usage """
    print(__doc__)
    exit(code)

def read_xyz(args):


    # ----------------------------------------------------------
    # option
    # ----------------------------------------------------------
    narg = len(args)
    if narg == 2:
        if args[1] == "-h" or args[1] == "--help":
            usage(0)
        else:
            if not os.path.exists(args[1]):
                print("Error : file {0} does not exist".format(args[1]))
                exit(1)
            else:
                file = args[1].strip()
                file = open(file, "r")
    else:
        print(args)
        print("Error : bad arguments")

    """ read a xyz file from file handle
    Parameters
    ----------
    file : file handle
        file to read from
    Returns
    -------
    xyz : namedtuple
        returns a named tuple with coords, title and list of atomtypes.
    """
    #file = open(fin, 'r')
    #print(file)
    natoms = int(file.readline())
    #print(natoms)
    title = file.readline()[:-1]
    print(title)
    coords = np.zeros([natoms, 3], dtype="float64")
    atomtypes = []
    for x in coords:
        line = file.readline().split()
        atomtypes.append(line[0])
        x[:] = list(map(float, line[1:4]))
    file.close()
    #print(coords)
    '''
    write xyz file
    Parameters
    ----------
    name : file handle
    Returns
    -------
    moved atoms by adding 50.0 50.0 50.0 
    out.xyz as output file
    '''
    name = 'out.xyz'
    with open(name, 'w') as fout:
    	fout.write("%d\n%s\n" % (coords.size / 3, title))
    	for x, atomtype in zip(coords.reshape(-1, 3), cycle(atomtypes)):
    		fout.write("%s %.18g %.18g %.18g\n" % (atomtype, x[0]+50.0, x[1]+50.0, x[2]+50.0))
        
    return namedtuple("XYZFile", ["coords", "title", "atomtypes"]) \
        (coords, title, atomtypes)

        
if __name__ == "__main__":
    read_xyz(sys.argv)
