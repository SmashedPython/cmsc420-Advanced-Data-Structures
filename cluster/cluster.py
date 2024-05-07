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
        self.laplacian = np.zeros((nodecount,nodecount),dtype = np.complex128)

    # Add an edge to the Laplacian matrix.
    # An edge is a pair [x,y].
    def addedge(self,edge):
        # Your code goes here.
        x, y = edge
        self.laplacian[x, x] += 1
        self.laplacian[y, y] += 1
        self.laplacian[x, y] -= 1
        self.laplacian[y, x] -= 1

    # Don't change this - no need.
    def laplacianmatrix(self) -> np.array:
        return self.laplacian

    # Calculate the Fiedler vector and return it.
    # You can use the default one from np.linalg.eig
    # but make sure the first entry is positive.
    # If not, negate the whole thing.
    def fiedlervector(self) -> np.array:
        # Replace this next line with your code.
        
        eigenvalues, eigenvectors = np.linalg.eig(self.laplacian)
        fvec = eigenvectors[:, np.argsort(eigenvalues)[1]]
        if fvec[0] < 0:
            fvec = -fvec
        return fvec

    # Cluster the nodes.
    # You should return a list of two lists.
    # The first list contains all the indices with nonnegative (positive and 0) Fiedler vector entry.
    # The second list contains all the indices with negative Fiedler vector entry.

    def clustersign(self):
        # Replace the next two lines with your code.
        pind = []
        nind = []
        fvec = self.fiedlervector()
        # Classify nodes based on the sign of the Fiedler vector entries
        pind = [i for i in range(self.nodecount) if fvec[i] >= 0]
        nind = [i for i in range(self.nodecount) if fvec[i] < 0]
        return [pind, nind]
        return([pind,nind])