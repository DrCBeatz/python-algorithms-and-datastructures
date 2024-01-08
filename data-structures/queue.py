# queue.py

from collections import deque

class EmptyQueueError(Exception):
    """Exception raised when attempting an operation on an empty queue"""
    pass

class Queue():
    def __init__(self) -> None:
        self.queue = deque([])

    def enqueue(self, value: any) -> None:
        self.queue.append(value)

    def dequeue(self) -> any:
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        return self.queue.popleft()
    
    def is_empty(self) -> bool:
        return len(self.queue) == 0