"""
Author: Cameron Britton, John Requizo
"""
from __future__ import annotations
from typing import Any
from node import Node


class BNode(Node):
    """ Binomial Node Class specific for Binomial Heaps and Binomial Trees

    BNode inherits from Node Class
    """

    
    def __init__(self, key:Any, degree:int, left:Node|None=None, right:Node|None=None, parent:Node|None=None):
        """ Construct a Binary Node Object

        Args:
            key (Any): Key or value of the Binomial node
            degree (int): Degree of the Binomial Node
            left (Node | None, optional): Left pointer to another Node Object. Defaults to None.
            right (Node | None, optional): Right pointer to another Node Object. Defaults to None.
            parent (Node | None, optional): Parent pointer to another Node Object. Defaults to None.
        """
        super().__init__(key, left, right)
        self.degree = degree
        self.parent = parent

        
    @property
    def parent(self) -> Node|None:
        """ Get the parent of the Binomial Node

        Returns:
            Node|None: The parent of the Binomial Node
        """
        return self.__parent

        
    @parent.setter
    def parent(self, parent:Node|None) -> None:
        """ Set the parent of the Binomial Node.

        Args:
            parent (Node | None): Parent of the Binomial Node.

        Raises:
            TypeError: Parent has to be of type Node or it's subclasses or None.
        """
        if not isinstance(parent, Node) or not isinstance(parent, None):
            raise TypeError(f"Expected {self.__class__.__name__} but was given {parent.__class__.__name__}")
        self.__parent = parent

        
    @property
    def degree(self) -> int:
        """ Get the degree of the Binomial Node

        Returns:
            int: The degree of the Binomial Node
        """
        return self.__degree

        
    @degree.setter
    def degree(self, degree:int) -> None:
        """ Set the degree of the Binomial Node

        Args:
            degree (int): The degree of the Binomial Node

        Raises:
            TypeError: _description_
        """
        if not isinstance(degree, int):
            raise TypeError(f"Expected degree to be of int type but was given {degree.__class__.name}")
        if degree < 0:
            raise ValueError("The degree of a Binomial Node cannot be less than zero.")
        self.__degree = degree

        
    @property
    def child(self) -> Node | None:
        """ Get the child (left node) of the Binomial Node.

        For readability, this getter uses self.left property getter as
        the child is equivalent to the left node.

        Returns:
            Node | None: The child (left node) of the Binomial Node 
        """
        return self.left

        
    @child.setter
    def child(self, child: Node | None) -> None:
        """ Set the child (left node) of the Binomial Node.

        For readability, this setter uses self.left property setter as
        the child is equivalent to the left node.

        Args:
            child (Node | None): The child node.
        """
        self.left = child

        
    @property
    def sibling(self) -> Node | None:
        """ Get the sibling (right node) of the Binomial Node.

        For readability, this getter uses self.right property getter as
        the sibling is equivalent to the right node.

        Returns:
            Node | None: The sibling (right node) of the Binomial Node 
        """
        return self.right

        
    @sibling.setter
    def sibling(self, sibling:Node|None) -> None:
        """ Set the sibling (right node) of the Binomial Node.

        For readability, this setter uses self.right property setter as
        the sibling is equivalent to the right node.

        Args:
            sibling (Node | None): The sibling node.
        """
        self.right = sibling

        
    def __repr__(self) -> str:
        return f"BinomialNode(key={self.key}, degree={self.degree}"
