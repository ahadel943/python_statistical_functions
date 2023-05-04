# Range => A function calculate the range of a data series
# The difference between the max value and the min value

def range(arr):
  min_Val = min(arr)
  max_val = max(arr)
  range_val = max_val - min_Val
  print ("Range is: " + str(range_val))
  
arr = [1, 4, 5, 12, 100, 180, 200]
range(arr)