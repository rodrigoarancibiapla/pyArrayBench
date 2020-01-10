from interfaces.IArray import IArray
from impl.native_impl_function import get_avg_len_rows

class arrayimpl(IArray):
     def get_avg_len_rows(self, myArray):        
        return get_avg_len_rows(myArray)
    
