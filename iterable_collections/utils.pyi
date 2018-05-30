import collections
from typing import Any, Callable, Hashable, ItemsView, List, NamedTuple, Sequence, Tuple, Union, Type

from iterable_collections.strategy import ErrorHandlingStrategyInterface


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


def make_nt_items(iterable: Union[ItemsView, Sequence[Tuple[Hashable, Any]]]) -> List[DictItem]:
    """
    Accepts either an :obj:`ItemsView<typing.ItemsView>` object or a Sequence of Sequences of two elements with the first element
    being a hashable type.

    Args:
        iterable: A :obj:`MappingView<typing.MappingView>` or :obj:`Sequence` object.

    """


def partial_at_position(func: Callable, *args, pos: int = 0, **kwargs) -> Callable:
    """
    Returns a function with ``args`` inserted at ``pos``, so that::

        f = lambda x, y, z: x + y + z

        p1 = partial_at_position(f, 1, pos=1)
        assert p1(1, 1) == 3

        p2 = partial_at_position(f, 1, 1, pos=0)
        assert p2(1) == 3

        p3 = partial_at_position(f, 1, 1, 1, pos=0)
        assert p3() == 3

    Keyword arguments are also accepted::

        f = lambda x, y, z=None: x + y + z

        p4 = partial_at_position(f, 1, 1, pos=0, z=1)
        assert p4() == 3

    Args:
        func: A function to which ``args`` and ``kwargs`` will be applied.
        *args: Arguments to be passed to ``func``.
        pos: The position at which to insert ``args``.
        **kwargs: Keyword arguments to be passed to ``func``.

    """


def rpartial(func: Callable, *args, **kwargs) -> Callable:
    """
    Returns a function with ``args`` as the right most arguments. So that::

        f = lambda x, y: (x, y)

        p1 = rpartial(f, 2)
        assert p1(1) == (1, 2)

        p2 = rpartial(f, 1, 2)
        assert p2() == (1, 2)

    Keyword Arguments are also accepted::

        f = lambda x, y=None: (x, y)

        p3 = rpartial(f, y=2)
        assert p3(1) == (1, 2)

    Args:
        func: A function to which ``args`` and ``kwargs`` will be applied.
        *args: Arguments to be passed to ``func``.
        **kwargs: Keyword arguments to be passed to ``func``.

    """


def safe_call(func: Callable, error_strategy: ErrorHandlingStrategyInterface, *args, **kwargs) -> Any:
    """
    Calls ``func`` inside a ``try: ... except:`` block expecting ``error_type``. ``args`` and ``kwargs`` are passed to
    ``func``. In the event of an error, ``error_instance`` it will be raised, if it is given. Otherwise, the resultant
    error is raised. If there are no errors, the result of ``func`` is returned.

    Args:
        func: The function to be called.
        error_strategy:
        *args: Arguments to be passed to ``func``.
        **kwargs: Keyword arguments to be passed to ``func``.

    """


def spread_tuple_parameter(func: Callable, *args, pos: int = 0, **kwargs) -> Tuple:
    """
    Returns a tuple containing a function which will receive a tuple of ``n`` length as an argument at ``pos`` and also
    ``args``. The tuple is spread so that its elements occupy the next ``n`` arguments starting at ``pos``.

    Args:
        func: A function whose signature receives ``n`` arguments in place of one tuple.
        *args: Additional arguments to returned in a tuple with a function.
        pos: The position the tuple should be spread.

    """
