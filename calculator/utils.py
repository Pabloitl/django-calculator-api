from typing import Protocol


# Command pattern
class Operation(Protocol):
    @classmethod
    def apply(cls, first: float, second: float) -> float:
        pass
