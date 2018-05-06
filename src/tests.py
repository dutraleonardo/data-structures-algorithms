from avl_tree.avl_weiss import AVL as avl_tree
from hashing.middle_open_hash import HMA
from hashing.double_hash_r import DoubleHash
from hashing.hash_table import HashTable
from hashing.hash_table_with_linked_list import HashTableWithLinkedList

def test_insert_avl(display, values):
    tree = avl_tree(display=display)
    root = tree.createFromList(values)
    tree.display_tree(root)
    tree.nodes

def test_insert_hma(size_table, charge_factor, values, rehashing):
    hma = HMA(size_table=size_table, charge_factor=charge_factor, rehashing=rehashing)
    hma.bulk_insert(values)

def test_insert_double_hash_r(size_table, values):
    dh = DoubleHash(size_table)
    dh.bulk_insert(values)
    print(dh)

def test_insert_hash_linked_list(size_table, charge_factor, values):
    hl = HashTableWithLinkedList(charge_factor=charge_factor, size_table=size_table)
    hl.bulk_insert(values)
    return hl

def test_insert_hash_table(size_table, values):
    ht = HashTable(size_table=size_table)
    ht.bulk_insert(values)
    # print(ht)
    return ht


# hl = test_insert_hash_linked_list(7, 3, [0,1,85,6,36,46,89,112,44])
# print(hl)
# hl.delete_value(85)
# print(hl)
test_insert_hma(5,3, [61, 31, 41, 27, 18, 19, 7, 14, 9122, 43, 36, 16, 44, 77, 62, 32, 101, 1], True)
# test_double_hash_r(29, [22, 43, 36, 16, 44, 77, 62, 32, 71, 31, 41, 27, 29, 19, 7, 14, 91, 81, 1])
# ht = test_insert_hash_table(11,[89,18,49,60,69,18])
# print(ht)
# print(ht.delete_value(18))
# print(ht.delete_value(69))
# print(ht)

