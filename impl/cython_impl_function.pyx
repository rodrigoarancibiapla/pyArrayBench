import math
from cpython cimport array
from libc.math cimport log10
cimport cython
import array

@cython.boundscheck(False) 
@cython.wraparound(False) 
def get_avg_len_rows_cy(myArray):   
    cdef double suma = 0     
    cdef int s
    cdef int[:, :] varray = myArray
    cdef int cols = len(myArray[0])
    cdef int rows = len(myArray)
    for lineN in range(rows):
        s = 0
        for x in range(cols):
            s = s + varray[lineN][x]        
        suma = suma + log10(s) +1
    return int((suma / len(myArray)))  

