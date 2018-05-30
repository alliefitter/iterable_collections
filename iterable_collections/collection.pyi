from collections import OrderedDict
from typing import Any, Callable, Dict, Hashable, Iterable, Iterator, List, Mapping, MappingView, Optional, Set, \
    Sequence, Tuple, Union

from iterable_collections.strategy import MethodStrategyInterface
from iterable_collections.utils import DictItem

StrategyDict = Dict[str, MethodStrategyInterface]

class Collection:
    """
    A container class for an iterable. Public methods of this class are defined by a :obj:`dict`
    containing objects implementing
    :obj:`MethodStrategyInterface<iterable_collections.strategy.MethodStrategyInterface>`.

    """
    def __init__(self, iterable: Iterable, strategies: StrategyDict) -> None:
        """
        Args:
            iterable: The Iterable type object :obj:`Collection` wraps around.
            strategies
        """
        self._iterable = None

    @property
    def iterable(self):
        """:obj:`Iterable<typing.Iterable>`: The Iterable type object :obj:`Collection` wraps around."""
    def all(self, store: bool = None, ret: bool = None) -> bool:
        """
        A proxy to the :func:`python:all` builtin function with :attr:`iterable<Collection.iterable>` as the first
        argument, ``iterable``.

        Args:
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def any(self, store: bool = None, ret: bool = None) -> bool:
        """
        A proxy to the :func:`python:any` builtin function with :attr:`iterable<Collection.iterable>` as the first
        argument, ``iterable``.

        Args:
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def chunks(self, length: int, store: bool = None, ret: bool = None) -> 'Collection':
        """
        Break the elements  of :attr:`iterable<Collection.iterable>` into a series of ``length`` long lists.

        Args:
            length: The number of elements each resulting list should contain.
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def chunks_dict(self, length: int, store: bool = None, ret: bool = None) -> 'Collection':
        """
        Break the elements  of :attr:`iterable<Collection.iterable>` into a series of ``length`` long lists. For use
        when :attr:`iterable<Collection.iterable>` is a :class:`python:dict`.

        Args:
            length: The number of elements each resulting list should contain.
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def chunks_iter(self, length: int, store: bool = None, ret: bool = None) -> 'Collection':
        """
        Break the elements  of :attr:`iterable<Collection.iterable>` into a series of ``length`` long lists. For use
        when :attr:`iterable<Collection.iterable>` is a :class:`python:typing.Sequence`.

        Args:
            length: The number of elements each resulting list should contain.
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def chunks_seq(self, length: int, store: bool = None, ret: bool = None) -> 'Collection':
        """
        Break the elements  of :attr:`iterable<Collection.iterable>` into a series of ``length`` long lists.For use
        when :attr:`iterable<Collection.iterable>` is a :class:`python:typing.Sequence`.

        Args:
            length: The number of elements each resulting list should contain.
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def concat(self, *other: Iterable, store: bool = None, ret: bool = None) -> 'Collection':
        """
        Concatenate an arbitrary number of :obj:`Iterables<typing.Iterable>` with :attr:`iterable<Collection.iterable>`. Each
        iterable is passed to the appropriate method (e.g. :obj:`python:dict` type arguments are passed to
        :meth:`Collection.concat_dict` while :obj:`python:list` type arguments are passed to
        :meth:`Collection.concat_seq`.).

        Args:
            *other: An :obj:`Iterable(s)<typing.Iterable>` to be concatenated with the :attr:`iterable<Collection.iterable>`
                property.
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def concat_dict(self, other: Mapping, store: bool = None, ret: bool = None) -> 'Collection':
        """
        Concatenate a A :obj:`dict` or other :obj:`Mapping<typing.Mapping>` type object with :attr:`iterable<Collection.iterable>`
        Calls :class:`python:dict` on both ``other`` and ``iterable`` then uses :meth:`dict.update` to combine the two.
        Equivalent to::

            dict(iterable).update(dict(other))


        Args:
            other: A :obj:`dict` or other :obj:`Mapping<typing.Mapping>` type object to be concatenated with the
                :attr:`iterable<Collection.iterable>` property using the :meth:`dict.update` method.
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        Raises:
            TypeError: Raised if either ``other`` or ``iterable`` are not structured in a way that can be converted to
                :obj:`dict` (e.g. is already a ``dict`` or subclass of ``dict`` (such as :obj:`collections.OrderedDict`)
                or a sequence of tuples each with two elements--with the element at position 0 being of a
                `hashable type <https://docs.python.org/3/glossary.html>`_)

        """
    def concat_iter(self, other: Iterator, store: bool = None, ret: bool = None) -> 'Collection':
        """
        Concatenate :attr:`iterable<Collection.iterable>` with an iterator using the :func:`itertools.chain` function.
        Calls :class:`python:iter` on both ``other`` and ``iterable`` then passes both to :func:`itertools.chain`.
        Equivalent to::

            chain(iter(iterable), iter(other))


        Args:
            other: An :obj:`Iterator<typing.Iterator>` type object to be concatenated with the
                :attr:`iterable<Collection.iterable>` property.
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def concat_seq(self, other: Union[MappingView, Sequence, Set], store: bool = None, ret: bool = None) -> 'Collection':
        """
        Concatenate :attr:`iterable<Collection.iterable>` with a :obj:`Sequence<typing.Sequence>`, :obj:`Set<typing.Set>`, or
        :obj:`MappingView<typing.MappingView>` object. Calls :class:`python:list` on both ``other`` and ``iterable``
        then pass both to :func:`operator.concat`. Equivalent to::

            concat(list(iterable), list(other))


        Args:
            other: A :obj:`Sequence<typing.Sequence>`, :obj:`Set<typing.Set>`, or :obj:`MappingView<typing.MappingView>`
                object to be concatenated with the :attr:`iterable<Collection.iterable>` property.
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def contains(self, b: Any, store: bool = None, ret: bool = None) -> bool:
        """
        A proxy to :func:`operator.contains` with :attr:`iterable<Collection.iterable>` as the first argument, ``a``.

        Args:
            b: An object whose presence in :attr:`iterable<Collection.iterable>` is be tested.
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def dict(self, store: bool = None, ret: bool = None, **kwargs) -> Dict:
        """
        Converts :attr:`iterable<Collection.iterable` to a :obj:`python:dict` and returns the result. A proxy to
        :class:`python:dict` with :attr:`iterable<Collection.iterable>` as the first argument, ``mapping``
        or ``iterable``. Equivalent to::

            dict(iterable)

        Args:
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.
            **kwargs: Additional keyword arguments that will be added to the resultant ``dict``.

        Raises:
            TypeError: Raised if either ``iterable`` are not structured in a way that can be converted to
                :obj:`dict` (e.g. is already a ``dict`` or subclass of ``dict`` (such as :obj:`collections.OrderedDict`)
                or a sequence of tuples each with two elements--with the element at position 0 being of a
                `hashable type <https://docs.python.org/3/glossary.html>`_)

        """
    def dict_(self, store: bool = None, ret: bool = None, **kwargs)-> 'Collection':
        """
        Convert :attr:`iterable<Collection.iterable` to a dict and store the result. An alias for
        :meth:`Collection.dict(store=True, ret=False)<Collection.dict>`. Equivalent to::

            dict(iterable)

        Args:
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.
            **kwargs: Additional keyword arguments that will be added to the resultant :obj:`python:dict`.

        Raises:
            TypeError: Raised if either ``iterable`` are not structured in a way that can be converted to
                :obj:`dict` (e.g. is already a ``dict`` or subclass of ``dict`` (such as :obj:`collections.OrderedDict`)
                or a sequence of tuples each with two elements--with the element at position 0 being of a
                `hashable type <https://docs.python.org/3/glossary.html>`_)

        """
    def diff(self, other: Iterable, store: bool = None, ret: bool = None)-> 'Collection':
        """
        Calculate the difference between the elements of :attr:`iterable<Collection.iterable>` and ``other``. The
        appropriate method is called based on the type of ``other`` (e.g. if ``other`` is a :obj:`python:dict` type
        object :meth:`diff_dict<Collection.diff_dict>` is called, if ``other`` is a :obj:`python:list` then
        :meth:`diff_seq<Collection.diff_seq>` is called.).

        Args:
            other: An Iterable type object to be compared with :attr:`iterable<Collection.iterable>`.
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def diff_dict(self, other: Mapping, store: bool = None, ret: bool = None)-> 'Collection':
        """
        Calculate the difference between :attr:`iterable<Collection.iterable>` and ``other``. Both are converted to
        :obj:`python:dict` and :meth:`dict.items` is called on each, then they are converted to :obj:`python:set` and
        passed to :func:`operator.sub`. Equivalent to::

            sub(set(dict(iterator).items()), set(dict(other).items()))

        Args:
            other: A Mapping type object to be compared with :attr:`iterable<Collection.iterable>`.
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        Raises:
            TypeError: Raised if either ``other`` or ``iterable`` are not structured in a way that can be converted to
                :obj:`dict` (e.g. is already a ``dict`` or subclass of ``dict`` (such as :obj:`collections.OrderedDict`)
                or a sequence of tuples each with two elements--with the element at position 0 being of a
                `hashable type <https://docs.python.org/3/glossary.html>`_)

        """
    def diff_seq(self, other: Union[Set, Sequence, MappingView], store: bool = None,
                 ret: bool = None)-> 'Collection':
        """
        Calculate the difference between :attr:`iterable<Collection.iterable>` and ``other``. Both are converted to
        :obj:`python:set` and passed to :func:`operator.sub`. Equivalent to::

            sub(set(iterable), set(iterable))

        Args:
            other: A Set, Sequence, or MappingView to be compared with :attr:`iterable<Collection.iterable>`.
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def diff_iter(self, other: Iterator, store: bool = None, ret: bool = None)-> 'Collection':
        """
        Calculate the difference between :attr:`iterable<Collection.iterable>` and ``other``. Both are converted to
        :obj:`python:set` and passed to :func:`operator.sub`. Equivalent to::

            sub(set(iterable), set(iterable))

        Args:
            other: An Iterator to be compared with :attr:`iterable<Collection.iterable>`.
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def emap(self, func: Callable[[int, Any], Any], *iterables: Optional[Iterable], store: bool = None,
             ret: bool = None)-> 'Collection':
        """
        Calls enumerate on :attr:`iterable<Collection.iterable>` and then maps the result with ``func``.
        :func:`spread_tuple_parameter<utils.spread_tuple_parameter>` is used to facilitate two parameters being passed
        to ``func``::

            lambda i, v: print('Index: {}, Value: {}'.format(i, v))

        ``emap`` is equivalent to::

            map(*spread_tuple_parameter(func), enumerate(iterable))

        Args:
            func: A function to which each element of iterable will be passed.
            *iterables: Additional Iterable type objects which will also be mapped.
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def enumerate(self, start: int = 0, store: bool = None, ret: bool = None)-> 'Collection':
        """
        A proxy to the :func:`python:enumerate` builtin function with :attr:`iterable<Collection.iterable>` as the first
        argument, ``iterable``.

        Args:
            start: The number from which to start the count. Defaults to 0.
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def empty(self, store: bool = None, ret: bool = None) -> bool:
        """
        Returns ``True`` if :attr:`iterable<Collection.iterable>` contains no elements. Iterators are evaluated
        differently that other Iterables. Equivalent to::

            not iterable if not isinstance(iterable, Iterator) else not any(True for _ in iterable)

        Args:
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def filter(self, func: Callable[[Any], Any], store: bool = None, ret: bool = None)-> 'Collection':
        """
        A proxy to the :func:`python:filter` builtin function with :attr:`iterable<Collection.iterable>` as the first
        argument, ``iterable``.

        Args:
            func: "Specifies a function of one argument that is used to extract a comparison key from each" element of
                iterable.
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def filter_items(self, func: Callable[[Hashable, Any], Any], store: bool = None, ret: bool = None)-> 'Collection':
        """
        Calls :meth:`dict.items` before :func:`python:filter`. Uses
        :func:`spread_tuple_parameter<utils.spread_tuple_parameter>` to facilitate spreading each element of the
        :obj:`ItemsView<typing.ItemsView>` into two parameters being passed to ``func``::

            lambda k, v: print('Key: {}, Value: {}'.format(k, v))

        Equivalent to::

            filter(*spread_tuple_parameter(func), dict(iterable).items())

        Args:
            func: "Specifies a function of one argument that is used to extract a comparison key from each" element of
                iterable.
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        Raises:
            TypeError: Raised if either ``iterable`` is not structured in a way that can be converted to
                :obj:`dict` (e.g. is already a ``dict`` or subclass of ``dict`` (such as :obj:`collections.OrderedDict`)
                or a sequence of tuples each with two elements--with the element at position 0 being of a
                `hashable type <https://docs.python.org/3/glossary.html>`_)

        """
    def filter_nt_items(self, func: Callable[[DictItem], Any], store: bool = None, ret: bool = None)-> 'Collection':
        """
        Calls :meth:`dict.items` on :attr:`iterable<Collection.iterable>` and converts the resultant
        :obj:`ItemsView<typing.ItemsView>` to a list of :obj:`DictItems<utils.DictItem>` with
        :func:`utils.make_nt_items` then calls :func:`python:filter`. Equivalent to::

            filter(func, make_nt_items(dict(iterable).items()))

        Args:
            func: "Specifies a function of one argument that is used to extract a comparison key from each" element of
                iterable.
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        Raises:
            TypeError: Raised if either ``iterable`` is not structured in a way that can be converted to
                :obj:`dict` (e.g. is already a ``dict`` or subclass of ``dict`` (such as :obj:`collections.OrderedDict`)
                or a sequence of tuples each with two elements--with the element at position 0 being of a
                `hashable type <https://docs.python.org/3/glossary.html>`_)

        """
    def first(self, store: bool = None, ret: bool = None) -> Any:
        """
        Returns an item at position ``0`` of :attr:`iterable<Collection.iterable>` using :func:`operator.itemgetter`.
        Note that ``iterable`` must be subscriptable. Equivalent to::

            itemgetter(0)(iterable)

        Args:
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        Raises:
            IndexError: Raised if ``iterable`` is an empty :obj:`python:list` or :obj:`python:tuple`.
            TypeError: Raised if ``iterable`` is not subscriptable.
            KeyError: Raised if ``iterable`` is a :obj:`python:dict` and the key ``0`` does not exist.

        """
    def first_item(self, store: bool = None, ret: bool = None) -> Any:
        """
        Calls :meth:`dict.items` on :attr:`iterable<Collection.iterable>` and converts the result to a
        :obj:`python:tuple` then returns the :obj:`python:tuple` as the tuple position ``0`` with
        :func:`operator.itemgetter`. Note that the :obj:`ItemsView<typing.ItemsView>` is converted to a
        :obj:`python:tuple` because ``ItemsViews`` are not subscriptable. Equivalent to::

            itemgetter(0)(tuple(dict(iterable).items))

        Args:
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        Raises:
            TypeError: Raised if either ``iterable`` is not structured in a way that can be converted to
                :obj:`dict` (e.g. is already a ``dict`` or subclass of ``dict`` (such as :obj:`collections.OrderedDict`)
                or a sequence of tuples each with two elements--with the element at position 0 being of a
                `hashable type <https://docs.python.org/3/glossary.html>`_)

        """
    def first_nt_item(self, store: bool = None, ret: bool = None) -> DictItem:
        """

        Calls :meth:`dict.items` on :attr:`iterable<Collection.iterable>` and converts the resultant
        :obj:`ItemsView<typing.ItemsView>` to a list of :obj:`DictItems<utils.DictItem>` with
        :func:`utils.make_nt_items` then retrieves the first element of the list. Equivalent to::

             itemgetter(0)(make_nt_items(dict(iterable).items()))

        Args:
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        Raises:
            TypeError: Raised if either ``iterable`` is not structured in a way that can be converted to
                :obj:`dict` (e.g. is already a ``dict`` or subclass of ``dict`` (such as :obj:`collections.OrderedDict`)
                or a sequence of tuples each with two elements--with the element at position 0 being of a
                `hashable type <https://docs.python.org/3/glossary.html>`_)

        """
    def flatten(self, store: bool = None, ret: bool = None)-> 'Collection':
        """
        Converts :attr:`iterable<Collection.iterable>` from an arbitrarily nested sequence a one dimensional
        :obj:`python:list`.

        Args:
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def getitem(self, b: Any, store: bool = None, ret: bool = None)-> Any:
        """
        Calls :func:`operator.getitem` on :attr:`iterable<Collection.iterable>` and retrieves the element at ``b``.
        Equivalent to::

            getitem(iterable, b)

        Args:
            b:
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.
        Raises:
            TypeError: Raised if :attr:`iterable<Collection.iterable>` is not of a subscriptable type.

        """
    def sorted_and_groupby(self, key: Optional[Callable], store: bool = None, ret: bool = None) -> 'Collection':
        """
        An alias for::

            Collection.sorted(key=key) \
                .group_by(key=key)

        Args:
            key: "Specifies a function of one argument that is used to extract a comparison key from each" element of
                iterable.
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def groupby(self, key: Optional[Callable], store: bool = None, ret: bool = None)-> 'Collection':
        """
        A proxy to :func:`itertools.groupby`. Equivalent to::

            groupby(iterable, key=key)

        Args:
            key:
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def intersect(self, other: Iterable, store: bool = None, ret: bool = None)-> 'Collection':
        """
        Calculate the intersect between :attr:`iterable<Collection.iterable>` and ``other``. Behaves differently
        based on the type of ``iterable``, calling the appropriate method for that type.

        Args:
            other: Another iterable.
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def intersect_dict(self, other: Mapping, store: bool = None, ret: bool = None)-> 'Collection':
        """
        Calculates the intersect between to objects of :obj:`python:dict` type. Calls :meth:`dict.items` on both
        :attr:`iterable<Collection.iterable>` and ``other``, converts them to :obj:`python:set`, and passes them to
        :func:`operator.and_`. Equivalent to::

            and_(set(dict(iterable).items()), set(dict(other).items()))

        Args:
            other: Another dict.
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        Raises:
            TypeError: Raised if either ``other`` or ``iterable`` are not structured in a way that can be converted to
                :obj:`dict` (e.g. is already a ``dict`` or subclass of ``dict`` (such as :obj:`collections.OrderedDict`)
                or a sequence of tuples each with two elements--with the element at position 0 being of a
                `hashable type <https://docs.python.org/3/glossary.html>`_)

        """
    def intersect_iter(self, other: Iterator, store: bool = None, ret: bool = None)-> 'Collection':
        """
        Calculates the intersect between to objects of :obj:`typing.Iterator` type. Converts both
        :attr:`iterable<Collection.iterable>` and ``other`` to :obj:`python:set` and passes them to
        :func:`operator.and_`. Equivalent to::

            and_(set(iterable), set(other))

        Args:
            other: Another iterator.
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def intersect_seq(self, other: Union[Set, Sequence, MappingView], store: bool = None,
                      ret: bool = None)-> 'Collection':
        """
        Calculates the intersect between to objects of :obj:`typing.Sequence` type. Converts both
        :attr:`iterable<Collection.iterable>` and ``other`` to :obj:`python:set` and passes them to
        :func:`operator.and_`. Equivalent to::

            and_(set(iterable), set(other))

        Args:
            other: Another sequence.
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def islice(self, start: int, stop: int, step: Optional[int], store: bool = None, ret: bool = None)-> 'Collection':
        """
        A proxy to :func:`itertools.islice`. Equivalent to::

            islice(iterable, start, stop, step)

        Args:
            start: The start position
            stop: The stop position
            step: The step.
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def items(self, store: bool = None, ret: bool = None)-> 'Collection':
        """
        Calls `dict.items` on :attr:`iterable<Collection.iterable>`. Equivalent to::

            dict(iterable).items()

        Args:
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def iter(self, sentinel: Optional[Any], store: bool = None, ret: bool = None) -> Iterable:
        """
        Converts :attr:`iterable<Collection.iterable` to a :obj:`python:iter` and returns the result. A proxy to
        :class:`python:iter` with :attr:`iterable<Collection.iterable>` as the first argument, ``object``.
        Equivalent to::

            iter(iterable)

        Args:
            sentinel: If the value of of ``sentinel`` is returned from ``object``, :obj:`StopIteration` is raised.
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def iter_(self, sentinel: Optional[Any], store: bool = None, ret: bool = None)-> 'Collection':
        """
        Convert :attr:`iterable<Collection.iterable` to an :obj:`typing.Iterator` and store the result. An alias for
        :meth:`Collection.iter(store=True, ret=False)<Collection.iter>`. Equivalent to::

            iter(iterable)

        Args:
            sentinel: If the value of of ``sentinel`` is returned from ``object``, :obj:`StopIteration` is raised.
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def join(self, str_: str, store: bool = None, ret: bool = None) -> str:
        """
        A proxy to the :obj:`python:str` method :meth:`python:str.join`. Should only be used with sequences of
        of :obj:`python:str`.

        Args:
            str_: The separator between the elements of :attr:`iterable<Collection.iterable>`.
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def last(self, store: bool = None, ret: bool = None) -> Any:
        """
        Returns an item at the last index of :attr:`iterable<Collection.iterable>` using :func:`operator.itemgetter`.
        Note that ``iterable`` must be subscriptable. Equivalent to::

            itemgetter(-1)(iterable)

        Args:
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        Raises:
            IndexError: Raised if ``iterable`` is an empty :obj:`python:list` or :obj:`python:tuple`.
            TypeError: Raised if ``iterable`` is not subscriptable.
            KeyError: Raised if ``iterable`` is a :obj:`python:dict` and the key ``0`` does not exist.

        Args:
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def last_nt_item(self, store: bool = None, ret: bool = None) -> Any:
        """
        Calls :meth:`dict.items` on :attr:`iterable<Collection.iterable>` and converts the resultant
        :obj:`ItemsView<typing.ItemsView>` to a list of :obj:`DictItems<utils.DictItem>` with
        :func:`utils.make_nt_items` then retrieves the last element of the list. Equivalent to::

             itemgetter(0)(make_nt_items(dict(iterable).items()))

        Args:
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        Raises:
            TypeError: Raised if either ``iterable`` is not structured in a way that can be converted to
                :obj:`dict` (e.g. is already a ``dict`` or subclass of ``dict`` (such as :obj:`collections.OrderedDict`)
                or a sequence of tuples each with two elements--with the element at position 0 being of a
                `hashable type <https://docs.python.org/3/glossary.html>`_)
        Args:
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def last_item(self, store: bool = None, ret: bool = None) -> Any:
        """
        Calls :meth:`dict.items` on :attr:`iterable<Collection.iterable>` and converts the result to a
        :obj:`python:tuple` then returns the :obj:`python:tuple` as the tuple at the last index with
        :func:`operator.itemgetter`. Note that the :obj:`ItemsView<typing.ItemsView>` is converted to a
        :obj:`python:tuple` because ``ItemsViews`` are not subscriptable. Equivalent to::

            itemgetter(0)(tuple(dict(iterable).items))

        Args:
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        Raises:
            TypeError: Raised if either ``iterable`` is not structured in a way that can be converted to
                :obj:`dict` (e.g. is already a ``dict`` or subclass of ``dict`` (such as :obj:`collections.OrderedDict`)
                or a sequence of tuples each with two elements--with the element at position 0 being of a
                `hashable type <https://docs.python.org/3/glossary.html>`_)

        Args:
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def len(self, store: bool = None, ret: bool = None) -> int:
        """
        A proxy to :func:`python:len`. Equivalent to::

            len(iterable)

        Args:
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def list(self, store: bool = None, ret: bool = None) -> List:
        """
        Converts :attr:`iterable<Collection.iterable` to a :obj:`python:list` and returns the result. A proxy to
        :class:`python:list` with :attr:`iterable<Collection.iterable>` as the first argument, ``iterable``.
        Equivalent to::

            list(iterable)

        Args:
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def list_(self, store: bool = None, ret: bool = None)-> 'Collection':
        """
        Convert :attr:`iterable<Collection.iterable` to an :obj:`python:list` and store the result. An alias for
        :meth:`Collection.list(store=True, ret=False)<Collection.list>`. Equivalent to::

            list(iterable)

        Args:
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def map(self, func: Callable[[Any], Any], *iterables: Optional[Iterable], store: bool = None,
            ret: bool = None)-> 'Collection':
        """
        A proxy to :func:`python:map`. Equivalent to::

            map(func, iterable, *iterables)

        Args:
            func: A function to which each element of ``iterable`` and the elements of ``iterables`` are passed.
            *iterables: Additional iterables that are passes to ``func``.
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def map_items(self, func: Callable[[Hashable, Any], Any], *iterables: Optional[Iterable], store: bool = None,
                  ret: bool = None)-> 'Collection':
        """
        Calls :meth:`dict.items` before :func:`python:map`. Uses
        :func:`spread_tuple_parameter<utils.spread_tuple_parameter>` to facilitate spreading each element of the
        :obj:`ItemsView<typing.ItemsView>` into two parameters being passed to ``func``::

            lambda k, v: print('Key: {}, Value: {}'.format(k, v))

        Equivalent to::

            map(*spread_tuple_parameter(func), dict(iterable).items())

        Args:
            func: A function to which each element of ``iterable`` and the elements of ``iterables`` are passed.
            *iterables: Additional iterables that are passes to ``func``.
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def map_nt_items(self, func: Callable[[DictItem], Any], *iterables: Optional[Iterable], store: bool = None,
                       ret: bool = None)-> 'Collection':
        """
        Calls :meth:`dict.items` on :attr:`iterable<Collection.iterable>` and converts the resultant
        :obj:`ItemsView<typing.ItemsView>` to a list of :obj:`DictItems<utils.DictItem>` with
        :func:`utils.make_nt_items` then calls :func:`python:map`. Equivalent to::

            map(func, make_nt_items(dict(iterable).items()))

        Args:
            func: A function to which each element of ``iterable`` and the elements of ``iterables`` are passed.
            *iterables: Additional iterables that are passes to ``func``.
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def max(self, *args, key: Optional[Callable], default: Optional[Any], store: bool = None, ret: bool = None) -> int:
        """
        A proxy to :func:`python:max`. Equivalent to::

            max(iterable, *args, key=key, default=default)

        Args:
            args: An arbitrary number of positional arguments that will compared against themselves and ``iterable``
                to determine the maximum value.
            key: "Specifies a function of one argument that is used to extract a comparison key from each" element of
                iterable.
            default: The default value to be returned if ``iterable`` is empty.
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def min(self, *args, key: Optional[Callable], default: Optional[Any], store: bool = None, ret: bool = None) -> int:
        """
        A proxy to :func:`python:min`. Equivalent to::

            min(iterable, *args, key=key, default=default)

        Args:
            args: An arbitrary number of positional arguments that will compared against themselves and ``iterable``
                to determine the minimum value.
            key: "Specifies a function of one argument that is used to extract a comparison key from each" element of
                iterable.
            default: The default value to be returned if ``iterable`` is empty.
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def next(self, store: bool = None, ret: bool = None) -> Any:
        """
        Converts :attr:`iterable<Collection.iterable>` to an :obj:`typing.Iterator` and passes it to :func:`python:next`
        Equivalent to::

            next(iter(iterable))

        Args:
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def nt_items(self, store: bool = None, ret: bool = None)-> 'Collection':
        """
        Calls :meth:`dict.items` on :attr:`iterable<Collection.iterable>` and converts the resultant
        :obj:`ItemsView<typing.ItemsView>` to a list of :obj:`DictItems<utils.DictItem>` with
        :func:`utils.make_nt_items`. Equivalent to::

            make_nt_items(dict(iterable).items())

        Args:
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def ordered_dict(self, store: bool = None, ret: bool = None, **kwargs) -> OrderedDict:
        """
        A proxy to :obj:`collections.OrderedDict`. Equivalent to::

            OrderedDict(iterable)

        Args:
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.
            **kwargs: Additional keyword arguments that will be added to the resultant :obj:`python:dict`.

        """
    def pop(self, i: Optional[int], store: bool = None, ret: bool = None) -> Any:
        """
        Converts :attr:`iterable<Collection.iterable>` to a :obj:`python:list` then passes it to :meth:`list.pop`.
        Equivalent to::

            list(iterable).pop()

        Args:
            i: Index to pop, if not given the index is popped.
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def reduce(self, func: Callable[[Any, Any], Any], initializer: Optional[Any], store: bool = None,
               ret: bool = None) -> Any:
        """
        A proxy to :func:`python:reduce`. Equivalent to::

            reduce(func, iterable, initializer=initializer)

        Args:
            func: A "function of two arguments cumulatively to the items of iterable, from left to right, so as to
                reduce the iterable to a single value."
            initializer: "If the optional initializer is present, it is placed before the items of the iterable in the
                calculation, and serves as a default when the iterable is empty. If initializer is not given and
                iterable contains only one item, the first item is returned."
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def reduce_items(self, func: Callable[[Any, Hashable, Any], Any], initializer: Optional[Any], store: bool = None,
                          ret: bool = None) -> Any:
        """
        Calls :meth:`dict.items` before :func:`python:reduce`. Uses
        :func:`spread_tuple_parameter<utils.spread_tuple_parameter>` to facilitate spreading each element of the
        :obj:`ItemsView<typing.ItemsView>` into two parameters being passed to ``func``::

            lambda k, v: print('Key: {}, Value: {}'.format(k, v))

        Equivalent to::

            reduce(*spread_tuple_parameter(func), dict(iterable).items())

        Args:
            func: A "function of two arguments cumulatively to the items of iterable, from left to right, so as to
                reduce the iterable to a single value."
            initializer: "If the optional initializer is present, it is placed before the items of the iterable in the
                calculation, and serves as a default when the iterable is empty. If initializer is not given and
                iterable contains only one item, the first item is returned."
            ret:
            store:

        """
    def reduce_nt_items(self, func: Callable[[Any, DictItem], Any], initializer: Optional[Any], store: bool = None,
                          ret: bool = None) -> Any:
        """
        Calls :meth:`dict.items` on :attr:`iterable<Collection.iterable>` and converts the resultant
        :obj:`ItemsView<typing.ItemsView>` to a list of :obj:`DictItems<utils.DictItem>` with
        :func:`utils.make_nt_items` then calls :func:`python:reduce`. Equivalent to::

            reduce(func, make_nt_items(dict(iterable).items()))

        Args:
            func: A "function of two arguments cumulatively to the items of iterable, from left to right, so as to
                reduce the iterable to a single value."
            initializer: "If the optional initializer is present, it is placed before the items of the iterable in the
                calculation, and serves as a default when the iterable is empty. If initializer is not given and
                iterable contains only one item, the first item is returned."
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def reversed(self, store: bool = None, ret: bool = None)-> 'Collection':
        """
        A proxy to :func:`python:reversed`. Equivalent to::

            reversed(iterable)

        Args:
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def set(self, store: bool = None, ret: bool = None) -> Set:
        """
        Converts :attr:`iterable<Collection.iterable` to a :obj:`python:set` and returns the result. A proxy to
        :class:`python:set` with :attr:`iterable<Collection.iterable>` as the first argument, ``iterable``.
        Equivalent to::

            set(iterable)

        Args:
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def set_(self, store: bool = None, ret: bool = None)-> 'Collection':
        """
        Convert :attr:`iterable<Collection.iterable` to an :obj:`python:set` and store the result. An alias for
        :meth:`Collection.set(store=True, ret=False)<Collection.set>`. Equivalent to::

            set(iterable)

        Args:
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def setitem(self, b: Hashable, c: Any, store: bool = None, ret: bool = None)-> 'Collection':
        """
        A proxy to :func:`operator.setitem` with :attr:`iterable<Collection.iterable` as the ``a`` argument.
        Equivalent to::

            setitem(iterable, b, c)

        Args:
            b: The key or index to be set on ``iterable``.
            c: The value to be set to key or index ``b``.
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def slice(self, start: int, stop: int, step: Optional[int], store: bool = None, ret: bool = None)-> 'Collection':
        """
        A proxy to :func:`operator.getitem` with :attr:`iterable<Collection.iterable` as ``a`` and a :obj:`python:slice`
        object as ``b``. Equivalent to::

            getitem(iterable, slice(stop))

            # Or...

            getitem(iterable, slice(start, stop, step=step))

        Args:
            start: The start position of the slice.
            stop: The stop position of the slice.
            step: The stop for the slice.
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def sorted(self, key: Optional[Callable], reverse: bool = False, store: bool = None,
               ret: bool = None)-> 'Collection':
        """
        A proxy to :func:`python:sorted`. Equivalent to::

            sorted(iterable, key=key, reverse=reverse)

        Args:
            key: "Specifies a function of one argument that is used to extract a comparison key from each" element of
                iterable.
            reverse: Should ``iterable`` be reversed.
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def tuple(self, store: bool = None, ret: bool = None) -> Tuple:
        """
        Converts :attr:`iterable<Collection.iterable` to a :obj:`python:tuple` and returns the result. A proxy to
        :class:`python:tuple` with :attr:`iterable<Collection.iterable>` as the first argument, ``iterable``.
        Equivalent to::

            tuple(iterable)

        Args:
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def tuple_(self, store: bool = None, ret: bool = None)-> 'Collection':
        """
        Convert :attr:`iterable<Collection.iterable` to an :obj:`python:tuple` and store the result. An alias for
        :meth:`Collection.tuple(store=True, ret=False)<Collection.tuple>`. Equivalent to::

            tuple(iterable)

        Args:
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def unique(self, store: bool = None, ret: bool = None)-> 'Collection':
        """
        An alias for :meth:`Collection.set`

        Args:
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """
    def zip(self, *iterables: Iterable, store: bool = None, ret: bool = None)-> 'Collection':
        """
        A proxy to :func:`python:zip`. Equivalent to::

            zip(iterable, *iterables)

        Args:
            iterables: An arbitrary number of iterables that will be zipped together.
            store: Store the result of the operation to the :attr:`iterable<Collection.iterable>` property.
            ret: Return the result of the operation instead of `self`.

        """

def collect(iterable: Iterable) -> Collection:
    """
    Returns a :obj:`Collection` object containing ``iterable``. Uses
    :obj:`DefaultMethodStrategyFactory<iterable_collections.factory.DefaultMethodStrategyFactory>`.

    Args:
        iterable: The Iterable type object :obj:`Collection` wraps around.
    """