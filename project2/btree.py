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

        # print("here is the node being promote", node.children[index+1].keys)
        node.keys[index] = node.children[index+1].keys.pop(0)

        node.values[index] = node.children[index+1].values.pop(0)

    def right_rotate(self, node, index):
        node.children[index + 1].keys.insert(0, node.keys[index])
        node.children[index + 1].values.insert(0,node.values[index])

        node.keys[index] = node.children[index].keys.pop(-1)
        node.values[index] = node.children[index].values.pop(-1)

    def split_promote(self, node):
        m = self.m

        if len(node.keys) <= m-1:
            return
        else:
            if node != self.root:
                parent = node.parent

                median_key = node.keys[(m-1)//2]
                median_value = node.values[(m-1)//2]

                newnode1 = Node(keys=node.keys[0:(m-1)//2], values= node.values[0:(m-1)//2], children= node.children[0:(m-1)//2 + 1], parent = parent)
                newnode2 = Node(keys=node.keys[(m-1)//2 + 1:], values= node.values[(m-1)//2 + 1:], children= node.children[(m-1)//2 + 1:], parent = parent)

                self.insert_helper(parent,median_key, median_value)
                for i in range(len(parent.children)):
                    if median_key in parent.children[i].keys:
                        parent.children.pop(i)
                        parent.children.insert(i,newnode2)
                        parent.children.insert(i,newnode1)
                        break
                
                self.split_promote(parent)
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
        if node.children == None or len(node.children) == 0:
            return True
        return False


    # Insert.
    def insert(self, key: int, value: str):
        if self.root == None:
            self.root = Node(keys=[key], values=[value],children=[])
            return

        m = self.m

        # Go to the leaf
        current = self.root

        while not self.is_leaf(current):

            i = 0
            while i < len(current.keys):

                if current.keys[i] > key:
                    current = current.children[i]
                    break
                i += 1
            if i == len(current.keys):
                current = current.children[i]

        #now current is a leaf
        if len(current.keys) < m - 1:
            # if it has extra space
            self.insert_helper(current, key, value)
        else:

            if self.root == current: # case we only have a root and it is full
                self.insert_helper(current,key,value)
                self.split_promote(current)
                return

            # try rotation first
            i = self.find_parent_index(current)
            parent = current.parent
            # print(parent.keys)
            # print(self.dump())
            # print(parent.children)
            # print("here0")
            if i-1 >= 0 and len(parent.children[i - 1].keys) < m - 1:
                # left has space

                self.insert_helper(current,key,value)
                self.left_rotate(parent, i-1)

            elif i < len(parent.children) - 1 and len(parent.children[i + 1].keys)< m - 1:
                # right has space

                self.insert_helper(current,key,value)
                self.right_rotate(parent, i)
            else:
               # if there is no space in adjacent siblings

                self.insert_helper(current,key,value)
                self.split_promote(current)




    # Delete.
    def delete(self, key: int):
        # Fill in the details.
        print(f'Delete: {key}') # This is just here to make the code run, you can delete it.

    # Search
    def search(self,key) -> str:
        # Fill in and tweak the return.
        return json.dumps(None)


t = Btree(3)
t.insert(1,1)
t.insert(2,2)
t.insert(3,3)
t.insert(0,0)
t.insert(4,4)

t.insert(5,5)

t.insert(6,6)
t.insert(-1,-1)

t.insert(-2,-2)
print("root",t.root.keys)
print(t.dump())
t.insert(7,7)

print(t.dump())


