# radix_sort.py

def counting_sort(nums, digit_place):
  count = [0] * 10
  output = [0] * len(nums)

  for n in nums:
    digit = ( n // digit_place) % 10
    count[digit] += 1
    
  for i in range(1, 10):
    count[i] += count[i-1]
    
  for i in range(len(nums) -1, -1, -1):
    digit = (nums[i] // digit_place) % 10
    output[count[digit] -1] = nums[i]
    count[digit] -= 1
      
  return output
  
def radix_sort(nums):
  max_val = max(nums)
  digit_place = 1
    
  while max_val // digit_place > 0:
    nums = counting_sort(nums, digit_place)
    digit_place *= 10
    
  return nums
  
