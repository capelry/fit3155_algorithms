"""
Author: Cameron Britten, John Requizo

Week 7 - Generalised B Trees
"""
from __future__ import annotations
from typing import Any

class BTreeNode:
    def __init__(self, degree : int, is_leaf : bool = True):
        self.keys = []
        self.degree = degree
        self.is_leaf = is_leaf
        self.child_pointers : BTreeNode = BTreeNode(degree)
        self.l_bound = degree - 1
        self.u_bound = degree * 2 - 1
        self.no_of_keys = 0


class BTree:
    """ Generalised B Tree Class implementation
    """
    def __int__(self, degree:int, is_leaf:bool=True) -> BTree:
        if degree < 2:
            raise ValueError("Degree of a B Tree cannot be less than zero")
        self.l_bound = degree - 1
        self.u_bound = 2 * degree - 1
        self.is_leaf = is_leaf
        self.node_list = []

        
    def insert(self, value:Any) -> None:
        n = Node(value)
        is_full = True if len(self.node_list) >= self.u_bound else False
        if self.is_leaf:
            if is_full:
                # Split the B Tree node
                pass
            else:
                # Insert
                pass
            pass
        else:
            pass
        if not self.node_list and self.is_leaf and not is_full:
            self.node_list.append(n)
            return

        if not self.is_leaf:
            pass
            
        pass