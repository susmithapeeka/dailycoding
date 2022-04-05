def matchingbrackets(str1):
  open_list = ["[","{","(","<"]
  close_list = ["]","}",")",">"]
  stack=[]
  for x in str1:
    if x in open_list:
      stack.append(x)
    elif x in close_list:
      position=close_list.index(x)
      if((len(stack)>0) and open_list[position]==stack[len(stack)-1]):
        stack.pop()
      else:
        return(0)
  if len(stack)==0:
    return(1) 
  else:
    return(0)

for x in range(int(input())):
  str1=input()
  print(matchingbrackets(str1),end=" ")
