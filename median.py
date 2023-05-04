# A function calculate the middle value of a given data series
# Median is a measure of central tendency. 

import math

def median(arr):
  sorted_arr = sorted(arr)
  if (len(sorted_arr) % 2 == 0):
    index_1 = sorted_arr[math.floor(len(sorted_arr)/2)-1]
    index_2 = sorted_arr[math.floor((len(sorted_arr)+2)/2)-1]
    med = (index_1 + index_2) / 2
    print ("Median is: " + str(med))
  else:
    med = sorted_arr[math.floor((len(sorted_arr)+1)/2)-1]
    print ("Median is: " + str(med))

arr = [1, 4, 5, 12, 100, 180, 200]
median(arr)