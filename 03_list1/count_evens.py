'''Ankita Saha
  Python Pigs
  SoftDev
  CodingBat List 2 Count Evens
  2024-9-16
  time spent: 0.75
  '''

def count_evens(nums):
  sum = 0
  for i in nums:
    if i % 2 == 0:
      sum+=1
      
  return sum
