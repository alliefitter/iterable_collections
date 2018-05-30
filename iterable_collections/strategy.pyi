from abc import ABC, abstractmethod
from typing import Callable, Iterable, Any, Dict, Tuple, Sequence, Iterator, Union

from iterable_collections.collection import Collection


class MethodStrategyInterface(ABC):
    """
    Encapsulates the functionality of a method on a :obj:`Collection<iterable_collections.collection.Collection>` by
    using other strategy objects.
    """
    @abstractmethod
    def make_method(self, instance: Collection) -> Callable:
        """
        Creates a function that is returned to the :obj:`Collection<iterable_collections.collection.Collection>` instance
        providing an instance method.

        Args:
            instance: An instance of :obj:`Collection<iterable_collections.collection.Collection>`.

        """


class ResultStrategyInterface(ABC):
    """
    Determines how the result of an operation is used, such as whether it should be stored, returned, or
    modified in some way.
    """
    @abstractmethod
    def handle_result(self, result: Any, iterable: Iterable, store: bool = None) -> Union[Any, Iterable]:
        """

        Args:
            result: The result returned from an operation.
            iterable: An iterable contained in a :obj:`Collection<iterable_collections.collection.Collection>` object.
            store: An optional keyword argument which can override default behavior.
        """


class ReturnValueStrategyInterface(ABC):
    """
    Determines what value is returned from a method.
    """
    @abstractmethod
    def return_value(self, instance: Collection, result: Any, ret: bool = None) -> Union[Any, Collection]:
        """

        Args:
            instance: An instance of :obj:`Collection<iterable_collections.collection.Collection>`.
            result: The result returned from an operation.
            ret: An optional keyword argument which can override default behavior.

        """


class PreProcessingStrategyInterface(ABC):
    """
    Performs a list of operations that must be performed before the method can be called.
    Typically this is used to coerce the type or format of an :obj:`iterable<collection.collection.Collection.iterable>`.
    """
    operations: Tuple[Dict[str, Union[str, Tuple, Dict]]] = ...
    @abstractmethod
    def pre_process(self, instance: Collection) -> None:
        """

        Args:
            instance: An instance of :obj:`Collection<iterable_collections.collection.Collection>`.

        """


class ArgumentFormattingStrategyInterface(ABC):
    """
    Formats the arguments of the method in some desired way, for instance by ensuring that an argument is of
    a certain type.
    """
    @abstractmethod
    def format(self, *args, **kwargs) -> Tuple[Tuple, Dict]:
        """

        Args:
            *args: Positional arguments passed to the method.
            **kwargs: Keyword arguments passed to the method.

        """


class ArgumentBindingStrategyInterface(ABC):
    """
    Binds an argument to function that performs operation of the method.
    """
    @abstractmethod
    def bind(self, func: Callable, instance: Collection) -> Callable:
        """

        Args:
            func: The function that performs the primary functionality of the method.
            instance: An instance of :obj:`Collection<iterable_collections.collection.Collection>`.

        """



class ErrorHandlingStrategyInterface(ABC):
    """
    Determines how errors that occur during execution of the method are handled.
    """
    @abstractmethod
    def get_error(self) -> Union[BaseException, Tuple[BaseException]]:
        """
        Returns errors which may occur during execution of the method.

        """

    @abstractmethod
    def handle(self, error: BaseException) -> BaseException:
        """
        Returns an error to be raised.

        Args:
            error: An error which occurred during execution of the method.

        """


class BaseExceptionErrorHandlingStrategy(ErrorHandlingStrategyInterface):
    """
    Handles any error and returns the error raised during execution of the method.
    """
    def get_error(self) -> BaseException:
        """
        Returns errors which may occur during execution of the method.

        """

    def handle(self, error) -> BaseException:
        """
        Returns an error to be raised.

        Args:
            error: An error which occurred during execution of the method.

        """


class ConvertToDictErrorHandlingStrategy(ErrorHandlingStrategyInterface):
    """
    Handles errors that may occur when converting an object to a :obj:`dict`.
    """
    def get_error(self) -> Tuple[TypeError, ValueError]:
        """
        Returns errors which may occur during execution of the method.

        """

    def handle(self, error: Union[TypeError, ValueError]) -> ValueError:
        """
        Returns an error to be raised.

        Args:
            error: An error which occurred during execution of the method.

        """


