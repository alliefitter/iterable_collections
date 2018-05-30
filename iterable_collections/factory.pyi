from abc import ABC, abstractmethod
from typing import Dict, Tuple

from iterable_collections.strategy import MethodStrategyInterface

StrategyDict = Dict[str, MethodStrategyInterface]

class MethodStrategyFactoryInterface(ABC):
    """
    Creates a :obj:`StrategyDict` containing series of objects implementing
    :obj:`MethodStrategyInterface<iterable_collections.strategy.MethodStrategyInterface>`.
    """
    @abstractmethod
    def create(self) -> StrategyDict:
        ...

    @abstractmethod
    def get_strategies(self) -> Tuple[MethodStrategyInterface]:
        ...


class DefaultMethodStrategyFactory(MethodStrategyFactoryInterface):
    """
    The factory used by the :func:`collect<iterable_collections.collection.collect>` function.
    """
    def create(self) -> StrategyDict:
        ...

    def get_strategies(self) -> Tuple[MethodStrategyInterface]:
        ...