class multistack:
  def __init__(self,size):
    self.size=size
    self.number=3
    self.fixedlist=[0]*(self.size*self.number)
    self.sizelist=[0]*self.number
  def isfull(self,stacknumber):
    if self.sizelist[stacknumber]==self.size:
      return True
    else:
      return False
  def isempty(self,stacknumber):
    if self.sizelist[stacknumber]==0:
      return True
    else:
      return False
  def indexOnTop(self,stacknumber):
    offset=stacknumber*self.size
    return offset+self.sizelist[stacknumber]-1
  def push(self,value,stacknumber):
    if self.isfull(stacknumber):
      return "full"
    else:
      self.sizelist[stacknumber]+=1 
      self.fixedlist[self.indexOnTop(stacknumber)]=value
  def pop(self,stacknumber):
    if self.isempty(stacknumber):
      return "empty stack"
    else:
      popp=self.fixedlist[self.indexOnTop(stacknumber)]
      self.fixedlist[self.indexOnTop(stacknumber)]=0
      self.sizelist[stacknumber]-=1 
      return popp
  def peek(self,stacknumber):
      if self.isempty(stacknumber):
        return "empty stack"
      else:
        return self.fixedlist[indexOnTop(stacknumber)]
        
customStack = multistack(6)
print(customStack.isfull(0))
print(customStack.isempty(1))
customStack.push(1, 0)
customStack.push(2, 0)
customStack.push(3, 2)
print(customStack.pop(0))
    