class GetItemErrorHandlingStrategy(ErrorHandlingStrategyInterface):
    """
    Handles errors that may occur when retrieving an item from object using :func:`operator.getitem`.
    """
    def get_error(self) -> Tuple[KeyError, TypeError, IndexError]:
        """
        Returns errors which may occur during execution of the method.

        """

    def handle(self, error: Union[KeyError, TypeError, IndexError]) -> Union[KeyError, TypeError, IndexError]:
        """
        Returns an error to be raised.

        Args:
            error: An error which occurred during execution of the method.

        """


class SetItemErrorHandlingStrategy(ErrorHandlingStrategyInterface):
    """
    Handles errors that may occur when using :func:`operator.setitem`.
    """
    def get_error(self) -> TypeError:
        """
        Returns errors which may occur during execution of the method.

        """

    def handle(self, error: TypeError) -> TypeError:
        """
        Returns an error to be raised.

        Args:
            error: An error which occurred during execution of the method.

        """


class StoreResultStrategy(ResultStrategyInterface):
    """
    Store the result of an operation to :obj:`iterable<collection.collection.Collection.iterable>`.
    """
    def handle_result(self, result: Any, iterable: Iterable, store: bool = None) -> Union[Any, Iterable]:
        """

        Args:
            result: The result returned from an operation.
            iterable: An iterable contained in a :obj:`Collection<iterable_collections.collection.Collection>` object.
            store: An optional keyword argument which can override default behavior.
        """


class StoreIterableStrategy(ResultStrategyInterface):
    """
    Store the unmodified Iterable to :obj:`iterable<collection.collection.Collection.iterable>`.
    """
    def handle_result(self, result: Any, iterable: Iterable, store: bool = None) -> Union[Any, Iterable]:
        """

        Args:
            result: The result returned from an operation.
            iterable: An iterable contained in a :obj:`Collection<iterable_collections.collection.Collection>` object.
            store: An optional keyword argument which can override default behavior.
        """


class ReturnInstanceStrategy(ReturnValueStrategyInterface):
    """
    Return an instance of :obj:`Collection<iterable_collections.collection.Collection>` from the method.
    """
    def return_value(self, instance: Collection, result: Any, ret: bool = None) -> Union[Any, Collection]:
        """

        Args:
            instance: An instance of :obj:`Collection<iterable_collections.collection.Collection>`.
            result: The result returned from an operation.
            ret: An optional keyword argument which can override default behavior.

        """


class ReturnResultStrategy(ReturnValueStrategyInterface):
    """
    Return the result of an operation.
    """
    def return_value(self, instance: Collection, result: Any, ret: bool = None) -> Union[Any, Collection]:
        """

        Args:
            instance: An instance of :obj:`Collection<iterable_collections.collection.Collection>`.
            result: The result returned from an operation.
            ret: An optional keyword argument which can override default behavior.

        """


class PartialIterableBindingStrategy(ArgumentBindingStrategyInterface):
    """
    Bind :obj:`iterable<collection.collection.Collection.iterable>` to the first argument of a function.
    """
    def bind(self, func: Callable, instance: Collection) -> Callable:
        """

        Args:
            func: The function that performs the primary functionality of the method.
            instance: An instance of :obj:`Collection<iterable_collections.collection.Collection>`.

        """


class RightPartialIterableBindingStrategy(ArgumentBindingStrategyInterface):
    """
    Bind :obj:`iterable<collection.collection.Collection.iterable>` to the right most argument of a function.
    """
    def bind(self, func: Callable, instance: Collection) -> Callable:
        """

        Args:
            func: The function that performs the primary functionality of the method.
            instance: An instance of :obj:`Collection<iterable_collections.collection.Collection>`.

        """

