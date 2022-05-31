
""" 
Authors: Cameron Britton, John Emerson Requizo
"""
from __future__ import annotations
from typing import Any

from numpy import isin


class Node:
    """ Node Class specific for Binomial Heaps
    """
    def __init__(self, key:Any, left:Node|None=None, right:Node|None=None) -> Node:
        """ Construct a Node object
        
        The node object must have a key and degree during instantiation

        Args:
            key (Any): The key of the Node
            left (Node | None, optional): Left Pointer to another Node Object. Defaults to None.
            right (Node | None, optional): Right Pointer to another Node Object. Defaults to None.
        """
        self.key = key
        self.left = left  # Child/Left is a pointer to the left node
        self.right = right # Sibling/Right is a pointer to the right node

        
    @property
    def left(self) -> Node:
        """ Get the left node.

        Returns:
            Node: The left Node
        """
        return self.__left

    
    @left.setter
    def left(self, left:Node|None):
        """ Set the left node.

        Args:
            left (Node | None): The left node

        Raises:
            TypeError: left has to be of type Node or None.
        """
        if not isinstance(left, Node) or not isinstance(left, None):
            raise TypeError(f"Expected {self.__class__.__name__} but was given {left.__class__.__name__}")
        self.__left = left

        
    @property
    def right(self) -> Node:
        """ Get the right node.

        Returns:
            Node: The right node
        """
        return self.__right

        
    @right.setter
    def right(self, right:Node|None):
        """ Set the right node.

        Args:
            right (Node | None):  The right node.

        Raises:
            TypeError: right has to be of type Node or None.
        """
        if not isinstance(right, Node) or not isinstance(right, Node):
            raise TypeError(f"Expected {self.__class__.__name__} but was given {right.__class__.__name__}")
        self.__right = right

        
    def __eq__(self, other):
        return self.key == other.key

        
    def __ne__(self, other):
        return self.key != other.key

    
    def __lt__(self, other):
        return self.key < other.key

        
    def __le__(self, other):
        return self.key <= other.key


    def __gt__(self, other):
        return self.key > other.key

        
    def __ge__(self, other):
        return self.key >= other.key

        
    def __repr__(self):
        return f"Node (key={self.key},degree={self.degree})"

        