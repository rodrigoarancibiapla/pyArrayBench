from interfaces.IArray import IArray
from numba import jit
import math
from impl.native_impl_function import get_avg_len_rows

class arrayimpl(IArray):  
    @staticmethod
    @jit(nopython=True)   
    def call_native_get_avg_len_rows(myArray):         
        suma = 0        
        for lineN in range(len(myArray)):
            s = 0
            for x in range(len(myArray[lineN])):
                s = s + myArray[lineN][x]
            suma = suma + int(math.log10(s))+1
        return int((suma / len(myArray)))       
        
    def get_avg_len_rows(self, myArray):        
        return self.call_native_get_avg_len_rows(myArray)
    
