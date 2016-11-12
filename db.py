## BPDB ##
# brunston (c) 2016

import numpy as np

class BPDB:
    """
    A new BPDB object, which contains both structured and unstructured data.
    Access this data with clean syntax.
    >>> b = BPDB()
    >>> print(b)
    BPDB(0,0)
    >>> foo = [100]
    >>> b.add_data(foo, 's')
    >>> print(b)
    BPDB(1,0)
    >>> bar = ['bar']
    >>> b.add_data(bar, 'u')
    >>> print(b)
    BPDB(1,1)
    """
    
    def __init__(self, name):
        self.s = np.array([]) # structured
        self.u = np.array([]) # unstructured

    def __str__(self):
        return "BPDB({0},{1})".format(len(self.s), len(self.u))

    def add_data(self, data, dtype):
        """
        adds data to the in-memory database. Does *not* modify flatfile databse
        """
        if dtype == "s":
            self.s = np.append(self.s, data)
        elif dtype == "u":
            self.u = np.append(self.u, data)
        else:
            raise Exception('DTypeError')
        return True # success

    def syncout(self):
        """
        syncs in-memory database out to flatfile database
        """
        np.savetxt(name+"s.bpdb", self.s) # save structured
        np.savetxt(name+"u.bpdb", self.u) # save unstructured

        return

    def syncin(self):
        """
        syncs flatfile database into memory.
        """

if __name__ == "__main__":
    import doctest
    doctest.testmod()
