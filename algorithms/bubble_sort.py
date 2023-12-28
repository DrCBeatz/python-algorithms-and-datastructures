# bubble_sort.py

def bubble_sort(nums: list) -> list:
    """
    Sort a list in ascending order using the bubble sort algorithm.

    Args:
        nums (list): The list to be sorted.

    Returns:
        list: The sorted list.
    """

    if not isinstance(nums, list):
        raise TypeError("Input must be a list")

    length = len(nums) - 1
    for i in range(length):
        swapped = False
        for j in range(0, length - i):
            if nums[j+1] < nums[j]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        if not swapped:
            break 
    return nums