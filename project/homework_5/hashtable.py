from typing import Any, Iterable, Iterator, KeysView, MutableMapping

from .binary_search_tree import BinarySearchTree
from collections import namedtuple

KeyValuePair = namedtuple("KeyValuePair", ["key", "value"])


class HashTable(MutableMapping):
    def __init__(self, initial_elements: list[tuple[Any, Any]] = []):
        self.bst: BinarySearchTree[int, KeyValuePair] = BinarySearchTree()

        self.size = len(initial_elements)

        for key, value in initial_elements:
            self[key] = value
            # self.bst.insert(hash(key), KeyValuePair(key, value))

    def __getitem__(self, key: Any) -> Any | None:
        """
        Gets the element. Example:
        >>> table['example']
        """
        found = self.bst.search(hash(key))
        if found is None:
            raise KeyError(key)
        return found.value.value

    def __setitem__(self, key: Any, value: Any):
        """
        Sets the element. Example:
        >>> table['example'] = 1
        """
        if key in self:
            self.bst.update(hash(key), KeyValuePair(key, value))
        else:
            self.bst.insert(hash(key), KeyValuePair(key, value))
            self.size += 1

    def __delitem__(self, key: Any):
        """
        Deletes the element. Example:
        >>> del table['example']
        """
        self.bst.delete(hash(key))
        self.size -= 1

    def __iter__(self) -> Iterator[KeyValuePair]:
        """Iterates over the elements in the table"""
        for element in self.bst.forward_iterator():
            yield element.value

    def __len__(self) -> int:
        """Returns the number of elements in the table"""
        return self.size

    def __contains__(self, key: Any) -> bool:
        """Checks if the table contains the given key"""
        return self.bst.search(hash(key)) is not None

    def __eq__(self, other: object) -> bool:
        """Checks if two hash tables are equal"""
        if not isinstance(other, HashTable):
            return False

        return self.bst == other.bst

    def keys(self):
        """Returns an iterator over the keys of the table"""
        for key_value_pair in self.bst:
            yield key_value_pair.value.key

    def values(self):
        for key_value_pair in self.bst:
            yield key_value_pair.value.value

    def items(self):
        for key_value_pair in self.bst:
            yield (key_value_pair.value.key, key_value_pair.value.value)


if __name__ == "__main__":
    table = HashTable([("1", 5), ("2", 6), ("3", 7)])
    print(list(table.keys()))
