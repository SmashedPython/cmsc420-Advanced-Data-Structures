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
    
    def insert_helper(self,node,key,value):
        succes_insert = False

        for i in range(len(node.keys)):
            if node.keys[i] > key:
                node.keys.insert(i,key)
                node.values.insert(i,value)
                succes_insert = True
                break
        
        if not succes_insert:
            node.keys.append(key)
            node.values.append(value)  

    def find_parent_index(self,node):
        p = node.parent
        target = node.keys[0]
        for i in range(len(p.keys)):
            if p.keys[i] > target:
                return i
        
        return len(p.keys)

    def left_rotate(self, node, index):
        node.children[index].keys.append(node.keys[index ])
        node.children[index].values.append(node.values[index ])

        node.keys[index] = node.children[index+1].keys.pop(0)
        node.values[index] = node.children[index+1].values.pop(0)

        # until the sibling balanced
        if len(node.children[index + 1].keys) - len(node.children[index].keys) > 1:
            self.left_rotate(node, index)

    def right_rotate(self, node, index):
        node.children[index + 1].keys.insert(0, node.keys[index])
        node.children[index + 1].values.insert(0,node.values[index])

        node.keys[index] = node.children[index].keys.pop(-1)
        node.values[index] = node.children[index].values.pop(-1)

        if len(node.children[index].keys) - len(node.children[index + 1].keys) > 1:
            self.right_rotate(node, index)

    def split_promote(self, node):
        m = self.m

        # if the node is not full, then just do nothing

        if len(node.keys) <= m-1:
            return

        else:
            if node != self.root:

                parent = node.parent

                median_key = node.keys[(m-1)//2]
                median_value = node.values[(m-1)//2]

                newnode1 = Node(keys=node.keys[0:(m-1)//2], values= node.values[0:(m-1)//2], children= node.children[0:(m-1)//2 + 1], parent = parent)
                newnode2 = Node(keys=node.keys[(m-1)//2 + 1:], values= node.values[(m-1)//2 + 1:], children= node.children[(m-1)//2 + 1:], parent = parent)
                
                # update parents
                for child in newnode1.children:
                    child.parent = newnode1
                for child in newnode2.children:
                    child.parent = newnode2

                self.insert_helper(parent,median_key, median_value)
                for i in range(len(parent.children)):
                    if median_key in parent.children[i].keys:
                        parent.children.pop(i)
                        parent.children.insert(i,newnode2)
                        parent.children.insert(i,newnode1)
                        break
                
                self.split_promote(parent)
            # if the node we going to split is the root
            else:

                median_key = node.keys[(m-1)//2]
                median_value = node.values[(m-1)//2]

                newroot = Node(keys=[median_key], values=[median_value],children=[])
                newnode1 = Node(keys=node.keys[0:(m-1)//2], values= node.values[0:(m-1)//2], children= node.children[0:(m-1)//2 + 1], parent=newroot)
                newnode2 = Node(keys=node.keys[(m-1)//2 + 1:], values= node.values[(m-1)//2 + 1:], children= node.children[(m-1)//2 + 1:], parent=newroot)
                
                # update parents since we created new object
                for child in newnode1.children:
                    child.parent = newnode1
                for child in newnode2.children:
                    child.parent = newnode2

                newroot.children.append(newnode1)
                newroot.children.append(newnode2)

                self.root = newroot
                return

    def is_leaf(self, node):
        if node.children == None or len(node.children) == 0 or all(child is None for child in node.children):
            return True
        return False

    def CLEAN_NULL(self,node):
        node.children = [i for i in node.children if i is not None]
        for child in node.children:
            self.CLEAN_NULL(child)

    def ADD_NULL(self, node):
        if self.is_leaf(node):
            node.children = [None] *(len(node.keys) + 1)
        else:
            for child in node.children:
                if child != None:
                    self.ADD_NULL(child)

    def find_leaf(self, key,node):
        if self.is_leaf(node):
            return node
        for i in range(len(node.keys)):
            if key < node.keys[i]:
                return self.find_leaf(key,node.children[i])
        return self.find_leaf(key,node.children[-1])
    # Insert.
    def insert(self, key: int, value: str):
        if self.root == None:
            self.root = Node(keys=[key], values=[value],children=[None,None])
            return

        self.CLEAN_NULL(self.root)

        m = self.m

        # Go to the leaf
        current = self.find_leaf(key,self.root)

        # insert the key into the node
        if len(current.keys) < m - 1:
            # if it has extra space
            self.insert_helper(current, key, value)

        else:

            if self.root == current: # case we only have a root and it is full
                self.insert_helper(current,key,value)
                self.split_promote(current)
                self.ADD_NULL(self.root)
                return

            # try rotation first
            i = self.find_parent_index(current)
            parent = current.parent

            if i-1 >= 0 and len(parent.children[i - 1].keys) < m - 1:
                # left has space

                self.insert_helper(current,key,value)
                self.left_rotate(parent, i-1)

            elif i < len(parent.children) - 1 and len(parent.children[i + 1].keys) < m - 1:

                # right has space
                self.insert_helper(current,key,value)
                self.right_rotate(parent, i)

            else:
               # if there is no space in adjacent siblings we perform split and  promot
                self.insert_helper(current,key,value)
                self.split_promote(current)

        self.ADD_NULL(self.root)




    # Delete.
    def delete(self, key: int):
        # Fill in the details.
        print(f'Delete: {key}') # This is just here to make the code run, you can delete it.

    # Search
    def search_helper(self, key, node, path):
        if key in node.keys:
            index = node.keys.index(key)
            path.append(node.values[index])
            return path
        else:
            for i in range(len(node.keys)):
                if key < node.keys[i]:
                    path.append(i)
                    return self.search_helper(key, node.children[i], path)
            
            path.append(len(node.keys))
            return self.search_helper(key, node.children[-1], path)


    def search(self,key) -> str:
        if key in self.root.keys:
            return json.dumps([self.root.values[self.root.keys.index(key)]])
        self.CLEAN_NULL(self.root)
        return json.dumps(self.search_helper(key,self.root,[]))

# t = Btree(3)
# t.insert(1,1)

# t.insert(2,2)
# t.insert(3,3)
# t.insert(0,0)
# t.insert(4,4)

# t.insert(5,5)

# t.insert(6,6)
# t.insert(-1,-1)

# t.insert(-2,-2)
# t.insert(7,7)

# print(t.dump())
# t = Btree(3)
# t.insert(77,"04PP93ZH9T")
# t.insert(76,"HE8AWZKX91")
# t.insert(99,"TG4CNACOBA")
# t.insert(44,"RJCJ6AG6WG")
# t.insert(21,"T34BOLK8K4")
# t.insert(58,"DHJ9XLHDZP")

# t.insert(67,"YPJMKFOU7L")
# t.insert(86,"J3HMG3WIND")
# t.insert(63,"X4EYGXZBBV")

# t.insert(85,"31C5Y78YEI")
# print(t.dump())
