from .hash_table import HashTable
from .number_theory.prime_numbers import next_prime

class DoubleHashTH(HashTable):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def __hash_double_function(self, data, th):
        return data % th

    def _colision_resolution(self, key, data=None):
        print(self._colision_presentation( data=data, new_key=key, size_table=self.size_table))
        new_key = key
        aux = self.size_table

        while self.values[new_key] is not None and self.values[new_key] != key:
            
            if self.balanced_factor() >= self.lim_charge:
                new_key = None
                break
            
            else:
                if aux == 2:
                    new_key = None
                    return new_key

                next_prime_lt = next_prime(aux, desc=True)
                aux = next_prime_lt
                print("TH = {0}".format(next_prime_lt))
                new_key = self.__hash_double_function(data, next_prime_lt)
                
                if self.values[new_key] is not None and self.values[new_key] != key:
                    print(self._colision_presentation(
                        data=data, new_key=new_key, size_table=next_prime_lt
                    ))
        
        return new_key