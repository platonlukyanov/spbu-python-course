from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, Iterator, Literal, Optional, TypeVar, Protocol


class Comparable(Protocol):
    """Class that represents a comparable object."""

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
    """Data Strucure for a node in Binary Search Tree

    Generic (<some comparatible type>, <value type>): Custom type for the key and value
    """

    key: T
    value: U
    left: Optional[Node] = None
    right: Optional[Node] = None

    def __str__(self):
        """Returns a string representation of the node"""
        return f"Node({self.key})"

    def __repr__(self):
        """Returns a representation of the node"""
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
        """Inserts a new node with (key, value) to the tree

        Args:
            key (T): key in a bst
            value (U): value that is attached to the key
            root (Node[T, U] | None | Literal[&quot;root&quot;], optional): _description_. Defaults to "root". - Start node (most likely you will not use it, it is more for internal purposes)

        Returns:
            Node[T, U]: node that was inserted with set key and value
        """
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
        """Searches for an element in the binary search tree

        Args:
            key (T): node key that needs to be found
            root (Node[T, U] | None | Literal[&quot;root&quot;], optional): Start node (mostly for internal purposes). Defaults to "root".

        Returns:
            Node[T, U] | None: found node
        """
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
        """
        Returns the maximum node in the binary search tree.

        Args:
            root (Node[T, U] | None | Literal["root"], optional):
                The node to start searching from (default is the root).

        Raises:
            ValueError: If the tree is empty.

        Returns:
            Node[T, U]: The node with the maximum key in the tree.
        """
        node: Node[T, U] | None = self.root if root == "root" else root
        if node is None:
            raise ValueError("Tree is empty")

        if node.right == None:
            return node

        return self.max(node.right)

    def delete(self, key: T) -> Node[T, U] | None:
        """
        Deletes the node with the given key from the binary search tree.

        Args:
            key (T): The key of the node to delete.

        Returns:
            Node[T, U] | None: The root of the updated tree after deletion.
        """
        self.root = self._delete_node(key, "root")

        return self.root

    def _delete_node(
        self, key: T, root: Node[T, U] | None | Literal["root"] = "root"
    ) -> Node[T, U] | None:
        """
        Internal helper method to delete a node by key from the tree.

        Args:
            key (T): The key of the node to delete.
            root (Node[T, U] | None | Literal["root"], optional):
                Node to start from (default is the root).

        Returns:
            Node[T, U] | None: Updated subtree root after deletion.
        """
        node: Node[T, U] | None = self.root if root == "root" else root

        if node is None:
            return node

        if key < node.key:
            node.left = self._delete_node(key, node.left)
        elif key > node.key:
            node.right = self._delete_node(key, node.right)
        elif node.left != None and node.right != None:
            node.key = self.min(node.right).key
            node.right = self._delete_node(node.key, node.right)
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
        """
        Returns an iterator that traverses the tree in forward order (pre-order traversal).

        Args:
            root (Node[T, U] | None | Literal["root"], optional):
                Node to start the iteration from (default is root).

        Yields:
            Iterator[Node[T, U]]: Nodes in forward traversal order.
        """
        node: Node[T, U] | None = self.root if root == "root" else root
        if node is not None:
            yield node
            while node.left is not None:
                node = node.left
                yield node
            while node.right is not None:
                node = node.right
                yield node

    def forward_list(self) -> list[Node[T, U]]:
        """
        Returns a list that traverses the tree in forward order (pre-order traversal).

        Returns:
            list[Node[T, U]]: Nodes in forward traversal order.

        """
        return list(self.forward_iterator())

    def backward_iterator(self) -> Iterator[Node[T, U]]:
        """
        Returns an iterator that traverses the tree in backward order (reverse of forward iterator).

        Yields:
            Iterator[Node[T, U]]: Nodes in backward traversal order.
        """
        nodes = []
        for node in self.forward_iterator():
            nodes.append(node)

        for node in nodes[::-1]:
            yield node

    def __eq__(self, value: object) -> bool:
        """
        Compares this binary search tree with another for equality.

        Args:
            value (object): Another object to compare with.

        Returns:
            bool: True if both trees have the same structure and node keys/values, False otherwise.
        """
        if not isinstance(value, BinarySearchTree):
            return False

        return self.root == value.root

    def equals(self, value: object) -> bool:
        """
        Compares this binary search tree with another for equality. (mirror of __eq__)

        Args:
            value (object): Another object to compare with.

        Returns:
            bool: True if both trees have the same structure and node keys/values, False otherwise.
        """
        if not isinstance(value, BinarySearchTree):
            return False

        return self.root == value.root

    def __iter__(self) -> Iterator[Node[T, U]]:
        """
        Iterates over the nodes of the tree in forward order.

        Returns:
            Iterator[Node[T, U]]: Forward iterator over the tree nodes.
        """
        return self.forward_iterator()

    def __reversed__(self) -> Iterator[Node[T, U]]:
        """
        Iterates over the nodes of the tree in backward order.

        Returns:
            Iterator[Node[T, U]]: Backward iterator over the tree nodes.
        """
        return self.backward_iterator()
