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
        self.values[key].insert(data)
        self._keys[key] = self.values[key].nodes

    def _avl_insert_presentation(self, key):
        column = [
            [str(key)],
            [self.values[key]]
        ]
        return AsciiTable(column).table

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

    def _lim_charge_func(self):
        return len(self.values) // 2 + 1

    # def _list_nodes_cell(self, cell):
    #     if self._is_tree(cell):
    #         return cell.nodes
    #     return None

    def rehashing(self):
        survivor_values = [tree for tree in self.values if tree is not None]
        self.size_table = next_prime(self.size_table, factor=2)
        self.lim_charge = self._lim_charge_func()
        self._keys.clear()
        self.values = [None] * self.size_table #hell's pointers D: don't DRY ;/
        [self.bulk_insert(tree.nodes) for tree in survivor_values]

    def _colision_resolution(self, key, data=None):
        # print('charge factor {0}'.format(self.charge_factor))
        if not(
            (self.values.count(None) <= self.lim_charge)
            and
            (
                self.balanced_factor_cell(self.values[key]) <= self.charge_factor
                and 
                self.values[key].find(data) is None
            )
        ): 
            print(self.values[key], self.balanced_factor_cell(self.values[key]))
            return key
        
        i = 1
        new_key = self.hash_function(key + i*i)

        while self.values[new_key] is not None:

            new_key = self.hash_function(key + i*i) if not \
            (
                (self.values.count(None) <= self.lim_charge) 
                and
                (
                    self.balanced_factor_cell(self.values[new_key]) <= self.charge_factor
                    and
                    self.values[new_key].find(data) is None
                )
            ) else None
            i += 1
            
            if new_key is not None:
                break
                print(new_key, data)
                return new_key
            
            elif new_key is None or (new_key is None and self.with_rehashing is True):
                print('rehashing')
                print(new_key, data)
                break

        
        
       

