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

    def size(self,node):
        if node is None:
            return 0

        leftsize = self.size(node.leftchild)
        rightsize = self.size(node.rightchild)
        return leftsize + rightsize + 1

    def depth(self,node):
        if node is None:
            return -1

        leftsize = self.depth(node.leftchild)
        rightsize = self.depth(node.rightchild)
        return max(leftsize,rightsize) + 1

    def reconstruct(self, node):

        def in_order_traverse(root):
            if root == None:
                return []

            return in_order_traverse(root.leftchild) + [(root.key,root.value)] + in_order_traverse(root.rightchild)

        
        def construct(pairs):
            if not pairs:
                return None
            mid = len(pairs)//2

            root = Node(key = pairs[mid][0], value=  pairs[mid][1])

            root.leftchild = construct(pairs[:mid])
            if(root.leftchild != None):
                root.leftchild.parent = root

            root.rightchild = construct(pairs[mid+1:])
            if(root.rightchild != None):
                root.rightchild.parent = root
            return root
        
        # Remove the next line and fill in code to restructure and assign the newroot.
        pairs = in_order_traverse(node)
        # print(pairs)
        newroot = construct(pairs=pairs)
        self.m = self.n
        return(newroot)

    def insert(self, key: int, value: str):
        if self.root == None:
            self.root = Node(key,value)
            self.m = 1
            self.n = 1
            return
        
        #perform insertion
        node = Node(key = key, value = value)

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

        
        if self.m == self.n:
            self.m += 1

        self.n += 1

        ratio = self.a/self.b
        d = self.depth(self.root)

        # check for scapegoat
        if d > math.log(self.n,1/ratio):
            # go back to find the scapegoat
            # print(key)
            p = prev
            while p != None:
                if self.size(p.leftchild)/self.size(p) > ratio or self.size(p.rightchild)/self.size(p) > ratio:
                    # print("s",p.key)
                    newroot = self.reconstruct(p)
                    # print("k", newroot.key)
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
            if root.leftchild != None:
                root.leftchild.parent = root
        elif key > root.key:
            root.rightchild = self.delete_helper(root.rightchild,key)
            if root.rightchild != None:
                root.rightchild.parent = root
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
        if self.n < (self.a / self.b) * self.m:
            # print(key)
            self.root = self.reconstruct(self.root)



    def search(self, search_key: int) -> str:
        value_list = []
        current = self.root
        while current.key != search_key:
            value_list.append(current.value)
            if current.key > search_key:
                current = current.leftchild
            else:
                current = current.rightchild

        value_list.append(current.value)
        return  json.dumps(value_list)

