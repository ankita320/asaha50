'''Ankita Saha
  Python Pigs
  SoftDev
  CodingBat List 2 Big Diff
  2024-9-16
  time spent: 2.6
  '''

def big_diff(nums):
  mi = nums[0]
  mp = nums[0]
  
  for i in range(0,len(nums)-1):
    mi = min(mi,nums[i+1])
    
  for j in range(0,len(nums)-1):
    mp = max(mp,nums[j+1])

  return mp-mi
