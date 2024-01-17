# bucket_sort.py

from collections import Counter

def bucket_sort(nums: list) -> list:
    counter = Counter(nums)
    sorted_array = []

    for key in sorted(counter):
        sorted_array.extend([key] * counter[key])
    
    return sorted_array