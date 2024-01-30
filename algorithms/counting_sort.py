# counting_sort.py

from typing import List

def counting_sort(nums: List[int]) -> List[int]:
  max_val = max(nums)
  count = [0] * (max_val + 1)
  output = [0] * len(nums)

  for n in nums:
    count[n] += 1
  
  for i in range(1, max_val + 1):
    count[i] += count[i - 1]
  
  for i in range(len(nums) -1, -1, -1):
    output[count[nums[i]] -1] = nums[i]
    count[nums[i]] -= 1
    
  return output
