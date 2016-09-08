class Observable(object):

    def __init__(self):
        pass

    def watch(self, *watchers):
        '''
        Add watchers to an :py:class:Observable.

        :param *watchers: One or more 2-tuples, each containing
            callback functions for update and complete
        '''

    def unwatch(self, *watchers):
        '''
        Remove a watcher from an :py:class:Observable.

        :param *watchers: One or more 2-tuples, each containing
            callback functions for update and complete
        '''

    def _update(self, payload):
        '''
        Send a payload to all watchers.

        This private method is meant to be called by a subclass. It
        accepts any payload and calls the update function of each
        watcher.

        :param payload: The payload to be delivered to each watcher
        :type payload: any
        '''

    def _finish(self):
        '''
        Alert all watchers that this observable will not produce more
        output.

        This private method is meant to be called by a subclass. It
        calls the finished function of each watcher.
        '''
