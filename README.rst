====================
Iterable Collections
====================

This package is inspired heavily by `Martin Fowler's Collection Pipeline pattern`_, and also by my first interaction
with this pattern--`Laravel's Collections in PHP`_. This is meant to be a versatile and extensible implementation of
the Collection Pipeline pattern that leverages Python's builtin functionality to provide a clearer, more legible
implementation than usage of builtins alone provides. In other words, this package is born of the belief that this
is more difficult to decipher::

    foo = list(filter(lambda y: y > 4, map(lambda x: x * 2, [1, 2, 3, 4])))

Than this::

    foo = collect([1, 2, 3, 4]).map(lambda x: x * 2) \
        .filter(lambda y: y > 4) \
        .list()

**HOWEVER** if you're only going to be working with Sequences, if you would like to connect directly to a data source,
if you are concerned with maintaining your data in an immutable chain, or if you prefer the syntax of Linq or Scala
(and don't feel like taking the time to implement it yourself with the tools provided in this package), I would highly
suggest you use `PyFunctional`_. It's a much more mature, more well conceived, and time tested package that provides
the same object oriented pipeline interface. Where these packages differ is in their intentions. As stated clearly in
`this Github issue`_, PyFunctional is built around these concepts:

- Constructing a lineage chain (functions that take an iterable and return one, or actions)

- Applying it to a base collection via the iterator interface, the base collection is also forced to be a list.

Iterable Collections was made with Dicts and other Mappings in mind--which is not to purport any superiority, just to
state they were conceived for different purposes. Because of the desire to work with Mappings, the desire for an easily
extendable interface, and the desire leverage builtins in a pipeline interface, I decided
there was room for a similar package.

Python 2.7 Support
------------------

There is currently no support for Python 2.7. That may be addressed in the future, but at the moment it is not a
priority.


Usage
-----

Basic usage of transformational methods::

    from iterable_collections import collect


    # map
    collect([1, 2, 3, 4]).map(lambda x: x + 2) \
        .list() # [3, 4, 5, 6]

    # filter
    collect([1, 2, 3, 4]).filter(lambda x: x > 2) \
        .list() # [3, 4]

    # groupby
    collect([{'a': 1, 'b': 2}, {'a': 1, 'b': 3}, {'a': 1, 'b': 2}]).sorted(key=lambda x: x['b']) \
        .groupby(key=lambda x: x['b'])
        .map(lambda x: (x[0], list(x[1]))) # We're using map here because the results of groupby are in iterators
        .list() # [(2, [{'a': 1, 'b': 2}, {'a': 1, 'b': 2}]), (3, [{'a': 1, 'b': 3}])]

    # reduce
    collect([1, 2, 3, 4]).reduce(lambda t, x: t + x) # 10

    # flatten
    collect([[1, 2], [3, 4]]).flatten() \
        .list() # [1, 2, 3, 4]

There are two approaches that can be used with Mappings: the ``*_items`` and ``*_nt_items`` methods, such as
``map_items`` and ``map_nt_items``. The ``*_items`` methods implicitly call ``dict.items`` on the
``Collection.iterable`` property which results in a Mapping View containing key value pairs. These methods accept a two
argument function instead of the usual one argument function used by ``map``::

    collect({'a': 1, 'b': 2, 'c': 3, 'd': 4}).map_items(lambda k, v: (k, v + 2)) \
        .dict() # {'a': 3, 'b': 4, 'c': 5, 'd': 6}

Also available are the ``*_nt_items`` methods. These methods also implicitly call ``dict.items``, but instead of
spreading the keys and values into two arguments, they create a ``namedtuple`` that has ``key`` and ``value``
attributes::

    collect({'a': 1, 'b': 2, 'c': 3, 'd': 4}).map_nt_items(lambda x: (x.key, x.value + 2)) \
        .dict() # {'a': 3, 'b': 4, 'c': 5, 'd': 6}

There ``*_items`` and ``*_nt_items`` available for the transformational methods: filter, map, and reduce. Additionally
the ``first`` and ``last`` methods have ``*_items`` and ``*_nt_items`` versions::

    # first
    collect([1, 2, 3, 4]).first() # 1

    # last
    collect([1, 2, 3, 4]).last() # 4

    # first_item
    collect({'a': 1, 'b': 2, 'c': 3, 'd': 4}).first_item() # ('a', 1)

    # last_item
    collect({'a': 1, 'b': 2, 'c': 3, 'd': 4}).last_item() # ('d', 4)

    # first_nt_item
    collect({'a': 1, 'b': 2, 'c': 3, 'd': 4}).first_nt_item() # DictItem(key='a', value=1)

    # last_nt_item
    collect({'a': 1, 'b': 2, 'c': 3, 'd': 4}).last_nt_item() # DictItem(key='d', value=4)

Extensibility
-------------

Each method on the ``Collection`` object is defined by a ``MethodStrategy``. These objects utilize a Callable object
and a series of other strategies to compose all the functionality encapsulated by a method. As defined in the
``MethodStrategy`` class, the process of encapsulating the functionality of a method can be characterized with six
phases:

1. **Pre-Processing:** A series of operations are performed on the ``Collection.iterable`` property. Typically
``iterable`` is converted into some desired format or type.

2. **Argument Formatting:** Format the arguments passed to the method. Also in this phase, typically arguments are
formatted into some desired format or type.

3. **Argument Binding:** Bind the arguments to desired positions in the Callable's signature.

4. **Execution:** The Callable object is called, performing the core functionality of the method--may result in errors.

5. **Result Handling:** Determine what should be done with the result of the Callable. Basic behavior is either storing
the result to the ``Collection.iterable`` property or preserving it's original value.

6. **Return Value:** Determine what value should be returned from the method. Basic behavior is either the result of
the Callable or the current ``Collection`` instance.


In order to determine the behaviors invoked in each of these phases, ``MethodStrategy`` is initialized with the method's
name as a ``str``, a Callable object, and a number of objects that implement interfaces which abstract the various
phases.

- ``PreProcessingStrategyInterface``

- ``ArgumentFormattingStrategyInterface``

- ``ArgumentBindingStrategyInterface``

- ``ErrorHandlingStrategyInterface`` (Handles any errors that occur during the Execution phase)

- ``ResultStrategyInterface``

- ``ReturnValueStrategyInterface``

An illustrative example of how these would be implemented can be seen in the definition of ``Collection.first_item``::

    MethodStrategy(
        'first_item', # name of the method
        operator.itemgetter(0), # the Callable object
        StoreIterableStrategy(), # Result Handling phase
        ReturnResultStrategy(), # Return Value phase
        PartialIterableBindingStrategy(), # Argument Binding phase
        UnformattedArgumentFormattingStrategy(), # Argument Formatting phase
        PreProcessingStrategy((
            {'name': 'items', 'args': (), 'kwargs': {}},
            {'name': 'tuple', 'args': (), 'kwargs': {'store': True}}
        )), # Pre-Processing phase
        GetItemErrorHandlingStrategy() # Error handling during Execution phase
    ),

All of these interfaces can be implemented in several different ways. The implementations found in the
``iterable_collections.strategy`` module are only those needed for the base cannon of methods. ``Collection.first_item``
is a good demonstration of how to leverage Python's builtin functionality. However if the Callable argument needs
custom behavior, ``MethodStrategy`` can be extended, as in ``ConcatMethodStrategy``::

    class ConcatMethodStrategy(MethodStrategy):
        def __init__(
                self,
                name,
                result_strategy,
                return_strategy,
                iterable_binding_strategy,
                argument_formatting_strategy,
                pre_process_strategy,
                error_strategy
        ):
            super().__init__(
                name,
                getattr(self, name),
                result_strategy,
                return_strategy,
                iterable_binding_strategy,
                argument_formatting_strategy,
                pre_process_strategy,
                error_strategy
            )

        def concat(self, instance, *args):
            for a in args:
                if not isinstance(a, Iterable):
                    raise TypeError('Must an iterable type.')
                if isinstance(a, (Set, Sequence, MappingView)):
                    instance.concat_seq(a)
                if isinstance(a, Mapping):
                    instance.concat_dict(a)
                if isinstance(a, Iterator):
                    instance.concat_iter(a)
            return instance.iterable

        def concat_dict(self, iterable, other):
            iterable.update(other)
            return iterable

        def concat_iter(self, iterable, other):
            return itertools.chain(iterable, other)

        def concat_seq(self, iterable, other):
            return operator.concat(iterable, other)


Different types are concatenated in different ways, so methods are defined for Mappings, Iterators, and Sequences. A
universal method ``concat`` determines which of these methods to call based on the type of each argument. Notice though
that the methods are being called on ``instance`` which is the current instance of the ``Collection`` object (i.e.
``self`` in ``Collection``.). By calling these on the instance, any pre-processing, argument formatting, etc... will
take place. This would not happen if these methods were called in this way, ``self.concat_dict(instance.iterable, a)``.


However to call methods this way, they must have been defined before the ``Collection`` object was instantiated.
``Collection`` is initialized with an Iterable and a ``StrategyDict``, which is a Mapping of ``str`` method names to
objects implementing the ``MethodStrategyInterface``. The included ``StrategyDict`` is created using
``DefaultMethodStrategyFactory`` defined in ``iterable_collections.factory``. The ``collect`` function creates a factory
object and then uses it to create the ``StrategyDict`` injected into ``Collection``. Below is an excerpt of
``DefaultMethodStrategyFactory``::

    class DefaultMethodStrategyFactory(MethodStrategyFactoryInterface):
        def create(self):
            return {s.name: s for s in self.get_strategies()} # Converts the Tuple of MethodStrategyInterface object
                                                              # into a Dict.

        def get_strategies(self): # Returns a Tuple of MethodStrategyInterface objects
            return (
                MethodStrategy(
                    'all',
                    builtins.all,
                    StoreIterableStrategy(),
                    ReturnResultStrategy(),
                    PartialIterableBindingStrategy(),
                    UnformattedArgumentFormattingStrategy(),
                    PreProcessingStrategy(),
                    BaseExceptionErrorHandlingStrategy()
                ),
                MethodStrategy(
                    'any',
                    builtins.any,
                    StoreIterableStrategy(),
                    ReturnResultStrategy(),
                    PartialIterableBindingStrategy(),
                    UnformattedArgumentFormattingStrategy(),
                    PreProcessingStrategy(),
                    BaseExceptionErrorHandlingStrategy()
                ),
                ChunksMethodStrategy( # A child class of MethodStrategy that breaks iterables into chunks.
                    'chunks',
                    StoreResultStrategy(),
                    ReturnInstanceStrategy(),
                    PartialInstanceBindingStrategy(),
                    UnformattedArgumentFormattingStrategy(),
                    PreProcessingStrategy(),
                    BaseExceptionErrorHandlingStrategy()
                ),
    ...

Future
------

Depending on how this received, future plans may include:

- Extensibility through configurations.
- Event driven extensibility.
- Python 2.7 support. (Though not likely unless there is demand.)
- I don't know... You got any ideas?


.. _Martin Fowler's Collection Pipeline pattern: https://martinfowler.com/articles/collection-pipeline/
.. _Laravel's Collections in PHP: https://laravel.com/docs/5.6/collections
.. _PyFunctional: https://github.com/EntilZha/PyFunctional
.. _this Github issue: https://github.com/EntilZha/PyFunctional/issues/108