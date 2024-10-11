from typing import List, Union

from app.calculation import Calculation
from app.operations import Number

class OperationCommand:
    def __init__(self, operation: Calculation) -> None:
        self.operation = operation
    
    def execute(self) -> Number:
        return self.operation.compute()

class HistoryManager:

    def __init__(self) -> None:
        self._history: List[OperationCommand] = []

    def add_to_history(self, operation: 'OperationCommand') -> None:
        self._history.append(operation)
    
    def get_latest(self, n: int = 1) -> 'OperationCommand':       #List['OperationCommand']
        return self._history[-n]
        
    def clear_history(self) -> None:
        self._history.clear
    
    def get_full_history(self) -> List['OperationCommand']:
        return self._history
    
    def undo_last(self) -> Union['OperationCommand', None]: 
        if self._history:
            return self._history.pop() 
        return None