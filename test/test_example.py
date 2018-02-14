import unittest
import mymodule

class TestExample(unittest.TestCase):

    def test_create(self):
        myobj = mymodule.TestClass(verbose=1)
        self.assertEqual(myobj.status.lower(), 'success')


if __name__ == '__main__':
    unittest.main()
