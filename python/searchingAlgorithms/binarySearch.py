import math
def binarySearch(arr,val):
  start=0
  end=len(arr)-1
  middle=math.floor((start+end)/2)
  while not(arr[middle]==val) and start<=end:
    if val<arr[middle]:
      end=middle-1
    else:
      start=middle+1 
    middle=math.floor((start+end)/2)
  if arr[middle]==val:
    return middle
  else:
    return -1
    
  

print(binarySearch([8,9,10,11,12,15,17],18))
