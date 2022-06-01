"""
Author: Cameron Britten, John Requizo

Week 7 - Generalised B Trees
"""
from __future__ import annotations


class BTree:
    """ Generalised B Tree Class implementation
    """
    def __int__(self, degree:int) -> BTree:
        if degree < 2:
            raise ValueError("Degree of a B Tree cannot be less than zero")
        self.l_bound = degree - 1
        self.u_bound = 2 * degree - 1
        self.node_list = []