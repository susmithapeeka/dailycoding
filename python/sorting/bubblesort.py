def bubblesort(customlist):
  for i in range(len(customlist)-1):
    for j in range(len(customlist)-i-1):
      if customlist[j]>customlist[j+1]:
        customlist[j],customlist[j+1]=customlist[j+1],customlist[j]
  print(customlist)

clist=[5,6,7,4,3,2,1]
print(bubblesort(clist))
