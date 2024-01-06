# quick_sort.py

def quick_sort(nums: list) -> list:
    if len(nums) <= 1:
        return nums
    
    pivot = nums[-1]
    larger, equal, smaller = [], [], []

    for n in nums:
        if n > pivot:
            larger.append(n)
        elif n < pivot:
            smaller.append(n)
        else:
            equal.append(n)
    
    return quick_sort(smaller) + equal + quick_sort(larger)
