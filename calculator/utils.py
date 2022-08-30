from typing import Protocol


# Command pattern
class Operation(Protocol):
    @classmethod
    def apply(cls, first: float, second: float) -> float:
        pass


class ModulusOperation:
    @classmethod
    def apply(cls, first: float, second: float) -> float:
        return first % second


class DivisionOperation:
    @classmethod
    def apply(cls, first: float, second: float) -> float:
        return first / second


class SubstractionOperation:
    @classmethod
    def apply(cls, first: float, second: float) -> float:
        return first - second


class MultiplicationOperation:
    @classmethod
    def apply(cls, first: float, second: float) -> float:
        return first * second
