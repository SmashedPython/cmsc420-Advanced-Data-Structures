# This is provided to you so that you can test your bst.py file with a particular tracefile.

import argparse
import csv
import bst

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-tf', '--tracefile')
    args = parser.parse_args()
    tracefile = args.tracefile

    t = None
    with open(tracefile, "r") as f:
        reader = csv.reader(f)
        lines = [l for l in reader]
        for l in lines:
            if l[0] == 'insert':
                t = bst.insert(t,int(l[1]),int(l[2]))
            if l[0] == 'delete':
                t = bst.delete(t,int(l[1]))
            if l[0] == 'search':
                print(bst.search(t,int(l[1])))
            if l[0] == 'dump':
                print(bst.dump(t))
            if l[0] == 'restructure':
                t = bst.restructure(t)