class PartialAtPositionIterableBindingStrategy(ArgumentBindingStrategyInterface):
    """
    Bind :obj:`iterable<collection.collection.Collection.iterable>` to the argument at the specified position.
    """
    position: int = ...
    def __init__(self, position: int = 0):
        """

        Args:
            position: The position at which :obj:`iterable<collection.collection.Collection.iterable>`
                should be bound.
        """

    def bind(self, func: Callable, instance: Collection) -> Callable:
        """

        Args:
            func: The function that performs the primary functionality of the method.
            instance: An instance of :obj:`Collection<iterable_collections.collection.Collection>`.

        """


class PartialInstanceBindingStrategy(ArgumentBindingStrategyInterface):
    """
    Bind an instance of :obj:`Collection<iterable_collections.collection.Collection>` the first argument of a function.
    """
    def bind(self, func: Callable, instance: Collection) -> Callable:
        """

        Args:
            func: The function that performs the primary functionality of the method.
            instance: An instance of :obj:`Collection<iterable_collections.collection.Collection>`.

        """


class PreProcessingStrategy(PreProcessingStrategyInterface):
    """
    Execute an arbitrary number of methods of a :obj:`Collection<iterable_collections.collection.Collection>` object.

    """
    def __init__(self, operations: Tuple = ()):
        """

        Args:
            operations: A :obj:`tuple` containing an arbitrary number of of operations.
                Format::

                    operation = (
                        {
                            'name': (str) The name of the method.
                            'args': (tuple) Positional arguments.
                            'kwargs': (dict) Keyword arguments
                        },
                        ...
                    )
        """

    def pre_process(self, instance: Collection) -> None:
        """

        Args:
            instance: An instance of :obj:`Collection<iterable_collections.collection.Collection>`.

        """


class UnformattedArgumentFormattingStrategy(ArgumentFormattingStrategyInterface):
    """
    Do not format the method's arguments in any way.
    """
    def format(self, *args, **kwargs) -> Tuple[Tuple, Dict]:
        """

        Args:
            *args: Positional arguments passed to the method.
            **kwargs: Keyword arguments passed to the method.

        """


class ConvertToDictArgumentFormattingStrategy(ArgumentFormattingStrategyInterface):
    """
    Convert the argument at ``position`` to :obj:`dict`.
    """
    error_strategy: ConvertToDictErrorHandlingStrategy = ...
    position: int = ...
    def __init__(self, error_strategy: ConvertToDictErrorHandlingStrategy, position: int = 0):
        """

        Args:
            error_strategy: Handles errors that may occur when converting an argument to a :obj:`dict`.
            position: The position of the argument that should be converted.
        """

    def format(self, *args, **kwargs) -> Tuple[Tuple, Dict]:
        """

        Args:
            *args: Positional arguments passed to the method.
            **kwargs: Keyword arguments passed to the method.

        """


class ConvertDictItemsToSetArgumentFormattingStrategy(ArgumentFormattingStrategyInterface):
    """
    After converting the argument at ``position`` to a :obj:`dict` and calling :meth:`dict.items`,
    convert the argument to a :obj:`set`.
    """
    dict_strategy: ConvertToDictArgumentFormattingStrategy = ...
    position: int = ...
    def __init__(self, dict_strategy: ConvertToDictArgumentFormattingStrategy, position: int = 0):
        """

        Args:
            dict_strategy: Converts an argument to a :obj:`dict`.
            position: The position of the argument that should be converted.
        """

    def format(self, *args, **kwargs) -> Tuple[Tuple, Dict]:
        """

        Args:
            *args: Positional arguments passed to the method.
            **kwargs: Keyword arguments passed to the method.

        """


class ConvertToIterArgumentFormattingStrategy(ArgumentFormattingStrategyInterface):
    """
    Convert the argument at ``position`` to :obj:`iter`.
    """
    def __init__(self, position: int = 0):
        """

        Args:
            position: The position of the argument that should be converted.
        """

    def format(self, *args, **kwargs) -> Tuple[Tuple, Dict]:
        """

        Args:
            *args: Positional arguments passed to the method.
            **kwargs: Keyword arguments passed to the method.

        """


