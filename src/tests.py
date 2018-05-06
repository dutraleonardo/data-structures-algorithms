from avl_tree.avl_weiss import AVL as avl_tree
from hashing.middle_open_hash import HMA
from hashing.double_hash_r import DoubleHashR
from hashing.double_hash_th import DoubleHashTH
from hashing.hash_table import HashTable
from hashing.hash_table_with_linked_list import HashTableWithLinkedList
from hashing.number_theory.prime_numbers import next_prime

def test_insert_avl(display, values):
    tree = avl_tree(display=display)
    root = tree.createFromList(values)
    tree.display_tree(root)
    tree.nodes

def test_insert_hma(size_table, charge_factor, values, rehashing=True):
    hma = HMA(size_table=size_table, charge_factor=charge_factor, rehashing=rehashing)
    hma.bulk_insert(values)
    return hma

def test_insert_double_hash_r(size_table, values):
    dh = DoubleHashR(size_table)
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

def test_nex_lt_prime(value):
    _next = next_prime(value)
    return _next

def test_double_hash_th(size_table, values):
    dh = DoubleHashTH(size_table=size_table)
    dh.bulk_insert(values)
    return dh

def test_insert_delete_hma(size_table, charge_factor, values_to_insert, values_to_delete):
    hma = test_insert_hma(size_table, charge_factor,  values_to_insert, rehashing=True)
    for value in values_to_delete:
        if hma.delete_value(value) is not None:
            print('element {0} deleted'.format(value))
            print(hma)
        else:
            print('element {0} not found'.format(value_t))


# print(test_double_hash_th(29, [22, 43, 36, 16, 44, 77, 62, 32, 71, 31, 41, 27, 29, 19, 7, 14, 91, 81, 1]))
# test_insert_hma(5,3, [6,4,8,21,37,59,16,13,6,8,11, 22,36,9,17,31,4,17,11,22,39,42,16,18], False)
# test_insert_hma(5,3, [61, 31, 41, 27, 18, 19, 7, 14, 9122, 43, 36, 16, 44, 77, 62, 32, 101, 1], False)
test_insert_delete_hma(5,3, [61, 31, 41, 27, 18, 19, 7, 14, 9122, 43, 36, 16, 44, 77, 62, 32, 101, 1], 
[36, 71, 7, 31])