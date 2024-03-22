# BST Variation 1

from __future__ import annotations
import json

# The class for a particular node in the tree.
# DO NOT MODIFY!
class Node():
    def  __init__(self,
                  key        : int  = None,
                  value      : int  = None,
                  leftchild  : Node = None,
                  rightchild : Node = None):
        self.key        = key
        self.value      = value
        self.leftchild  = leftchild
        self.rightchild = rightchild

# For the tree rooted at root:
# Return the json.dumps of the list with indent=2.
# DO NOT MODIFY!
def dump(root: Node) -> str:
    def _to_dict(node) -> dict:
        return {
            "key"        : node.key,
            "value"      : node.value,
            "leftchild"  : (_to_dict(node.leftchild) if node.leftchild is not None else None),
            "rightchild" : (_to_dict(node.rightchild) if node.rightchild is not None else None)
        }
    if root == None:
        dict_repr = {}
    else:
        dict_repr = _to_dict(root)
    return json.dumps(dict_repr,indent = 2)

# For the tree rooted at root and the key and value given:
# Insert the key/value pair.
# The key is guaranteed to not be in the tree.
def insert(root: Node, key: int, value: int) -> Node:
    node = Node(key = key, value = value)
    if root == None:
        return node

    prev = None
    current = root

    while current != None:
        prev = current

        if current.key > key:
            current = current.leftchild
        else:
            current = current.rightchild
    
    if prev.key > key:
        prev.leftchild = node
    else:
        prev.rightchild = node
            

    return root

# For the tree rooted at root and the key given, delete the key.
# When replacement is necessary use the inorder successor.
def delete(root: Node, key: int) -> Node:
    def find_inorder_successor(node):
        current = node
        while current.leftchild != None:
            current = current.leftchild
        return current

    if root == None:
        return None
    
    if key < root.key:
        root.leftchild = delete(root.leftchild,key)
    elif key > root.key:
        root.rightchild = delete(root.rightchild,key)
    else:
        if root.leftchild == None:
            return root.rightchild
        
        elif root.rightchild == None:
            return root.leftchild

            
        temp = find_inorder_successor(root.rightchild)
        root.key = temp.key
        root.value = temp.value
        root.rightchild = delete(root.rightchild, temp.key)

    return root

# For the tree rooted at root and the key given:
# Calculate the list of values on the path from the root down to and including the search key node.
# The key is guaranteed to be in the tree.
# Return the json.dumps of the list with indent=2.
def search(root: Node, search_key: int) -> str:
    # Remove the next line and fill in code to construct value_list.

    value_list = []
    current = root
    while current.key != search_key:
        value_list.append(current.value)
        if current.key > search_key:
            current = current.leftchild
        else:
            current = current.rightchild

    value_list.append(current.value)

    return json.dumps(value_list,indent = 2)

# Restructure the tree..
def restructure(root: Node):

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
        root.rightchild = construct(pairs[mid+1:])
        return root
    
       
    # Remove the next line and fill in code to restructure and assign the newroot.
    pairs = in_order_traverse(root)
    newroot = construct(pairs=pairs)
    return(newroot)