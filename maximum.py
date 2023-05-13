def maximum(arr):
  max_num = arr[0]
  for num in arr:
    if num > max_num:
      max_num = num
  print ("Maximum Value: " + str(max_num))
  
maximum([14, 18, 19, 24, 26, 33, 42, 55, 67])
