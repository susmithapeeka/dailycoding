class binaryTree:
  def __init__(self,size):
    self.list=size*[None]
    self.lastused=0
    self.maxsize=size
  def insert(self,value):
    if self.lastused+1==self.maxsize:
      return "tree is full"
    self.list[self.lastused+1]=value
    self.lastused+=1 
    return "value successfully inserted"
  def search(self,nodevalue):
    for x in range(len(self.list)):
      if self.list[i]==nodevalue:
        return "success"
    return "not found"
      
bina=binaryTree(8)
bina.insert("Drinks")
bina.insert("Hot")
bina.insert("Cold")
