from avl_tree.avl_weiss import AVL as avl_tree
from hashing.middle_open_hash import HMA


def test_avl(display, values):
    tree = avl_tree(display=display)
    root = tree.createFromList(values)
    tree.display_tree(root)
    tree.nodes

def test_hma(size_table, charge_factor, values, rehashing):
    hma = HMA(size_table=size_table, charge_factor=charge_factor, rehashing=rehashing)
    hma.bulk_insert(values)


test_hma(5,2, [6, 4, 8, 21, 37,59,16,13,6, 8,11,22,36,9,17,11,22,39,42,16,18], True)
# test_avl(True, [1,2,3,4])