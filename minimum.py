def minimum(arr):
  min_num = arr[0]
  for num in arr:
    if num < min_num:
      min_num = num
  print ("Minimum Value: " + str(min_num))
