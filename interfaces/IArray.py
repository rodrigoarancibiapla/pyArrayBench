from abc import ABC, abstractmethod

class IArray(ABC):

    @abstractmethod
    def get_avg_len_rows(self, myArray):        
        pass
