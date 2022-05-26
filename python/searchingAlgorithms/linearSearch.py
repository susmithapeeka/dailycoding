def linearSearch(arr,value):
  for x in range(len(arr)):
    if arr[x]==value:
      return x 
  return -1
  
print(linearSearch([10,20,30,50,70],90))
