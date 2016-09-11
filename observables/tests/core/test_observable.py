import unittest
from core.observable import Observable


class TestObservable(unittest.TestCase):

    def testInit(self):

        # Empty observable
        oEmpty = Observable()

        self.assertTrue(hasattr(oEmpty, "_Observable__watchers"))
        self.assertTrue(hasattr(oEmpty, "_Observable__finished"))
        self.assertFalse(oEmpty._Observable__finished)
        self.assertSetEqual(oEmpty._Observable__watchers, set())

    def testWatch(self):
        pass

if __name__ == "__main__":
    unittest.main()
