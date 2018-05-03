from avl_tree.avl_weiss import AVL as AvlTree
from .hash_table import HashTable
from terminaltables import AsciiTable

class HMA(HashTable):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _set_value(self, key, data):
        self.values[key] = AvlTree() if self.values[key] is None else self.values[key]
        self.values[key].insert(data)
        self._keys[key] = self.values[key].nodes
    
    def _avl_insert_presentation(self, key):
        column = [
            [str(key)],
            [self.values[key]]
        ]
        print(AsciiTable(column).table)

    def _insert_presentation(self, *kwargs):
        super().__init__(*kwargs)
        self._avl_insert_presentation(kwargs['key'])
    
    def _is_tree(self, cell):
        return (cell is not None and cell is isinstance(AvlTree))

    def balanced_factor_cell(self, cell):
        if self._is_tree(cell):
            return cell.__class__.getHeight(cell[0])
        return 0

    def _lim_charge_func(self):
        return len(self.values) // 2 + 1
    
    def _list_nodes_cell(self, cell):
        if self._is_tree(cell):
            return cell.nodes
        return None

    def rehashing(self):
        pass
    
    def _colision_resolution(self, key, data=None):
        i = 1
        new_key = self.hash_function(key + i*i)

        while self.values[new_key] is not None \
                and self.values[new_key] != key:
            new_key = self.hash_function(key + i*i) if \
            (
                self.values.count(None) <= self.lim_charge 
                or
                self.balanced_factor_cell(self.values[new_key]) < self.lim_charge 
                or 
                data in self._list_nodes_cell(self.values[new_key])
            ) else None
            
            if new_key is not None:
                break
                return new_key
            elif new_key is None or (new_key is None and self.with_rehashing is True):
                break
        
    