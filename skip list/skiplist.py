from __future__ import annotations
import json
import math
from typing import List

verbose = False

# DO NOT MODIFY!
class Node():
    def  __init__(self,
                  key      : int,
                  value    : str,
                  toplevel : int,
                  pointers : List[Node] = None):
        self.key      = key
        self.value    = value
        self.toplevel = toplevel
        self.pointers = pointers

# DO NOT MODIFY!
class SkipList():
    def  __init__(self,
                  maxlevel : int = None,
                  nodecount: int = None,
                  headnode : Node = None,
                  tailnode : Node = None):
        self.maxlevel = maxlevel
        self.nodecount = nodecount
        self.headnode  = headnode
        self.tailnode  = tailnode

    # DO NOT MODIFY!
    # Return a reasonable-looking json.dumps of the object with indent=2.
    # We create an list of nodes,
    # For each node we show the key, the value, and the list of pointers and the key each points to.
    def dump(self) -> str:
        currentNode = self.headnode
        nodeList = []
        while currentNode is not self.tailnode:
            pointerList = str([n.key for n in currentNode.pointers])
            nodeList.append({'key':currentNode.key,'value':currentNode.value,'pointers':pointerList})
            currentNode = currentNode.pointers[0]
        pointerList = str([None for n in currentNode.pointers])
        nodeList.append({'key':currentNode.key,'value':currentNode.value,'pointers':pointerList})
        return json.dumps(nodeList,indent = 2)

    # DO NOT MODIFY!
    # Creates a pretty rendition of a skip list.
    # It's vertical rather than horizontal in order to manage different lengths more gracefully.
    # This will never be part of a test but you can put "pretty" as a single line in your tracefile
    # to see what the result looks like.
    def pretty(self) -> str:
        currentNode = self.headnode
        longest = 0
        while currentNode != None:
            if len(str(currentNode.key)) > longest:
                longest = len(str(currentNode.key))
            currentNode = currentNode.pointers[0]
        longest = longest + 2
        pretty = ''
        currentNode = self.headnode
        while currentNode != None:
            lineT = 'Key = ' + str(currentNode.key) + ', Value = ' + str(currentNode.value)
            lineB = ''
            for p in currentNode.pointers:
                if p is not None:
                    lineB = lineB + ('('+str(p.key)+')').ljust(longest)
                else:
                    lineB = lineB + ''.ljust(longest)
            pretty = pretty + lineT
            if currentNode != self.tailnode:
                pretty = pretty + "\n"
                pretty = pretty + lineB + "\n"
                pretty = pretty + "\n"
            currentNode = currentNode.pointers[0]
        return(pretty)

    # DO NOT MODIFY!
    # Initialize a skip list.
    # This constructs the headnode and tailnode each with maximum level maxlevel.
    # Headnode has key -inf, and pointers point to tailnode.
    # Tailnode has key inf, and pointers point to None.
    # Both have value None.
    def initialize(self,maxlevel):
        pointers = [None] * (1+maxlevel)
        tailnode = Node(key = float('inf'),value = None,toplevel = maxlevel,pointers = pointers)
        pointers = [tailnode] * (maxlevel+1)
        headnode = Node(key = float('-inf'),value = None, toplevel = maxlevel,pointers = pointers)
        self.headnode = headnode
        self.tailnode = tailnode
        self.maxlevel = maxlevel

    # Create and insert a node with the given key, value, and toplevel.
    # The key is guaranteed to not be in the skiplist.
    # Check if we need to rebuild and do so if needed.
    def insert(self,key,value,toplevel):
        if self.nodecount == None:
            self.initialize(maxlevel=self.maxlevel)
            self.nodecount = 0
        
        #perform searhing:
        node = Node(key = key,value = value,toplevel=toplevel, pointers= [None] * (1+toplevel))
        bound1 = self.headnode
        bound2 = self.tailnode

        in_table = [self.headnode]*(toplevel + 1)
        out_table = [self.tailnode]*(toplevel + 1)

        while bound1.pointers[0] != bound2:
 
            for i in range(len(bound1.pointers) - 1, -1,-1):
                # if(key ==49):
                #     print("intable of", key)
                #     print(", ".join(str(a.key) for a in in_table))
                if bound1.pointers[i].key < key:
                    bound1 = bound1.pointers[i]

                    in_table = [bound1]*(i+1) + in_table[i+2:]
                    in_table = in_table[:toplevel+2]

                    break

                if  bound1.pointers[i].key > key and bound1.pointers[i].key < bound2.key:
                    bound2 = bound1.pointers[i]

                    out_table = [bound2] * (i+1) + out_table[i+2:]
                    out_table = out_table[:toplevel+2]
                    break


        # for i in range(len(out_table)):
        #     print("outtable",out_table[i].key)
        
        node.pointers = out_table
        for i in range(len(in_table)):
            in_table[i].pointers[i] = node
        # if(key ==49):
        #     print("intable of", key)
        #     print(", ".join(str(a.key) for a in in_table))

        self.nodecount += 1

        if 1 + math.log2(self.nodecount) > self.maxlevel:
            # print("rebuild at", key)
            self.rebuild()
        
    def rebuild(self):
        def get_level(i):
            level = 0
            while i % 2 == 0 and level <= self.maxlevel:
                level += 1
                i //= 2
            return level

        pointer_list = []
        new_maxlevel = 2 * self.maxlevel
        current = self.headnode

        while current.key != float('inf'):
            # print(current.key)
            pointer_list.append((current.key,current.value))
            current = current.pointers[0]

        pointer_list = pointer_list[1:]

        self.maxlevel = new_maxlevel
        self.headnode = None
        self.tailnode = None
        self.nodecount = None
        for i in range(len(pointer_list)):
            level = get_level(i+1)
            # print("level",level)
            # print(pointer_list[i][0])
            self.insert(key= pointer_list[i][0],value = pointer_list[i][1],toplevel= level)

        
        return


    # Delete node with the given key.
    # The key is guaranteed to be in the skiplist.
    def delete(self,key):
        print('Placeholder')

    # Search for the given key.
    # Construct a list of all the keys in all the nodes visited during the search.
    # Append the value associated to the given key to this list.
    def search(self,key) -> str:
        A = ['your list gets constructed here']
        return json.dumps(A,indent = 2)

# s = SkipList(maxlevel=2)
# s.insert(key = 48,value= "1",toplevel= 0)
# s.insert(key =2,value= "1",toplevel=2)
# s.insert(key =49,value= "1",toplevel=2)
# s.insert(key =22,value= "1",toplevel=0)
# print(s.dump())