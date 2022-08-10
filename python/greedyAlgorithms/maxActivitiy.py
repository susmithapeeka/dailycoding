def maxActivity(array):
  array.sort(key=lambda x:x[2])
  i=0
  first =array[i][0]
  print(first)
  for j in range(len(array)):
    if array[j][1]>array[i][2]:
      print(array[j][0])
      i=j
    
array=[["a1",0,6],["a2",1,2],["a3",3,4],["a4",5,6],["a5",5,7],["a6",8,10]]
print(maxActivity(array))
activities = [["A1", 0, 6],
              ["A2", 3, 4],
              ["A3", 1, 2],
              ["A4", 5, 8],
              ["A5", 5, 7],
              ["A6", 8, 9]
                ]
print(maxActivity(activities))
