import timeit

if __name__ == "__main__":
    import timeit
    print("< Python native >")
    setup = "from impl.nativeimpl import arrayimpl; import numpy;array = numpy.random.randint(1,200,1000000).reshape(1000,1000)"
    print(timeit.timeit("i=arrayimpl();i.get_avg_len_rows(array)", setup=setup,number=1))
    print("< Numba >")
    setup = "from impl.numbaimpl import arrayimpl; import numpy;array = numpy.random.randint(1,200,1000000).reshape(1000,1000);n=arrayimpl();n.get_avg_len_rows(array)"
    print(timeit.timeit("i=arrayimpl();i.get_avg_len_rows(array)", setup=setup,number=1))

    print("< Cython >")
    setup = "from impl.cythonimpl import arrayimpl; import numpy;array = numpy.random.randint(1,200,1000000).reshape(1000,1000)"
    print(timeit.timeit("i=arrayimpl();i.get_avg_len_rows(array)", setup=setup,number=1))
    
    
    


