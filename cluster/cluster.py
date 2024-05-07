from __future__ import annotations
import json
import math
from typing import List
import numpy as np

class Graph():
    def  __init__(self,
            nodecount : None):
        self.nodecount = nodecount
        # IMPORTANT!!!
        # Replace the next line so the Laplacian is a nodecount x nodecount array of zeros.
        # You will need to do this in order for the code to run!
        self.laplacian = 1

    # Add an edge to the Laplacian matrix.
    # An edge is a pair [x,y].
    def addedge(self,edge):
        # Your code goes here.
        print('Filler code...')
        # Nothing to return.

    # Don't change this - no need.
    def laplacianmatrix(self) -> np.array:
        return self.laplacian

    # Calculate the Fiedler vector and return it.
    # You can use the default one from np.linalg.eig
    # but make sure the first entry is positive.
    # If not, negate the whole thing.
    def fiedlervector(self) -> np.array:
        # Replace this next line with your code.
        fvec = [0]
        # Return
        return fvec

    # Cluster the nodes.
    # You should return a list of two lists.
    # The first list contains all the indices with nonnegative (positive and 0) Fiedler vector entry.
    # The second list contains all the indices with negative Fiedler vector entry.

    def clustersign(self):
        # Replace the next two lines with your code.
        pind = []
        nind = []
        # Return
        return([pind,nind])