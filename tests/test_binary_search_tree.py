from project.homework_5.binary_search_tree import BinarySearchTree


def test_binary_search_tree_initialization():
    bst = BinarySearchTree()
    assert bst.root is None


def test_insert_and_search():
    bst = BinarySearchTree()
    bst.insert(1, 1)
    assert bst.search(1).value == 1


def test_multiple_inserts():
    bst = BinarySearchTree()
    bst.insert(1, 1)
    bst.insert(2, 2)
    bst.insert(3, 3)
    bst.insert(4, 4)
    assert bst.search(2).value == 2
    assert bst.search(3).value == 3
    assert bst.search(4).value == 4


def test_update():
    bst = BinarySearchTree()
    bst.insert(1, 1)
    bst.insert(2, 2)
    bst.insert(3, 3)
    bst.insert(4, 4)
    bst.update(2, 22)
    assert bst.search(2).value == 22
    assert bst.search(3).value == 3
    assert bst.search(4).value == 4


def test_min():
    bst = BinarySearchTree()
    bst.insert(1, 1)
    bst.insert(2, 2)
    bst.insert(3, 3)
    bst.insert(4, 4)
    assert bst.min().value == 1


def test_delete():
    bst = BinarySearchTree()
    bst.insert(1, 1)
    bst.insert(2, 2)
    bst.insert(3, 3)
    bst.insert(4, 4)
    bst.delete(2)
    assert bst.search(2) is None
    assert bst.search(3).value == 3
    assert bst.search(4).value == 4


def test_forward_iterator():
    bst = BinarySearchTree()
    bst.insert(1, 1)
    bst.insert(2, 2)
    bst.insert(3, 3)
    bst.insert(4, 4)
    assert list(map(lambda x: x.value, list(bst.forward_iterator()))) == [1, 2, 3, 4]


def test_backward_iterator():
    bst = BinarySearchTree()
    bst.insert(1, 1)
    bst.insert(2, 2)
    bst.insert(3, 3)
    bst.insert(4, 4)
    assert list(map(lambda x: x.value, list(bst.backward_iterator()))) == [4, 3, 2, 1]


def test_equality():
    bst1 = BinarySearchTree()
    bst1.insert(1, 1)
    bst1.insert(2, 2)
    bst1.insert(3, 3)
    bst1.insert(4, 4)

    bst2 = BinarySearchTree()
    bst2.insert(1, 1)
    bst2.insert(2, 2)
    bst2.insert(3, 3)
    bst2.insert(4, 4)

    assert bst1 == bst2


def test_inequality():
    bst1 = BinarySearchTree()
    bst1.insert(1, 1)
    bst1.insert(2, 2)
    bst1.insert(3, 3)
    bst1.insert(4, 4)

    bst2 = BinarySearchTree()
    bst2.insert(1, 1)
    bst2.insert(2, 2)
    bst2.insert(3, 3)
    bst2.insert(5, 5)

    assert bst1 != bst2


def test_delete_all_nodes():
    bst = BinarySearchTree()
    bst.insert(1, 1)
    bst.insert(2, 2)
    bst.insert(3, 3)
    bst.insert(4, 4)
    bst.delete(2)
    bst.delete(3)
    bst.delete(1)
    assert bst.search(1) is None
    assert bst.search(3) is None
    assert bst.search(2) is None
