# This is provided to you so that you can test your bst.py file with a particular tracefile.

import argparse
import csv
import skiplist

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-tf', '--tracefile')
    args = parser.parse_args()
    tracefile = args.tracefile

    t = skiplist.SkipList(None)
    with open(tracefile, "r") as f:
        reader = csv.reader(f)
        lines = [l for l in reader]
        for l in lines:
            if l[0] == 'initialize':
                t.initialize(int(l[1]))
            if l[0] == 'insert':
                t.insert(int(l[1]),str(l[2]),int(l[3]))
            if l[0] == 'delete':
                t.delete(int(l[1]))
            if l[0] == 'search':
                print(t.search(int(l[1])))
            if l[0] == 'dump':
                print(t.dump())
            if l[0] == 'pretty':
                print(t.pretty())
