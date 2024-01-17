# heap_sort.py

import heapq

def heap_sort(nums: list) -> list:
    heapq.heapify(nums)
    return [heapq.heappop(nums) for _ in range(len(nums))]