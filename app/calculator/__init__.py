from typing import List, Union

from app.calculation import Calculation
from app.history_manager import HistoryManager, OperationCommand
from app.operations import Number


class Calculator:
    def __init__(self) -> None:
        self.history_manager = HistoryManager()

    def perform_operation(self, operation: 'Calculation') -> Number:
        command = OperationCommand(operation)
        result = command.execute()
        self.history_manager.add_to_history(command)
        return result

    def get_history(self) -> List['OperationCommand']:
        return self.history_manager.get_full_history()
    
    def undo(self) -> Union['OperationCommand', None]:
        return self.history_manager.undo_last()
    
    def clear_history(self) -> None:
        self.history_manager.clear_history()