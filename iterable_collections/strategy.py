import operator
from abc import ABC, abstractmethod
from functools import partial
from collections.abc import Iterable,  Mapping, Set, Sequence, MappingView, Iterator

import itertools

from iterable_collections.utils import rpartial, partial_at_position, safe_call


class MethodStrategyInterface(ABC):
    @abstractmethod
    def make_method(self, instance):
        raise NotImplementedError


class ResultStrategyInterface(ABC):
    @abstractmethod
    def handle_result(self, result, iterable, store=None):
        raise NotImplementedError


class ReturnValueStrategyInterface(ABC):
    @abstractmethod
    def return_value(self, instance, result, ret=None):
        raise NotImplementedError


class PreProcessingStrategyInterface(ABC):
    @abstractmethod
    def pre_process(self, instance):
        raise NotImplementedError


class ArgumentFormattingStrategyInterface(ABC):
    @abstractmethod
    def format(self, *args, **kwargs):
        raise NotImplementedError


class ArgumentBindingStrategyInterface(ABC):
    @abstractmethod
    def bind(self, func, instance):
        raise NotImplementedError


class ErrorHandlingStrategyInterface(ABC):
    @abstractmethod
    def get_error(self):
        raise NotImplementedError

    @abstractmethod
    def handle(self, error):
        raise NotImplementedError


class BaseExceptionErrorHandlingStrategy(ErrorHandlingStrategyInterface):
    def get_error(self):
        return BaseException

    def handle(self, error):
        return error


class ConvertToDictErrorHandlingStrategy(ErrorHandlingStrategyInterface):
    def get_error(self):
        return TypeError, ValueError

    def handle(self, error):
        return ValueError('Invalid iterable structure to for type dict')


class GetItemErrorHandlingStrategy(ErrorHandlingStrategyInterface):
    def get_error(self):
        return KeyError, TypeError, IndexError

    def handle(self, error):
        if isinstance(error, KeyError):
            error = KeyError('iterable contains no key, 0.')
        if isinstance(error, TypeError):
            error = TypeError('iterable is not of a subscriptable type.')
        if isinstance(error, IndexError):
            error = IndexError('Index 0 is not set on iterable.')
        return error


class SetItemErrorHandlingStrategy(ErrorHandlingStrategyInterface):
    def get_error(self):
        return TypeError

    def handle(self, error):
        return TypeError('iterable is not of a subscriptable type.')


class StoreResultStrategy(ResultStrategyInterface):
    def handle_result(self, result, iterable, store=None):
        if store is not False:
            return result
        return iterable


class StoreIterableStrategy(ResultStrategyInterface):
    def handle_result(self, result, iterable, store=None):
        if store is not True:
            return iterable
        return result


class ReturnInstanceStrategy(ReturnValueStrategyInterface):
    def return_value(self, instance, result, ret=None):
        if ret is not True:
            return instance
        return result


class ReturnResultStrategy(ReturnValueStrategyInterface):
    def return_value(self, instance, result, ret=None):
        if ret is not False:
            return result
        return instance


class PartialIterableBindingStrategy(ArgumentBindingStrategyInterface):
    def bind(self, func, instance):
        return partial(func, instance.iterable)


class PartialInstanceBindingStrategy(ArgumentBindingStrategyInterface):
    def bind(self, func, instance):
        return partial(func, instance)


class RightPartialIterableBindingStrategy(ArgumentBindingStrategyInterface):
    def bind(self, func, instance):
        return rpartial(func, instance.iterable)


class PartialAtPositionIterableBindingStrategy(ArgumentBindingStrategyInterface):
    def __init__(self, position=0):
        self.position = position

    def bind(self, func, instance):
        return partial_at_position(func, instance.iterable, pos=self.position)


class PreProcessingStrategy(PreProcessingStrategyInterface):
    def __init__(self, operations=()):
        self.operations = operations

    def pre_process(self, instance):
        for operation in self.operations:
            getattr(instance, operation.get('name'))(*operation.get('args', ()), **operation.get('kwargs', {}))


class UnformattedArgumentFormattingStrategy(ArgumentFormattingStrategyInterface):
    def format(self, *args, **kwargs):
        return args, kwargs


class ConvertToDictArgumentFormattingStrategy(ArgumentFormattingStrategyInterface):
    def __init__(self, error_strategy, position=0):
        self.error_strategy = error_strategy
        self.position = position

    def format(self, *args, **kwargs):
        return (
            *args[:self.position],
            safe_call(
                dict,
                self.error_strategy,
                args[self.position]
            ),
            *args[self.position + 1:]
        ), kwargs


class ConvertDictItemsToSetArgumentFormattingStrategy(ArgumentFormattingStrategyInterface):
    def __init__(self, dict_strategy, position=0):
        self.dict_strategy = dict_strategy
        self.position = position

    def format(self, *args, **kwargs):
        formatted_args, formatted_kwargs = self.dict_strategy.format(args[self.position])
        return (
            *args[:self.position],
            set(formatted_args[0].items()),
            *args[self.position + 1:]
        ), kwargs


class ConvertToIterArgumentFormattingStrategy(ArgumentFormattingStrategyInterface):
    def __init__(self, position=0):
        self.position = position

    def format(self, *args, **kwargs):
        return (iter(args[0]), *args[1:]), kwargs


class ConvertToListArgumentFormattingStrategy(ArgumentFormattingStrategyInterface):
    def __init__(self, position=0):
        self.position = position

    def format(self, *args, **kwargs):
        return (
            *args[:self.position],
            list(args[self.position]),
            *args[self.position + 1:]
        ), kwargs


