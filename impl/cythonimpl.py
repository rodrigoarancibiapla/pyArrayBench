from interfaces.IArray import IArray
import impl.cython_impl_function

class arrayimpl(IArray):
     def get_avg_len_rows(self, myArray):        
        return impl.cython_impl_function.get_avg_len_rows_cy(myArray)
    
