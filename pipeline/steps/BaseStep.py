from abc import ABC, abstractmethod
from context import Context

class BaseStep(ABC):
    @abstractmethod
    def run(self, ctx: Context) -> None:
        pass
