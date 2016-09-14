import unittest
from core.observable import Observable
from core.observer import Observer


class TestObservable(unittest.TestCase):

    def setUp(self):
        self.doublePayload = lambda x: 2 * x

        def returnPayload(payload):
            return payload
        self.returnPayload = returnPayload

        def returnString():
            return "finished"
        self.returnString = returnString

        def returnAlmostPi():
            return 22 / 7
        self.returnAlmostPi = returnAlmostPi

        class EchoObserver(Observer):

            def update(self, payload):
                return payload

            def finish(self):
                return "finished"

        self.EchoObserver = EchoObserver
        self.echoObserver = EchoObserver()

        class PassThrough(Observable, Observer):

            def update(self, payload):
                self._update(payload)

            def finish(self):
                self._finish()

        self.PassThrough = PassThrough

        self.watcherExamples = [
            (
                # Test that no input is fine
                (),
                set()
            ),
            (
                # Test two functions
                ((self.returnPayload, self.returnString),),
                {(self.returnPayload, self.returnString)}
            ),
            (
                # Test watcher
                (self.echoObserver, ),
                {(self.echoObserver.update, self.echoObserver.finish)}
            ),
            (
                # Test
                (self.doublePayload,),
                {(self.doublePayload, None)}
            ),
            (
                # Test that duplicates are ignored
                (self.echoObserver, self.echoObserver),
                {(self.echoObserver.update, self.echoObserver.finish)}
            ),
            (
                # Test two functions and observer
                ((self.returnPayload, self.returnAlmostPi), self.echoObserver),
                {
                    (self.returnPayload, self.returnAlmostPi),
                    (self.echoObserver.update, self.echoObserver.finish)
                }
            )
        ]

    def testInit(self):

        for watcherExample in self.watcherExamples:
            obl = Observable(*watcherExample[0])
            self.assertSetEqual(
                watcherExample[1],
                obl._Observable__watchers)

    def testWatch(self):
        obl = Observable()
        expected = set()

        self.assertSetEqual(obl._Observable__watchers, expected)

    def testUnwatch(self):
        pass

    def testUpdate(self):
        pass

    def testFinish(self):
        pass

    def testEnsureProperties(self):
        pass

    def testFormatWatchers(self):
        pass

if __name__ == "__main__":
    unittest.main()
