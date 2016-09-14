from core.observer import Observer
from collections import Iterable


class Observable:

    def __init__(self, *watchers):
        '''
        Initialize the observable, optionally with one or more
        watchers.

        :param *watchers: One or more 2-tuples, each containing
            callback functions for update and complete
        '''

        self.__ensure_properties()
        self.watch(*watchers)

    def watch(self, *watchers):
        '''
        Add watchers to an :py:class:Observable.

        :param *watchers: One or more 2-tuples, each containing
            callback functions for update and complete
        '''

        self.__ensure_properties()
        self.__watchers |= self.__format_watchers(watchers)

    def unwatch(self, *watchers):
        '''
        Remove a watcher from an :py:class:Observable.

        :param *watchers: One or more 2-tuples, each containing
            callback functions for update and complete
        '''

        self.__ensure_properties()
        self.__watchers -= self.__format_watchers(watchers)

    def _update(self, payload):
        '''
        Send a payload to all watchers.

        This private method is meant to be called by a subclass. It
        accepts any payload and calls the update function of each
        watcher.

        :param payload: The payload to be delivered to each watcher
        :type payload: any
        '''

        for watcher in self.__watchers:
            watcher[0](payload)

    def _finish(self):
        '''
        Alert all watchers that this observable will not produce more
        output.

        This private method is meant to be called by a subclass. It
        calls the finished function of each watcher.
        '''

        for watcher in self.__watchers:
            if callable(watcher[1]):
                watcher[1]()

    def __ensure_properties(self):
        '''
        Ensures that the __watchers and __finished parameters exist.

        If not, it initializes __watchers as an empty set and
        __finished as False.
        '''
        if not hasattr(self, "__watchers"):
            self.__watchers = set()

        if not hasattr(self, "__finished"):
            self.__finished = False

    def __format_watchers(self, raw_watchers):
        '''
        Turns the raw input from a *watchers parameter into a set of
        homogenous (update, finish) tuples.

        :param raw_watchers: The watcher list from a *watchers
            parameter
        :type raw_watchers: N-tuple of Observers, iterators returning
            callables, or callables
        '''

        nice_watchers = set()

        for raw_watcher in raw_watchers:
            print("Parsing watcher: " + repr(raw_watcher))
            print("The watcher is an observer: " +
                  str(isinstance(raw_watcher, Observer)))
            if isinstance(raw_watcher, Observer):
                print("Got Observer: " + repr(raw_watcher))
                update = raw_watcher.update
                finish = raw_watcher.finish
            elif isinstance(raw_watcher, Iterable) and len(raw_watcher) >= 1 and callable(raw_watcher[0]):
                update = raw_watcher[0]
                if len(raw_watcher) >= 2:
                    finish = raw_watcher[1]
                else:
                    finish = None
            elif callable(raw_watcher):
                update = raw_watcher
                finish = None
            else:
                raise TypeError(
                    "Watcher must be an Observer, an iterator returning callables, or a callable")

            nice_watchers.add((update, finish))

        return nice_watchers
