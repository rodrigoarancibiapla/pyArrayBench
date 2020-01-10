def get_avg_len_rows(myArray):        
    suma = 0        
    for line in myArray:
        suma = suma + len(str(sum(line)))    
    return int((suma / len(myArray)))