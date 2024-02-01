# stack.py

from typing import Any, Optional

class EmptyStackError(Exception):
    """Exception raised when attempting an operation on an empty stack"""
    pass

class Stack:
    def __init__(self, capacity: Optional[int] = None):
        self._stack = []
        self._capacity = capacity

    def is_empty(self) -> bool:
        return len(self._stack) == 0
    
    def pop(self) -> Any:
        if self.is_empty():
            raise EmptyStackError('Stack is empty')
        return self._stack.pop()
    
    def push(self, value: Any) -> None:
        if self._capacity is not None and len(self._stack) >= self._capacity:
            raise OverflowError('Stack capacity reached')
        self._stack.append(value)

    def peek(self) -> Any:
        if self.is_empty():
            raise EmptyStackError('Stack is empty')
        return self._stack[-1]
    
    def size(self) -> int:
        return len(self._stack)
