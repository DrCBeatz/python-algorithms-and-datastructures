# comb_sort.py

def next_gap(gap):
    # Shrink gap by Shrink factor
    gap = (gap * 10) // 13
    if gap < 1:
        return 1
    return gap

def comb_sort(nums):
    length = len(nums)
    gap = length
    swapped = True

    while gap != 1 or swapped:
        # Find next gap
        gap = next_gap(gap)
        swapped = False

        for i in range(0, length - gap):
            if nums[i] > nums[i + gap]:
                nums[i], nums[i + gap] = nums[i + gap], nums[i]
                swapped = True
    
    return nums