from __future__ import annotations
import json
from typing import List

# Node Class.
# You may make minor modifications.
class Node():
    def  __init__(self,
                  keys     : List[int]  = None,
                  values   : List[str] = None,
                  children : List[Node] = None,
                  parent   : Node = None):
        self.keys     = keys
        self.values   = values
        self.children = children
        self.parent   = parent

# DO NOT MODIFY THIS CLASS DEFINITION.
class Btree():
    def  __init__(self,
                  m    : int  = None,
                  root : Node = None):
        self.m    = m
        self.root = root

    # DO NOT MODIFY THIS CLASS METHOD.
    def dump(self) -> str:
        def _to_dict(node) -> dict:
            return {
                "keys": node.keys,
                "values": node.values,
                "children": [(_to_dict(child) if child is not None else None) for child in node.children]
            }
        if self.root == None:
            dict_repr = {}
        else:
            dict_repr = _to_dict(self.root)
        return json.dumps(dict_repr,indent=2)

    # Insert.
    def insert(self, key: int, value: str):
        if self.root == None:
            self.root = Node(keys=[key], values=[value])
            return
        
        # try rotation first 
        
        # if root is full, create a new root
        if len(root.keys) == m - 1:
            newroot = Node(children= [])
            self.root = newroot
            newroot.children.insert(0,root)
            self.split_child(newroot,0)
            self.insert_unfull(node=newroot,key=key,value=value)
        else:
            self.insert_unfull(root,key,value)

    def split_child(self, node, index):
        m = self.m

        child = node.children[index]
        newnode = Node()
        node.children.insert(index + 1,newnode)

        #promote the middle one into the node
        node.keys.insert(index, child.keys[m//2])
        node.values.insert(index, child.values[m//2])

        #split into 2
        child.keys = child.keys[0 : m//2 - 1]
        newnode.keys = child.keys[m//2 + 1: ]
        child.values = child.values[0 : m//2 - 1]
        newnode.values = child.values[m//2 + 1: ]

        if not check_leaf(child):
            newnode.children = child.children[m//2: ]
            child.children = child.children[ :m//2-1 ]



    def check_leaf(node):
        if node.children == None or  node.children == []:
            return True
        return False

    def insert_unfull(self,node,key,value):
        m = self.m
        i = len(node.keys)-1

        
        if check_leaf(node):
            # if the node is a leaf, we add key/value into the node
            node.keys.append(None)
            node.values.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i+1] = node.keys[i]
                node.values[i+1] = node.values[i]

                i -= 1
            node.keys[i+1] = key
            node.values[i+1] = value
        else:
            # if it is not a leaf, we find the correct subtree
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            # if child node is full, split it
            if len(node.children[i]) == m-1:
                self.split_child(node,i)
                if key > x.keys[i]:
                    i += 1
            self.insert_unfull(node = node.children[i],key=key,value=value)




    # Delete.
    def delete(self, key: int):
        # Fill in the details.
        print(f'Delete: {key}') # This is just here to make the code run, you can delete it.

    # Search
    def search(self,key) -> str:
        # Fill in and tweak the return.
        return json.dumps(None)