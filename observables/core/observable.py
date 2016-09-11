class Observable(object):

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
            watcher[1]()

    def __ensure_properties(self):
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
        :type raw_watchers: N-tuple
        '''

        nice_watchers = set()

        for raw_watcher in raw_watchers:
            update = raw_watcher[0]
            try:
                finish = raw_watcher[1]
            except IndexError:
                finish = None

            nice_watchers.add((update, finish))

        return nice_watchers
