# heap_sort.py

from typing import List
import heapq

def heap_sort(nums: List[int]) -> List[int]:
    heapq.heapify(nums)
    return [heapq.heappop(nums) for _ in range(len(nums))]