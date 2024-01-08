# stack.py

from typing import Any

class EmptyStackError(Exception):
    """Exception raised when attempting an operation on an empty stack"""
    pass

class Stack():
    def __init__(self):
        self.stack = []
    
    def is_empty(self) -> bool:
        return len(self.stack) == 0
    
    def pop(self) -> Any:
        if self.is_empty():
            raise EmptyStackError('Stack is empty')
        return self.stack.pop()
    
    def push(self, value: Any) -> None:
        self.stack.append(value)

    def peek(self) -> Any:
        return self.stack[-1] if not self.is_empty() else None
    
    def size(self) -> int:
        return len(self.stack)
