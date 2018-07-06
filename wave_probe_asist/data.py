"""
data.py -- functions to read ASIST wave probe data.
"""

import os

DATA_PATH = os.environ['ASIST_DATA_PATH']

def load_data():
    """Returns time and elevation time series from CSV file."""
    datafile = DATA_PATH + '/deep/redo_rte01_ID1_Ch1_Channel 1.csv'
    data = [line.rstrip() for line in open(datafile).readlines()]
    time = []
    elevation = []
    for line in data[2:]:
        line = line.split(',')
        time.append(float(line[0]))
        elevation.append(float(line[2]))
    return time, elevation
