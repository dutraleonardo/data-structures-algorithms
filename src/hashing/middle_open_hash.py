from avl_tree.avl_weiss import AVL as AvlTree
from .hash_table import HashTable
from .quadratic_probing import QuadraticProbing
from terminaltables import AsciiTable
from .number_theory.prime_numbers import next_prime


class HMA(QuadraticProbing):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _set_value(self, key, data):
        self.values[key] = AvlTree(display=False) if self.values[key] is None else self.values[key]
        self.values[key] = self.values[key].insert(data)
        self._keys[key] = self.values[key].nodes
        print('{0} insert in bucket {1}'.format(data, key))
        print(self)

    def _insert_presentation(self, **kwargs):
        super()._insert_presentation(**kwargs)
        self._avl_insert_presentation(kwargs["key"])

    def _is_tree(self, cell):
        return True if isinstance(cell, AvlTree) else False
        # return (cell is not None) and (cell is isinstance(cell, AvlTree))

    def balanced_factor_cell(self, cell):
        if self._is_tree(cell):
            return cell.__class__.getHeight(cell)
        return 0

    def delete_value(self,value):
        
        def _delete_in_tree(self, tree, value):
            try:
                tree.delete(value)
                return tree 
            except ValueError:
                return None

        for tree in [index for index in self.values if index is not None]:
            if _delete_in_tree(self, tree, value) is not None:
                return value
            else:
                return None

    def _list_cells_with_height_equal_charge_factor(self):
        list_heights_trees = [tree for tree in self.values \
        if tree is not None and self.balanced_factor_cell(tree) == self.charge_factor]
        return list_heights_trees
    
    def rehashing(self):
        survivor_values = [tree for tree in self.values if tree is not None]
        self.size_table = next_prime(self.size_table, factor=2)
        self.values = [None] * self.size_table
        self.lim_charge = self._lim_charge_func()
        self._keys.clear() #hell's pointers D: don't DRY ;/
        print("\n##########------** rehashing new size table value => {0}".format(self.size_table) + ' **------##########\n')
        values = []
        for tree in survivor_values:
            values += tree.nodes
        self.bulk_insert(values)

    def _maximun_nodes_avl_with_height(self, h):
        return 2**(h+1)-1

    def _colision_resolution(self, key, data=None):
        trees = self._list_cells_with_height_equal_charge_factor()

        if len(trees) < self.lim_charge and \
            (self.balanced_factor_cell(self.values[key]) <=  self.charge_factor
            and
            self.values[key].find(data) is None
            and
            len(self.values[key].nodes) < self._maximun_nodes_avl_with_height(self.charge_factor)):
            # print('{0} insert in bucket {1}'.format(data, key))
            return key

        i = 1
        new_key = self.hash_function(key + i*i)

        while self.values[new_key] is not None:

            if not \
            (
                self.balanced_factor_cell(self.values[new_key]) <=  self.charge_factor
                and
                self.values[new_key].find(data) is None
                and
                len(self.values[new_key].nodes) < self._maximun_nodes_avl_with_height(self.charge_factor)
            ):
                i+=1
                new_key = self.hash_function(key + i*i)
            elif not len(trees) < self.lim_charge:
                new_key = None

            if new_key is not None:
                # print('{0} insert in bucket {1}'.format(data, new_key))
                return new_key

            elif new_key is None or (new_key is None and self.with_rehashing is True):
                break

        # print('{0} insert in bucket {1}'.format(data, new_key))
        return new_key





