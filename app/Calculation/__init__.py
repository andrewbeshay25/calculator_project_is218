from abc import ABC, abstractmethod
from app.operations import addition, subtraction, multiplication, division, Number

class Calculation(ABC):
    def __init__(self, a: Number, b: Number) -> None:
        self.a = a
        self.b = b

    @classmethod
    def create(cls, a: Number, b: Number) -> 'Calculation':
        return cls(a, b)
    
    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass
        
    @abstractmethod
    def compute() -> Number:
        pass
    
class Addition(Calculation):
    
    def compute(self) -> Number:
        return addition(self.a, self.b)
    
    def __str__(self) -> str:
        return f"Addition: {self.a} + {self.b} = {self.compute()}"

    def __repr__(self):
        return f"(Addition) a: {self.a} + b: {self.b} = {self.compute()}"

class Subtraction(Calculation):
    
    def compute(self) -> Number:
        return subtraction(self.a, self.b)
    
    def __str__(self) -> str:
        return f"Subtraction: {self.a} - {self.b} = {self.compute()}"

    def __repr__(self):
        return f"(Subtraction) a: {self.a} - b: {self.b} = {self.compute()}"
    
class Multiplication(Calculation):
    
    def compute(self) -> Number:
        return multiplication(self.a, self.b)
    
    def __str__(self) -> str:
        return f"Multiplication: {self.a} * {self.b} = {self.compute()}"

    def __repr__(self):
        return f"(Multiplication) a: {self.a} * b: {self.b} = {self.compute()}"
    
class Division(Calculation):
    
    def compute(self) -> Number:
        return division(self.a, self.b)
    
    def __str__(self) -> str:
        result = self.compute()
        # If the result is a whole number, format it as an integer; otherwise, keep it as a float.
        formatted_result = int(result) if result.is_integer() else result
        return f"Division: {self.a} / {self.b} = {formatted_result}"

    def __repr__(self) -> str:
        result = self.compute()
        formatted_result = int(result) if result.is_integer() else result
        return f"(Division) a: {self.a} / b: {self.b} = {formatted_result})"