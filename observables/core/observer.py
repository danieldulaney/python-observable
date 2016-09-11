from abc import (ABCMeta,
                 abstractmethod)


class Observer(metaclass=ABCMeta):

    @abstractmethod
    def update(self, payload):
        pass

    @abstractmethod
    def finish(self):
        pass
