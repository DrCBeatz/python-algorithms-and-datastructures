# bucket_sort.py

from typing import List
from collections import Counter

def bucket_sort(nums: List[int]) -> List[int]:
    counter = Counter(nums)
    sorted_array = []

    for key in sorted(counter):
        sorted_array.extend([key] * counter[key])
    
    return sorted_array