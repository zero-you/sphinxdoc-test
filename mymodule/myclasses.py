from __future__ import print_function

class TestClass(object):
    """
    This is a test class
    """
    def __init__(self, verbose=0):
        """
        Initiate the test class object

        Parameters
        ----------
        verbose : int
                  the level of details to be printed to stdout
        """
        if verbose>0:
            print('hello', 'world')
        self._status = 'success'

    @property
    def status(self):
        """
        Status of object creation
        """
        return self._status
