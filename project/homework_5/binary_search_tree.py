from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, Iterator, Literal, Optional, TypeVar, Protocol


class Comparable(Protocol):
    def __lt__(self: T, other: T) -> bool:
        pass

    def __le__(self: T, other: T) -> bool:
        pass

    def __gt__(self: T, other: T) -> bool:
        pass


T = TypeVar("T", bound=Comparable)
U = TypeVar("U")


@dataclass
class Node(Generic[T, U]):
    key: T
    value: U
    left: Optional[Node] = None
    right: Optional[Node] = None
    parent: Optional[Node] = None

    def __str__(self):
        return f"Node({self.key})"

    def __repr__(self):
        return f"Node({self.key})"


class BinarySearchTree(Generic[T, U]):
    """
    Class that represents a binary search tree \n
    Example usage:
    >>> bst = BinarySearchTree()
    >>> bst.insert(1, 1) # inserts 1 into the tree
    >>> bst.insert(2, 2)
    >>> bst.insert(3, 3)
    >>> bst.insert(4, 4)
    >>> bst.search(2) # returns Node(2)
    >>> bst.search(5) # returns None
    >>> bst.update(2, 22) # updates the value of the node with the given key in the binary search tree
    >>> bst.min() # returns Node(1)
    >>> bst.delete(2) # deletes the node with the given key from the binary search tree
    >>> bst.delete(5) # returns None
    """

    def __init__(self):
        """Initializes binary search tree with empty root node"""
        self.root = None

    def insert(
        self, key: T, value: U, root: Node[T, U] | None | Literal["root"] = "root"
    ) -> Node[T, U]:
        """Inserts an element into the binary search tree"""
        node: Node[T, U] | None = self.root if root == "root" else root

        if node is None:
            node = Node(key, value)
        elif key < node.key:
            node.left = self.insert(key, value, node.left)
        else:
            node.right = self.insert(key, value, node.right)

        if root == "root":
            self.root = node

        return node

    def search(
        self, key: T, root: Node[T, U] | None | Literal["root"] = "root"
    ) -> Node[T, U] | None:
        """Searches for an element in the binary search tree"""
        node: Node[T, U] | None = self.root if root == "root" else root

        if node is None or key == node.key:
            return node

        if key < node.key:
            return self.search(key, node.left)
        else:
            return self.search(key, node.right)

    def update(
        self, key: T, newValue: U, root: Node[T, U] | None | Literal["root"] = "root"
    ) -> Node[T, U] | None:
        """Updates the value of the node with the given key in the binary search tree"""
        foundNode = self.search(key, root)

        if foundNode is None:
            raise ValueError("Node not found")

        foundNode.value = newValue
        return foundNode

    def min(self, root: Node[T, U] | None | Literal["root"] = "root") -> Node[T, U]:
        """Returns the minimum node in the binary search tree"""
        node: Node[T, U] | None = self.root if root == "root" else root
        if node is None:
            raise ValueError("Tree is empty")

        if node.left == None:
            return node

        return self.min(node.left)

    def max(self, root: Node[T, U] | None | Literal["root"] = "root") -> Node[T, U]:
        """Returns the maximum node in the binary search tree"""
        node: Node[T, U] | None = self.root if root == "root" else root
        if node is None:
            raise ValueError("Tree is empty")

        if node.right == None:
            return node

        return self.max(node.right)

    def delete(
        self, key: T, root: Node[T, U] | None | Literal["root"] = "root"
    ) -> Node[T, U] | None:
        """Deletes the node with the given key from the binary search tree"""
        node: Node[T, U] | None = self.root if root == "root" else root

        if node is None:
            return node

        if key < node.key:
            node.left = self.delete(key, node.left)
        elif key > node.key:
            node.right = self.delete(key, node.right)
        elif node.left != None and node.right != None:
            node.key = self.min(node.right).key
            node.right = self.delete(node.key, node.right)
        else:
            if node.left != None:
                node = node.left
            elif node.right != None:
                node = node.right
            else:
                node = None

        return node

    def forward_iterator(
        self, root: Node[T, U] | None | Literal["root"] = "root"
    ) -> Iterator[Node[T, U]]:
        """Returns an iterator that traverses the tree in a forward direction"""
        node: Node[T, U] | None = self.root if root == "root" else root
        if node is not None:
            yield node
            while node.left is not None:
                node = node.left
                yield node
            while node.right is not None:
                node = node.right
                yield node

    def backward_iterator(self) -> Iterator[Node[T, U]]:
        """Returns an iterator that traverses the tree in a backward direction"""
        nodes = []
        for node in self.forward_iterator():
            nodes.append(node)

        for node in nodes[::-1]:
            yield node

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, BinarySearchTree):
            return False

        return self.root == value.root

    def __iter__(self) -> Iterator[Node[T, U]]:
        return self.forward_iterator()
