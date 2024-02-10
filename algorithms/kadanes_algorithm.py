# kadanes_algorithm.py

def kadanes(nums):
  max_sum = nums[0]
  cur_sum = 0

  for n in nums:
    cur_sum = max(cur_sum, 0)
    cur_sum += n
    max_sum = max(cur_sum, max_sum)
  return max_sum
