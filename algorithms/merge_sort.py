# merge_sort.py

def merge_sort(nums: list) -> list:
    if len(nums) > 1:
        mid = len(nums) // 2
        L = nums[:mid]
        R = nums[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            nums[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            nums[k] = R[j]
            j += 1
            k += 1

    return nums

assert merge_sort([5,4,3,2,1]) == [1,2,3,4,5]