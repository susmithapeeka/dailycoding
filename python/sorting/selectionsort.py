def selectionSort(customlist):
  for i in range(len(customlist)):
    minIndex=i
    for j in range(i+1,len(customlist)):
      if customlist[minIndex]>customlist[j]:
        minIndex=j 
    customlist[i],customlist[minIndex]=customlist[minIndex],customlist[i]
  print(customlist)   

clist=[4,5,6,7,8,1,2,3]
selectionSort(clist)

