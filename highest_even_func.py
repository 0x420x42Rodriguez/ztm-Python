def highest_even(li):
  '''
  Function to find the greatest even number in a list
  '''
  evens = []
  for item in li:
    if item % 2 ==0:
      evens.append(item)
  return max(evens)
  


print(highest_even([10,2,3,4,8,11]))