class stack:
  def __init__(self,maxsize):
    self.maxsize=maxsize
    self.list=[]
  def __str__(self):
    values=[str(x) for x in self.list]
    return '\n'.join(values)
  def push(self,value):
    if self.isFull():
      return "list is full"
    else:
      return self.list.append(value)
  def isempty(self):
    if self.list==[]:
      return True
    else:
      return False
  def isFull(self):
    if len(self.list)==self.maxsize:
      return True
    else:
      return False
    
  def rem(self):
    if isempty():
      return "no elements"
    else:
      return self.list.pop()
  def peek(self):
    if self.isempty():
      return "no elements"
    else:
      return self.list[-1]
    
cus=stack(2)
cus.push(1)
cus.push(5)
cus.push(6)
print(cus)
k=cus.peek()
print("---------------")
print(k)
