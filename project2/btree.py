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
        # Fill in the details.
        print(f'Insert: {key} {value}') # This is just here to make the code run, you can delete it.

    # Delete.
    def delete(self, key: int):
        # Fill in the details.
        print(f'Delete: {key}') # This is just here to make the code run, you can delete it.

    # Search
    def search(self,key) -> str:
        # Fill in and tweak the return.
        return json.dumps(None)