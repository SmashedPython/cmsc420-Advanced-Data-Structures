# This is provided to you so that you can test your file with a particular tracefile.

import argparse
import csv
import cluster

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-tf', '--tracefile')
    args = parser.parse_args()
    tracefile = args.tracefile

    g = None
    with open(tracefile, "r") as f:
        reader = csv.reader(f)
        lines = [l for l in reader]
        for l in lines:
            if l[0] == 'nodecount':
                g = cluster.Graph(int(l[1]))
            if l[0] == 'addedge':
                g.addedge([int(l[1]),int(l[2])])
            if l[0] == 'laplacianmatrix':
                print(g.laplacianmatrix())
            if l[0] == 'fiedlervector':
                print(g.fiedlervector())
            if l[0] == 'clustersign':
                print(g.clustersign())