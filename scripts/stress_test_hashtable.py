from project.homework_5.hashtable import HashTable
import time


def deploy_inserts(table: HashTable, start: int, end: int):
    for i in range(start, end):
        table[i] = f"value_{i}"


def deploy_updates(table: HashTable, start: int, end: int):
    for i in range(start, end):
        if i in table:
            table[i] = f"updated_{i}"


def deploy_deletes(table: HashTable, start: int, end: int):
    for i in range(start, end):
        try:
            del table[i]
        except KeyError:
            pass


def main():
    initial_data = [(i, f"value_{i}") for i in range(5_000_000)]
    table = HashTable(initial_data)
