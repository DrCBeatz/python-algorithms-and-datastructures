# shell_sort.py

def shell_sort(nums: list) -> list:
    length = len(nums)
    gap = length // 2
    while gap > 0:
        for i in range(gap, length):
            key = nums[i]
            j = i
            while j >= gap and key < nums[j - gap]:
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = key
        gap //= 2
    return nums