import ast
teststr = "'(5,4,2)','(12,4,3)','(3,4,13)'"
testarray = ast.literal_eval(teststr)
output=[]
for x in testarray:
  inla=[]
  for y in x:
    if y == ")":
      output.append(inla)
      inla=[]
    if y.isdigit():
      inla.append(int(y))
print(output)
result=""
for x in range(len(output)):
  mini=min(output[x])
  index=output[x].index(mini)
  result+="("+str((x+1))+"-"+""+str(index+1)+")"
print(result)
