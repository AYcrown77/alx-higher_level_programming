#!/usr/bin/python3
"""Define classes for a singly-linked list"""


class Node:
    """Represent a node in a singly-linked list"""

    def __init__(self, data, next_node=None);
    """Initialize a new node

    Args:
        data (int): The data of the new Node
        next_node (Node): The next ofthe new Node.
    """
    self.data = data
    self.next_node = next_node

    @property
    def data(self):
        """Get/set the data of the Node"""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/set the next_node of the Node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """sets node"""
        if value is not None and type(value) != Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


    class SinglyLinkedList:
        """define a sll"""

        def __init__(self):
            """this is init"""
            self.head = None

        def __str__(self):
            """teach python to print my way
            Returns: the printed thing"""
            printsll = ""
            location = self.head
            while location:
                printsll += str(location.data) + "\n"
                location = location.next_node
            return printsll[:-1]

        def sorted_insert(self, value):
            """insert in a sorted fashion
            Args:
                value: what the value will be on the node
            """
            new = Node(value)
            if not self.head:
                self.head = new
                return
            if value < self.head.data:
                new.next_node = self.head
                self.head = new
                return
            location = self.head
            while location.next_node and location.next_node.data < value:
                location = location.next_node
            if location.next_node:
                new.next_node = location.next_node
            location.next_node = new
