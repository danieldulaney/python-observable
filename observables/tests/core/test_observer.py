import unittest
from core.observer import Observer


class Test(unittest.TestCase):

    def testAbstraction(self):
        self.assertRaises(TypeError, Observer,
                          "Observer should throw a TypeError on instantiation")

    def testSubclass(self):

        class ConcreteObserverNoUpdate(Observer):

            def finish(self):
                return True

        class ConcreteObserverNoFinish(Observer):

            def update(self, payload):
                return payload

        class ConcreteObserver(Observer):

            def update(self, update):
                return update

            def finish(self):
                return True

        self.assertRaises(TypeError, ConcreteObserverNoUpdate,
                          "ConcreteObserverNoUpdate should throw a TypeError on instantiation")

        self.assertRaises(TypeError, ConcreteObserverNoFinish,
                          "ConcreteObserverNoFinish should throw a TypeError on instantiation")

        ConcreteObserver()

if __name__ == "__main__":
    unittest.main()
