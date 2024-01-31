# queue.py

from collections import deque
from typing import Any

class EmptyQueueError(Exception):
    """Exception raised when attempting an operation on an empty queue"""
    pass

class Queue():
    def __init__(self) -> None:
        self.queue = deque([])

    def enqueue(self, value: Any) -> None:
        self.queue.append(value)

    def dequeue(self) -> Any:
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        return self.queue.popleft()
    
    def is_empty(self) -> bool:
        return len(self.queue) == 0
        
    def size(self) -> int:
        return len(self.queue)
        
    def front(self) -> Any:
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        return self.queue[0]
        

s