class ConvertToListArgumentFormattingStrategy(ArgumentFormattingStrategyInterface):
    """
    Convert the argument at ``position`` to :obj:`list`.
    """
    position: int = ...
    def __init__(self, position: int = 0):
        """

        Args:
            position: The position of the argument that should be converted.
        """

    def format(self, *args, **kwargs) -> Tuple[Tuple, Dict]:
        """

        Args:
            *args: Positional arguments passed to the method.
            **kwargs: Keyword arguments passed to the method.

        """


class ConvertToSetArgumentFormattingStrategy(ArgumentFormattingStrategyInterface):
    """
    Convert the argument at ``position`` to :obj:`set`.
    """
    position: int = ...
    def __init__(self, position: int = 0):
        """

        Args:
            position: The position of the argument that should be converted.
        """

    def format(self, *args, **kwargs) -> Tuple[Tuple, Dict]:
        """

        Args:
            *args: Positional arguments passed to the method.
            **kwargs: Keyword arguments passed to the method.

        """


class SpreadTupleParameterArgumentFormattingStrategy(ArgumentFormattingStrategyInterface):
    position: int = ...
    callable_position: int = ...
    def __init__(self, position: int = 0, callable_position: int = 0):
        """

        Args:
            position: The position of the argument that should be converted, which should be a
                :obj:`Callable<typing.Callable>`.
            callable_position: The position in the :obj:`Callable<typing.Callable>` of the tuple that
                should be spread into two arguments.
        """

    def format(self, *args, **kwargs) -> Tuple[Tuple, Dict]:
        """

        Args:
            *args: Positional arguments passed to the method.
            **kwargs: Keyword arguments passed to the method.

        """


class MethodStrategy(MethodStrategyInterface):
    """
    Encapsulates the functionality of a method on a :obj:`Collection<iterable_collections.collection.Collection>` by
    using other strategy objects.

    """
    name: str = ...
    callable: Callable = ...
    result_strategy: ResultStrategyInterface = ...
    return_strategy: ReturnValueStrategyInterface = ...
    iterable_binding_strategy: ArgumentBindingStrategyInterface = ...
    argument_formatting_strategy: ArgumentFormattingStrategyInterface = ...
    pre_process_strategy: PreProcessingStrategyInterface = ...
    error_strategy: ErrorHandlingStrategyInterface = ...
    def __init__(
            self,
            name: str,
            callable_: Callable,
            result_strategy: ResultStrategyInterface,
            return_strategy: ReturnValueStrategyInterface,
            argument_binding_strategy: ArgumentBindingStrategyInterface,
            argument_formatting_strategy: ArgumentFormattingStrategyInterface,
            pre_process_strategy: PreProcessingStrategyInterface,
            error_strategy: ErrorHandlingStrategyInterface,

    ):
        """

        Args:
            name: The name of the method.
            callable_: The :obj:`Callable<typing.Callable>` object that contains the method's primary functionality.
            result_strategy: Determines what should be saved to :obj:`iterable<collection.collection.Collection.iterable>`.
            return_strategy: Determines what is returned from the method.
            argument_binding_strategy: Determines what object should be bound to
                :meth:`callable<MethodStrategy.callable>` and in what position.
            argument_formatting_strategy: Formats the arguments that passed to :meth:`callable<MethodStrategy.callable>`.
            pre_process_strategy: Performs a series of operations before executing
                :meth:`callable<MethodStrategy.callable>`
            error_strategy: Handles errors that occur during execution of the method.

        """

    def make_method(self, instance: Collection) -> Callable:
        """
        Creates a function using various strategies to incorporate desired functionality. The function
        is then used a method on a :obj:`iterable<collection.collection.Collection.iterable>` object.

        Args:
            instance: An instance of :obj:`iterable<collection.collection.Collection.iterable>`

        """


