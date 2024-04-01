from __future__ import annotations
import json
import math
from typing import List

# Datum class.
# DO NOT MODIFY.
class Datum():
    def __init__(self,
                 coords : tuple[int],
                 code   : str):
        self.coords = coords
        self.code   = code
    def to_json(self) -> str:
        dict_repr = {'code':self.code,'coords':self.coords}
        return(dict_repr)

# Internal node class.
# DO NOT MODIFY.
class NodeInternal():
    def  __init__(self,
                  splitindex : int,
                  splitvalue : float,
                  leftchild,
                  rightchild):
        self.splitindex = splitindex
        self.splitvalue = splitvalue
        self.leftchild  = leftchild
        self.rightchild = rightchild

# Leaf node class.
# DO NOT MODIFY.
class NodeLeaf():
    def  __init__(self,
                  data : List[Datum]):
        self.data = data

# KD tree class.
class KDtree():
    def  __init__(self,
                  splitmethod : str,
                  k           : int,
                  m           : int,
                  root        : NodeLeaf = None):
        self.k    = k
        self.m    = m
        self.splitmethod = splitmethod
        self.root = root

    # For the tree rooted at root, dump the tree to stringified JSON object and return.
    # DO NOT MODIFY.
    def dump(self) -> str:
        def _to_dict(node) -> dict:
            if isinstance(node,NodeLeaf):
                return {
                    "p": str([{'coords': datum.coords,'code': datum.code} for datum in node.data])
                }
            else:
                return {
                    "splitindex": node.splitindex,
                    "splitvalue": node.splitvalue,
                    "l": (_to_dict(node.leftchild)  if node.leftchild  is not None else None),
                    "r": (_to_dict(node.rightchild) if node.rightchild is not None else None)
                }
        if self.root is None:
            dict_repr = {}
        else:
            dict_repr = _to_dict(self.root)
        return json.dumps(dict_repr,indent=2)

    # Insert the Datum with the given code and coords into the tree.
    # The Datum with the given coords is guaranteed to not be in the tree.
    def insert(self,point:tuple[int],code:str):
        
        def split_leaf(leaf, split_index, split_value):
            sorted_data = sorted(leaf.data, key=lambda d: d.coords[split_index])

            left_data = [d for d in sorted_data if d.coords[split_index] < split_value]
            right_data = [d for d in sorted_data if d.coords[split_index] >= split_value]
            return NodeLeaf(left_data), NodeLeaf(right_data)

        def find_split_value(data ,split_index):
            values = sorted(d.coords[split_index] for d in data)
            if len(values)% 2 ==0:
                return float(values[len(values) // 2 - 1] + values[len(values) // 2 ])/2
            else:
                return float(values[len(values) // 2])

        def split_helper(depth,data):      
            if self.splitmethod == "spread":
                max_spread = -1
                split_index = -1
                for i in range(self.k):
                    dim_values = [d.coords[i] for d in data]
                    spread = max(dim_values) - min(dim_values)
                    if spread > max_spread:
                        max_spread = spread
                        split_index = i

                split_value = find_split_value(data,split_index)
            else:         
                split_index = depth % self.k
                split_value = find_split_value(data,split_index)
            return split_index,split_value

        def insert_helper(node,depth):
            if self.root == None:
                return NodeLeaf([Datum(point, code)])

            if isinstance(node, NodeLeaf):

                node.data.append(Datum(point, code))
                # for i in node.data:
                #     print(i.coords, i.code)

                if len(node.data) > self.m:
                    # perform a split
                    split_index, split_value = split_helper(depth,node.data)

                    leftchild, rightchild = split_leaf(node, split_index, split_value)
                    return NodeInternal(splitindex= split_index, splitvalue= split_value, leftchild= leftchild, rightchild= rightchild)
                return node

            else:
                # we are in internal node
                if point[node.splitindex] < node.splitvalue:
                    node.leftchild = insert_helper(node.leftchild,depth + 1)
                else:
                    node.rightchild = insert_helper(node.rightchild, depth + 1)
                return node


        self.root = insert_helper(self.root,0)

    # Delete the Datum with the given point from the tree.
    # The Datum with the given point is guaranteed to be in the tree.
    def delete(self,point:tuple[int]):
        thisisaplaceholder = True

    # Find the k nearest neighbors to the point.
    def knn(self,k:int,point:tuple[int]) -> str:
        # Use the strategy discussed in class and in the notes.
        # The list should be a list of elements of type Datum.
        # While recursing, count the number of leaf nodes visited while you construct the list.
        # The following lines should be replaced by code that does the job.
        leaveschecked = 0
        knnlist = []
        # The following return line can probably be left alone unless you make changes in variable names.
        return(json.dumps({"leaveschecked":leaveschecked,"points":[datum.to_json() for datum in knnlist]},indent=2))


# tree = KDtree("spread",5,6)
# tree.insert([4,14,10,12,9], "ZPJ")
# tree.insert([9,8,7,15,5], "AVM")
# print(tree.dump())