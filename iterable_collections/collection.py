from collections import Iterable

from iterable_collections.factory import DefaultMethodStrategyFactory


class Collection:

    def __init__(self, iterable, strategies):
        self._iterable = None
        self.iterable = iterable
        self._strategies = strategies

    def __getattr__(self, item):
        if item not in self._strategies:
            raise AttributeError('Unknown attribute {}'.format(item))
        return self._strategies[item].make_method(self)

    def __iter__(self):
        return iter(self.iterable)

    def __next__(self):
        return next(self.iterable)

    def __repr__(self):
        return 'Collection({})'.format(self.iterable)

    @property
    def iterable(self):
        return self._iterable

    @iterable.setter
    def iterable(self, iterable):
        if not isinstance(iterable, Iterable):
            ValueError('Must be an Iterable type.')
        self._iterable = iterable


def collect(iterable):
    return Collection(iterable, DefaultMethodStrategyFactory().create())
