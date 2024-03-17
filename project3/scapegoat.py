from __future__ import annotations
import json
import math
from typing import List

# Node Class
# You may make minor modifications.

class Node():
    def  __init__(self,
                  key        = None,
                  value      = None,
                  leftchild  = None,
                  rightchild = None,
                  parent     = None):
        self.key        = key
        self.value      = value
        self.leftchild  = leftchild
        self.rightchild = rightchild
        self.parent     = parent

# Scapegoat Tree Class.
# DO NOT MODIFY.
class SGtree():
    def  __init__(self,
                  a    : int  = None,
                  b    : int  = None,
                  m    : int  = None,
                  n    : int  = None,
                  root : Node = None):
        self.m     = 0
        self.n     = 0
        self.a     = a
        self.b     = b
        self.root  = None

    # For the tree rooted at root, dump the tree to stringified JSON object and return.
    def dump(self) -> str:
        def _to_dict(node) -> dict:
            pk = None
            if node.parent is not None:
                pk = node.parent.key
            return {
                "k": node.key,
                "v": node.value,
                "l": (_to_dict(node.leftchild)  if node.leftchild  is not None else None),
                "r": (_to_dict(node.rightchild) if node.rightchild is not None else None)
            }
        if self.root == None:
            dict_repr = {}
        else:
            dict_repr = _to_dict(self.root)
        return json.dumps(dict_repr,indent=2)

    def insert(self, key: int, value: str):
        # Fill in the details.
        print(f'Insert: {key},{value}') # This is just here to make the code run, you can delete it.

<<<<<<< HEAD
        prev = None
        current = self.root

        while current != None:
            prev = current

            if current.key > key:
                current = current.leftchild
            else:
                current = current.rightchild

        node.parent = prev
        if prev.key > key:
            prev.leftchild = node
        else:
            prev.rightchild = node

        self.n += 1
        self.m += 1
        ratio = self.a/self.b
        d = self.depth(self.root)

        # check for scapegoat
        if d > math.log(self.n,1/ratio):
            # go back to find the scapegoat
            p = prev
            while p != None:
                if self.size(p.leftchild)/self.size(p) > ratio or self.size(p.rightchild)/self.size(p) > ratio:
                    newroot = self.reconstruct(p)
                    if p == self.root:
                        self.root = newroot
                    else:
                        newroot.parent = p.parent

                        if p.parent.key > newroot.key:
                            p.parent.leftchild = newroot
                        else:
                            p.parent.rightchild = newroot
                            
                    break

                else: p = p.parent

    def delete_helper(self, root, key):
        def find_inorder_successor(node):
            current = node
            while current.leftchild != None:
                current = current.leftchild
            return current

        if root == None:
            return None
        
        if key < root.key:
            root.leftchild = self.delete_helper(root.leftchild,key)
        elif key > root.key:
            root.rightchild = self.delete_helper(root.rightchild,key)
        else:
            if root.leftchild == None:
                return root.rightchild
            
            elif root.rightchild == None:
                return root.leftchild

                
            temp = find_inorder_successor(root.rightchild)
            root.key = temp.key
            root.value = temp.value
            root.rightchild = self.delete_helper(root.rightchild, temp.key)

        return root
    
    def delete(self, key: int):
        self.root = self.delete_helper(self.root,key)
        self.n -= 1
        if self.n < self.a/ self.b * self.m:
            self.root = self.reconstruct(self.root)
            self.m = self.n

        

    




=======
    def delete(self, key: int):
        # Fill in the details.
        print(f'Delete: {key}') # This is just here to make the code run, you can delete it.
>>>>>>> parent of 74f84fd (')

    def search(self, search_key: int) -> str:
        # Fill in and tweak the return.
        return json.dumps(None)
