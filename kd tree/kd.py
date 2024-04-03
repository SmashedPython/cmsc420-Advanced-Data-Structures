from __future__ import annotations
import json
import math
from typing import List
import heapq
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
        def delete_from_leaf(node, point):
            for i, datum in enumerate(node.data):
                if datum.coords == point:
                    del node.data[i]
                    break
            return node, len(node.data) == 0

        def delete_helper(node,point):
            if isinstance(node, NodeLeaf):
                node, is_empty = delete_from_leaf(node, point)
                return None if is_empty else node
            else:
                if point[node.splitindex] < node.splitvalue:
                    node.leftchild = delete_helper(node.leftchild, point)
                else:
                    node.rightchild = delete_helper(node.rightchild, point)
                
                if node.leftchild is None:
                    return node.rightchild
                elif node.rightchild is None:
                    return node.leftchild
                return node
        
        self.root = delete_helper(self.root, point)

    # Find the k nearest neighbors to the point.
    def knn(self,k:int,point:tuple[int]) -> str:
        # Use the strategy discussed in class and in the notes.
        # The list should be a list of elements of type Datum.
        # While recursing, count the number of leaf nodes visited while you construct the list.
        # The following lines should be replaced by code that does the job.

        def sq_euclidean_distance(p1,p2):
            return sum((x - y) ** 2 for x, y in zip(p1, p2))

        def bounding_box(node, min_bound, max_bound):
            if isinstance(node, NodeLeaf):
                for datum in node.data:
                    for i in range(self.k):
                        min_bound[i] = min(min_bound[i], datum.coords[i])
                        max_bound[i] = max(max_bound[i], datum.coords[i])

            else:
                bounding_box(node.leftchild, min_bound, max_bound)
                bounding_box(node.rightchild, min_bound, max_bound)

            return 

        def sq_distance_to_bondingbox(point,min_bound,max_bound):
            distant = 0
            for i in range(self.k):
                if not (point[i] >= min_bound[i] and point[i] <= max_bound[i]):
                    distant += min(abs(point[i] - min_bound[i]),abs(point[i] - max_bound[i]))**2

            return distant

        
        def knn_helper(node,k,point):
            nonlocal leaveschecked
            nonlocal knnlist

            if isinstance(node, NodeLeaf):
                leaveschecked += 1

                for datum in node.data:
                    distance = sq_euclidean_distance(point, datum.coords)
                    if len(knnlist) < k:
                        heapq.heappush(knnlist, (-distance, datum))
                    else:
                        if distance < -knnlist[0][0] or (distance == - knnlist[0][0] and datum.code < knnlist[0][1].code):
                            heapq.heapreplace(knnlist, (-distance, datum))
                        
            else:
                if len(knnlist) < k:
                    min_bound = [float('inf')] * self.k
                    max_bound = [float('-inf')] * self.k
                    bounding_box(node.leftchild, min_bound, max_bound)

                    dist_left = sq_distance_to_bondingbox(point,min_bound,max_bound)

                    min_bound = [float('inf')] * self.k
                    max_bound = [float('-inf')] * self.k
                    bounding_box(node.rightchild, min_bound, max_bound)
                    dist_right = sq_distance_to_bondingbox(point,min_bound,max_bound)


                    if dist_left <= dist_right:
                        knn_helper(node.leftchild,k,point)
                        if len(knnlist) < k or dist_right <= -knnlist[0][0]:

                            knn_helper(node.rightchild,k,point)

                    else:
                        knn_helper(node.rightchild,k,point)
                        if len(knnlist) < k or dist_left <= -knnlist[0][0]:

                            knn_helper(node.leftchild,k,point)
                else:
                    min_bound = [float('inf')] * self.k
                    max_bound = [float('-inf')] * self.k
                    bounding_box(node,min_bound,max_bound)



                    if sq_distance_to_bondingbox(point,min_bound,max_bound) <= -knnlist[0][0]:
                        
                        min_bound = [float('inf')] * self.k
                        max_bound = [float('-inf')] * self.k
                        bounding_box(node.leftchild, min_bound, max_bound)

                        dist_left = sq_distance_to_bondingbox(point,min_bound,max_bound)

                        min_bound = [float('inf')] * self.k
                        max_bound = [float('-inf')] * self.k
                        bounding_box(node.rightchild, min_bound, max_bound)
                        dist_right = sq_distance_to_bondingbox(point,min_bound,max_bound)

                        
                        if dist_left <= dist_right:
                            if dist_left <= -knnlist[0][0]:
                                knn_helper(node.leftchild,k,point)
                            if dist_right <= -knnlist[0][0]:
                                knn_helper(node.rightchild,k,point)

                        else:
                            if dist_right <= -knnlist[0][0]:
                                knn_helper(node.rightchild,k,point)
                            if dist_left <= -knnlist[0][0]:
                                knn_helper(node.leftchild,k,point)            
            

        leaveschecked = 0
        knnlist = []

        knn_helper(self.root,k,point)
        knnlist = [heapq.heappop(knnlist)[1] for _ in range(len(knnlist))]
        knnlist.reverse() 

        # The following return line can probably be left alone unless you make changes in variable names.
        return(json.dumps({"leaveschecked":leaveschecked,"points":[datum.to_json() for datum in knnlist]},indent=2))

