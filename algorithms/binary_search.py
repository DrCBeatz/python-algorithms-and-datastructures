# binary_search.py

def binary_search(nums: list, target: int) -> int:
    """
    Perform a binary search on a sorted list.

    Args:
        nums (list): A sorted list of integers.
        target (int): The integer to search for in the list.

    Returns:
        int: The index of the target in the list if found, otherwise -1.
    """

    if nums != sorted(nums):
        raise ValueError("Input list must be sorted")
    
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left+right) // 2
        if target > nums[mid]:
            left = mid + 1
        elif target < nums[mid]:
            right = mid - 1
        else:
            return mid
    return -1

