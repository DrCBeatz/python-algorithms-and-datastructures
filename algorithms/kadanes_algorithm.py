# kadanes_algorithm.py
from typing import List

def kadanes(nums: List[int]) -> int:
  max_sum: int = nums[0]
  cur_sum: int  = 0

  for n in nums:
    cur_sum = max(cur_sum, 0)
    cur_sum += n
    max_sum = max(cur_sum, max_sum)
  return max_sum
