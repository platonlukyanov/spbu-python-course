from typing import Any, Iterable, Iterator, KeysView, MutableMapping

from .binary_search_tree import BinarySearchTree
from collections import namedtuple

KeyValuePair = namedtuple("KeyValuePair", ["key", "value"])


class HashTable(MutableMapping):
    """
    HashTable implemented using a binary search tree for storage of hashed keys.

    Example usage:
    >>> table = HashTable()
    >>> table['example'] = 1
    >>> table['example']
    1
    >>> del table['example']
    >>> 'example' in table
    False
    """

    def __init__(self, initial_elements: list[tuple[Any, Any]] = []):
        """
        Initializes the HashTable.

        Args:
            initial_elements (list[tuple[Any, Any]], optional): List of (key, value) pairs to initialize the table with.

        The initial elements will be inserted into the hash table.
        """
        self.bst: BinarySearchTree[int, KeyValuePair] = BinarySearchTree()

        self.size = len(initial_elements)

        for key, value in initial_elements:
            self[key] = value

    def __getitem__(self, key: Any) -> Any | None:
        """
        Gets the element by key.

        Args:
            key (Any): Key to lookup.

        Raises:
            KeyError: If key is not found.

        Returns:
            Any: The value associated with the key.

        Example:
            >>> table['example']
        """
        found = self.bst.search(hash(key))
        if found is None:
            raise KeyError(key)
        return found.value.value

    def __setitem__(self, key: Any, value: Any):
        """
        Sets the element by key.

        Args:
            key (Any): Key to insert or update.
            value (Any): Value to associate with the key.

        Example:
            >>> table['example'] = 1
        """
        if key in self:
            self.bst.update(hash(key), KeyValuePair(key, value))
        else:
            self.bst.insert(hash(key), KeyValuePair(key, value))
            self.size += 1

    def __delitem__(self, key: Any):
        """
        Deletes the element by key.

        Args:
            key (Any): Key of the element to delete.

        Raises:
            KeyError: If key is not found.

        Example:
            >>> del table['example']
        """
        self.bst.delete(hash(key))
        self.size -= 1

    def __iter__(self) -> Iterator[KeyValuePair]:
        """
        Iterates over the elements in the table.

        Yields:
            Iterator[KeyValuePair]: KeyValuePair objects of entries in the table.
        """
        for element in self.bst.forward_iterator():
            yield element.value

    def __len__(self) -> int:
        """
        Returns the number of elements in the table.

        Returns:
            int: Count of elements.
        """
        return self.size

    def __contains__(self, key: Any) -> bool:
        """
        Checks if the table contains the given key.

        Args:
            key (Any): Key to check existence of.

        Returns:
            bool: True if key exists, else False.
        """
        return self.bst.search(hash(key)) is not None

    def __eq__(self, other: object) -> bool:
        """
        Checks if two hash tables are equal.

        Args:
            other (object): Other object to compare.

        Returns:
            bool: True if both are HashTable and have equal BST structures.
        """
        if not isinstance(other, HashTable):
            return False

        return self.bst == other.bst

    def keys(self):
        """
        Returns an iterator over the keys of the table.

        Yields:
            Iterator[Any]: Keys stored in the hash table.
        """
        for key_value_pair in self.bst:
            yield key_value_pair.value.key

    def values(self):
        """
        Returns an iterator over the values of the table.

        Yields:
            Iterator[Any]: Values stored in the hash table.
        """
        for key_value_pair in self.bst:
            yield key_value_pair.value.value

    def items(self):
        """
        Returns an iterator over the (key, value) pairs in the table.

        Yields:
            Iterator[tuple[Any, Any]]: Key-value pairs stored in the hash table.
        """
        for key_value_pair in self.bst:
            yield (key_value_pair.value.key, key_value_pair.value.value)

    def clear(self):
        """
        Clears all elements from the hash table.
        Resets the internal binary search tree and size to zero.
        """
        for key in self.keys():
            del self[key]