class ConcatMethodStrategy(MethodStrategy):
    """
    :obj:`MethodStrategy` containing functionality for concatenating objects.
    """
    def __init__(
            self,
            name: str,
            result_strategy: ResultStrategyInterface,
            return_strategy: ReturnValueStrategyInterface,
            argument_binding_strategy: ArgumentBindingStrategyInterface,
            argument_formatting_strategy: ArgumentFormattingStrategyInterface,
            pre_process_strategy: PreProcessingStrategyInterface,
            error_strategy: ErrorHandlingStrategyInterface
    ):

        """

        Args:
            name: The name of the method.
            result_strategy: Determines what should be saved to :obj:`iterable<collection.collection.Collection.iterable>`.
            return_strategy: Determines what is returned from the method.
            argument_binding_strategy: Determines what object should be bound to
                :meth:`callable<MethodStrategy.callable>` and in what position.
            argument_formatting_strategy: Formats the arguments that passed to :meth:`callable<MethodStrategy.callable>`.
            pre_process_strategy: Performs a series of operations before executing
                :meth:`callable<MethodStrategy.callable>`
            error_strategy: Handles errors that occur during execution of the method.

        """

    def concat(self, instance: Collection, *args) -> Iterable:
        ...

    def concat_dict(self, iterable: Dict, other: Dict) -> Iterable:
        ...

    def concat_iter(self, iterable: Iterator, other: Iterator) -> Iterable:
        ...

    def concat_seq(self, iterable: Sequence, other: Sequence) -> Iterable:
        ...


class DiffMethodStrategy(MethodStrategy):
    """
    :obj:`MethodStrategy` containing functionality for calculating the difference of two objects.
    """
    def __init__(
            self,
            name: str,
            result_strategy: ResultStrategyInterface,
            return_strategy: ReturnValueStrategyInterface,
            argument_binding_strategy: ArgumentBindingStrategyInterface,
            argument_formatting_strategy: ArgumentFormattingStrategyInterface,
            pre_process_strategy: PreProcessingStrategyInterface,
            error_strategy: ErrorHandlingStrategyInterface

    ):
        ...

    def diff(self, instance: Collection, other: Iterable) -> Iterable:
        ...


class FlattenMethodStrategy(MethodStrategy):
    """
    :obj:`MethodStrategy` containing functionality for flattening nested sequences.
    """
    def __init__(
            self,
            name: str,
            result_strategy: ResultStrategyInterface,
            return_strategy: ReturnValueStrategyInterface,
            argument_binding_strategy: ArgumentBindingStrategyInterface,
            argument_formatting_strategy: ArgumentFormattingStrategyInterface,
            pre_process_strategy: PreProcessingStrategyInterface,
            error_strategy: ErrorHandlingStrategyInterface
    ):
        ...

    def flatten(self, iterable: Iterable) -> Iterable:
        ...


class IntersectMethodStrategy(MethodStrategy):
    """
    :obj:`MethodStrategy` containing functionality for calculating the intersect of two iterables.
    """
    def __init__(
            self,
            name: str,
            result_strategy: ResultStrategyInterface,
            return_strategy: ReturnValueStrategyInterface,
            argument_binding_strategy: ArgumentBindingStrategyInterface,
            argument_formatting_strategy: ArgumentFormattingStrategyInterface,
            pre_process_strategy: PreProcessingStrategyInterface,
            error_strategy: ErrorHandlingStrategyInterface

    ):
        ...

    def intersect(self, instance: Collection, target: Iterable) -> Iterable:
        ...


class SortedAndGroupbyMethodStrategy(MethodStrategy):
    """
    Provides a shortcut to sort an iterable then group it's contents using a ``key`` function.
    """
    def __init__(
            self,
            name: str,
            result_strategy: ResultStrategyInterface,
            return_strategy: ReturnValueStrategyInterface,
            argument_binding_strategy: ArgumentBindingStrategyInterface,
            argument_formatting_strategy: ArgumentFormattingStrategyInterface,
            pre_process_strategy: PreProcessingStrategyInterface,
            error_strategy: ErrorHandlingStrategyInterface

    ):
        ...

    def group_sort(self, instance: Collection, key: Callable = None) -> Iterable:
        ...

class ChunksMethodStrategy(MethodStrategy):
    """
    Breaks ``iterable`` into chunks of ``length`` sized lists.
    """
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
        ...

    def chunks(self, instance: Collection, length: int) -> Iterable:
        ...

    def chunks_dict(self, iterable: Dict, length: int) -> Iterable:
        ...

    def chunks_iter(self, iterable: Iterator, length: int) -> Iterable:
        ...

    def chunks_seq(self, iterable: Sequence, length: int) -> Iterable:
        ...

