import collections


class DictItem(collections.namedtuple('DictItem', 'key value')):
    """
    An individual element of an :obj:`ItemsView<typing.ItemsView>` as a :obj:`namedtuple<collections.namedtuple>` with
    ``key`` and ``value`` attributes.

    Attributes:
        key(:obj:`Hashable<typing.Hashable>`): The key of an individual element of an :obj:`ItemsView<typing.ItemsView>`
            (e.g. the item at position 0 of one the :obj:`tuples<python:tuple>` that make up an
            :obj:`ItemsView<typing.ItemsView>`.).
        value(:obj:`Any<typing.Any>`): The value of an individual element of an :obj:`ItemsView<typing.ItemsView>`
            (e.g. the item at position 1 of one the :obj:`tuples<python:tuple>` that make up an
            :obj:`ItemsView<typing.ItemsView>`.).
    """


def make_nt_items(iterable):
    return list(map(DictItem._make, iterable))


def partial_at_position(func, *args, pos=0, **kwargs):
    return lambda *a, **k: func(*(a[:pos] + args + a[pos:]), **dict(k, **kwargs))


def rpartial(func, *args, **kwargs):
    return lambda *a, **k: func(*(a + args), **dict(k, **kwargs))


def safe_call(func, error_strategy, *args, **kwargs):
    try:
        res = func(*args, **kwargs)
    except error_strategy.get_error() as e:
        raise error_strategy.handle(e)
    return res


def spread_tuple_parameter(func, *args, pos=0, **kwargs):
    return (lambda *x: func(*(x[:pos] + x[pos] + x[pos + 1:])), *args)
