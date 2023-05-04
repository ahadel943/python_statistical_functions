# A function calculate the average value of a given numerical data series.
# Mean or Average is a measure of central tendency.
# The sum of the numerical values of a data series divided by its count. 

def mean(arr):
  arr_sum = 0
  for n in arr:
    arr_sum += n
  avg = arr_sum / len(arr)
  print ("Mean is: " + str(avg))

arr = [1, 4, 5, 12, 100, 180, 200]
mean(arr)