class ConvertToSetArgumentFormattingStrategy(ArgumentFormattingStrategyInterface):
    def __init__(self, position=0):
        self.position = position

    def format(self, *args, **kwargs):
        return (
            *args[:self.position],
            set(args[self.position]),
            *args[self.position + 1:]
        ), kwargs


class SpreadTupleParameterArgumentFormattingStrategy(ArgumentFormattingStrategyInterface):
    def __init__(self, position=0, callable_position=0):
        self.position = position
        self.callable_position = callable_position

    def format(self, *args, **kwargs):
        return (
            *args[:self.position],
            lambda *x: args[self.position](
                *(x[:self.callable_position] + x[self.callable_position] + x[self.callable_position + 1:])
            ), *args[self.position + 1:]
        ), kwargs


class MethodStrategy(MethodStrategyInterface):
    def __init__(
            self,
            name,
            callable_,
            result_strategy,
            return_strategy,
            iterable_binding_strategy,
            argument_formatting_strategy,
            pre_process_strategy,
            error_strategy,

    ):
        self.name = name
        self.callable = callable_
        self.result_strategy = result_strategy
        self.return_strategy = return_strategy
        self.iterable_binding_strategy = iterable_binding_strategy
        self.argument_formatting_strategy = argument_formatting_strategy
        self.pre_process_strategy = pre_process_strategy
        self.error_strategy = error_strategy

    def make_method(self, instance):

        def call(*args, store=None, ret=None, **kwargs):
            self.pre_process_strategy.pre_process(instance)
            formatted_args, formatted_kwargs = self.argument_formatting_strategy.format(*args, **kwargs)
            result = safe_call(
                partial(
                    self.iterable_binding_strategy.bind(self.callable, instance),
                    *formatted_args,
                    **formatted_kwargs
                ), self.error_strategy
            )
            instance._iterable = self.result_strategy.handle_result(result, instance.iterable, store)
            return self.return_strategy.return_value(instance, result, ret)

        return call


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


class DiffMethodStrategy(MethodStrategy):
    def __init__(
            self, 
            name,
            result_strategy,
            return_strategy,
            argument_binding_strategy,
            argument_formatting_strategy,
            pre_process_strategy,
            error_strategy

    ):
        super().__init__(
            name,
            self.diff,
            result_strategy,
            return_strategy,
            argument_binding_strategy,
            argument_formatting_strategy,
            pre_process_strategy,
            error_strategy
        )

    def diff(self, instance, other):
        if not isinstance(other, Iterable):
            raise TypeError('Must an iterable type.')
        if isinstance(other, (Set, Sequence, MappingView, Iterator)):
            instance.diff_seq(other)
        if isinstance(other, Mapping):
            instance.diff_dict(other)
        return instance.iterable


class FlattenMethodStrategy(MethodStrategy):
    def __init__(
            self,
            name,
            result_strategy,
            return_strategy,
            argument_binding_strategy,
            argument_formatting_strategy,
            pre_process_strategy,
            error_strategy
    ):
        super().__init__(
            name,
            self.flatten,
            result_strategy,
            return_strategy,
            argument_binding_strategy,
            argument_formatting_strategy,
            pre_process_strategy,
            error_strategy
        )

    def flatten(self, iterable):
        flat_list = []
        for i in iterable:
            flat_list += self.flatten(list(i)) if isinstance(i, Sequence) and not isinstance(i, (str, bytes)) else [i]
        return flat_list


class IntersectMethodStrategy(MethodStrategy):
    def __init__(
            self,
            name,
            result_strategy,
            return_strategy,
            argument_binding_strategy,
            argument_formatting_strategy,
            pre_process_strategy,
            error_strategy

    ):
        super().__init__(
            name,
            self.intersect,
            result_strategy,
            return_strategy,
            argument_binding_strategy,
            argument_formatting_strategy,
            pre_process_strategy,
            error_strategy
        )

    def intersect(self, instance, target):
        if not isinstance(target, Iterable):
            raise TypeError('Must an iterable type.')
        if isinstance(target, (Set, Sequence, MappingView, Iterator)):
            instance.intersect_seq(target)
        if isinstance(target, Mapping):
            instance.intersect_dict(target)
        return instance.iterable


class SortedAndGroupbyMethodStrategy(MethodStrategy):
    def __init__(
            self,
            name,
            result_strategy,
            return_strategy,
            argument_binding_strategy,
            argument_formatting_strategy,
            pre_process_strategy,
            error_strategy

    ):
        super().__init__(
            name,
            self.group_sort,
            result_strategy,
            return_strategy,
            argument_binding_strategy,
            argument_formatting_strategy,
            pre_process_strategy,
            error_strategy
        )

    def group_sort(self, instance, key=None):
        instance.sorted(key=key) \
            .groupby(key=key)
        return instance.iterable


class ChunksMethodStrategy(MethodStrategy):
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

    def chunks(self, instance, length):
        if isinstance(instance.iterable, (Set, Sequence, MappingView, Iterator)):
            instance.chunks_seq(length)
        if isinstance(instance.iterable, Mapping):
            instance.chunks_dict(length)
        return instance.iterable

    def _chunks(self, iterable, length):
        for x in range(0, len(iterable), length):
            yield iterable[x:x + length]

    def chunks_dict(self, iterable, length):
        return list(self._chunks(iterable, length))

    def chunks_iter(self, iterable, length):
        return list(self._chunks(iterable, length))

    def chunks_seq(self, iterable, length):
        return list(self._chunks(iterable, length))
