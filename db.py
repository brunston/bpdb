## BPDB ##
# brunston (c) 2016

import numpy as np

class BPDB:
    """
    A new BPDB object, which contains both structured and unstructured data.
    Access this data with clean syntax.
    >>> b = BPDB()
    >>> b
    BPDB()
    >>> foo = [100]
    >>> b.add_data(foo, 's')
    >>> b
    BPDB(1,0)
    >>> bar = ['bar']
    >>> b.add_data(bar, 'u')
    >>> b
    BPDB(1,1)
    """
    
    def __init__(self):
        self.u = np.array([])
        self.s = np.array([])

    def __repr__(self):
        return "BPDB"

    def __str__(self):
        return "BPDB"

    def add_data(self, data, dtype):
        return None

if __name__ == "__main__":
    import doctest
    doctest.testmod()
