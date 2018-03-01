from __future__ import print_function

class TestClass(object):
    """
    This is a test class

    Attributes
    ----------
    status : str
        status of object creation
    """
    def __init__(self, verbose=0):
        """
        Initiate the test class object

        Parameters
        ----------
        verbose : int
                  the level of details to be printed to stdout
        """
        if verbose > 0:
            print('hello', 'world')
        self._status = 'success'

    @property
    def status(self):
        return self._status

    def testfun(self, test_input):
        """
        A test function

        Parameters
        ----------
        test_input : list
            a list of integers

        Returns
        out : list
            a list of integers
        """
        out = list(map(lambda x: x**2, test_input))
        return out
