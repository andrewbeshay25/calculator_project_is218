from app.calculation import Addition, Subtraction, Multiplication, Division
from app.calculator import Calculator
from typing import Dict, Type
from app.history_manager import HistoryManager

operations_map: Dict[str, Type] = {
    'add': Addition,
    'subtract': Subtraction,
    'multiply': Multiplication,
    'divide': Division
}

class CommandProcessor:
    def __init__(self) -> None:
        self.calculator = Calculator()
    
    def execute(self, command: str) -> None:
        parts = command.split()

        if len(parts) != 3:
            print("Invalid command format. Type 'help' for instructions.")
            return
        
        operation, a_str, b_str = parts

        try:
            a = float(a_str)
            b = float(b_str)
        except ValueError:
            print("Invalid numbers. Please enter valid numeric values.")
            return
        
        if operation not in operations_map:
            print(f"Unknown operation '{operation}'. Type 'help' for instructions.")
            return
        
        calculation_class = operations_map[operation]
        calculation = calculation_class.create(a, b)
        
        try:
            result = self.calculator.perform_operation(calculation)
            print(f"Result: {result}")
            print(f"Operation: {calculation}")
        
        except ZeroDivisionError:
            print("Error: Division by zero.")

    def show_help(self) -> None:
         print("""
Available commands:
  add a b        - Adds a and b
  subtract a b   - Subtracts b from a
  multiply a b   - Multiplies a and b
  divide a b     - Divides a by b
  history        - Shows the operation history
  undo           - Undoes the last operation
  clear          - Clears the operation history
  exit           - Exits the REPL
  help           - Shows this help message
""")
         
    def show_history(self) -> None:
        history = self.calculator.get_history()

        if not history:
            print("You got no history.")
        else:
            for index, command in enumerate(history, start=1):
                print(f"{index}: {command.operation}")

    def undo_last(self) -> None:
        last_operation = self.calculator.undo()

        if last_operation:
            print(f"Undid operation: {last_operation.operation}")
        else:
            print("No operation to undo.")

    def clear_history(self) -> None:
        self.calculator.clear_history()
        print("History cleared.")

class main():
    processor = CommandProcessor()
    print("Welcome to the Calculator REPL. Type 'help' for instructions or 'exit' to quit.")

    while True:
        command = input(">>> ").strip().lower()
        
        if command in ['exit', 'quit']:
            print("Goodbye!")
            break
        elif command == 'help':
            processor.show_help()
        elif command == 'history':
            processor.show_history()
        elif command == 'undo':
            processor.undo_last()
        elif command == 'clear':
            processor.clear_history()
        else:
            processor.execute(command)

if __name__ == '__main__':
    main()