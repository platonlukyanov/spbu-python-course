from project.homework_5.hashtable import HashTable


def test_hashtable_initialization():
    table = HashTable()
    assert list(table.keys()) == []
    assert list(table.values()) == []


def test_hashtable_insert():
    table = HashTable()
    table[1] = 5
    assert list(table.keys()) == [1]
    assert list(table.values()) == [5]
    assert table[1] == 5


def test_hashtable_insert_multiple():
    table = HashTable()
    table[1] = 5
    table[2] = 6
    table[3] = 7
    assert list(table.keys()) == [1, 2, 3]
    assert list(table.values()) == [5, 6, 7]
    assert table[1] == 5
    assert table[2] == 6
    assert table[3] == 7


def test_hashtable_update():
    table = HashTable()
    table[1] = 5
    table[2] = 6
    table[3] = 7
    table[1] = 11
    assert list(table.keys()) == [1, 2, 3]
    assert list(table.values()) == [11, 6, 7]
    assert table[1] == 11
    assert table[2] == 6
    assert table[3] == 7


def test_hashtable_delete():
    table = HashTable()
    table[1] = 5
    table[2] = 6
    table[3] = 7
    del table[2]
    assert list(table.keys()) == [1, 3]
    assert list(table.values()) == [5, 7]
    assert table[1] == 5
    assert table[3] == 7


def test_hashtable_iteration():
    table = HashTable()
    table[1] = 5
    table[2] = 6
    table[3] = 7
    assert list(table.items()) == [(1, 5), (2, 6), (3, 7)]


def test_hashtable_equality():
    table1 = HashTable()
    table1[1] = 5
    table1[2] = 6
    table1[3] = 7

    table2 = HashTable()
    table2[1] = 5
    table2[2] = 6
    table2[3] = 7

    assert table1 == table2


def test_hashtable_inequality():
    table1 = HashTable()
    table1[1] = 5
    table1[2] = 6
    table1[3] = 7

    table2 = HashTable()
    table2[1] = 5
    table2[2] = 6
    table2[3] = 8

    assert table1 != table2


def test_hashtable_keys():
    table = HashTable()
    table[1] = 5
    table[2] = 6
    table[3] = 7
    assert list(table.keys()) == [1, 2, 3]


def test_hashtable_values():
    table = HashTable()
    table[1] = 5
    table[2] = 6
    table[3] = 7
    assert list(table.values()) == [5, 6, 7]


def test_hashtable_initial_elements():
    table = HashTable([(1, 5), (2, 6), (3, 7)])
    assert list(table.keys()) == [1, 2, 3]
    assert list(table.values()) == [5, 6, 7]
    assert table[1] == 5


def test_hashtable_initial_elements_with_duplicates():
    table = HashTable([(1, 5), (2, 6), (3, 7), (1, 11)])
    assert list(table.keys()) == [1, 2, 3]
    assert list(table.values()) == [11, 6, 7]
    assert table[1] == 11


def test_contains_in_hashtable():
    table = HashTable()
    table[1] = 5
    table[2] = 6
    table[3] = 7
    assert 1 in table
    assert 2 in table
    assert 3 in table
    assert 4 not in table


def test_len_in_hashtable():
    table = HashTable()
    table[1] = 5
    table[2] = 6
    table[3] = 7
    assert len(table) == 3


def test_string_in_hashtable_keys():
    table = HashTable()
    table[1] = 5
    table["2"] = 6
    table[3] = 7
    assert 1 in table
    assert "2" in table
    assert 3 in table


def test_tuple_in_hashtable_keys():
    table = HashTable()
    table[1] = 5
    table[(2, 3)] = 6
    table[3] = 7
    assert 1 in table
    assert (2, 3) in table
    assert 3 in table


def test_clear_hashtable():
    table = HashTable()
    table[1] = 5
    table[2] = 6
    table[3] = 7
    table.clear()
    assert list(table.keys()) == []
    assert list(table.values()) == []
