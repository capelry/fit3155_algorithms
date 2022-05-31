from __future__ import annotations
from .node import Node
from typing import Any

class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0


    @property
    def head(self) -> Node | None:
        """ Get the Node pointed by the head pointer.

        Returns:
            Node | None: The node pointed by the head pointer.
        """
        return self.__head


    @property
    def tail(self) -> Node | None:
        """ Get the Node pointed by the tail pointer.

        Returns:
            Node | None: The node pointed by the tail pointer.
        """
        return self.__tail

        
    def __len__(self) -> int:
        return self.__count


class SinglyLinkedList(LinkedList):
    def __init__(self) -> SinglyLinkedList:
        super.__init__()


    def append(self, value:Any) -> None:
        """ Append a value into the Singly Linked List.

        Args:
            value (Any): A value to append into the Singly Linked List.
        """
        new_node = Node(value)
        if self.head is None and self.tail is None:
            new_node.right = None
            self.head = new_node
            self.tail = new_node
            return
        
        prev_node = self.tail
        prev_node.right = new_node
        new_node.right = None
        self.tail = new_node
        self.__count += 1

        
class DoublyLinkedList(LinkedList):
    def __init__(self):
        super.__init__()