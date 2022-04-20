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
      if self.list[x]==nodevalue:
        return "success"
    return "not found"
  def preOrderTraversal(self,index):
    if index>self.lastused:
      return
    print(self.list[index])
    self.preOrderTraversal(index*2)
    self.preOrderTraversal(index*2+1)
  def InorderTraversal(self,index):
    if index>self.lastused:
      return
    self.preOrderTraversal(index*2)
    print(self.list[index])
    self.preOrderTraversal(index*2+1)
  def PostOrderTraversal(self,index):
    if index>self.lastused:
      return
    self.PostOrderTraversal(index*2)
    self.PostOrderTraversal(index*2+1)
    print(self.list[index])
  def levelOrderTraversal(self,index):
    for i in range(index,self.lastused+1):
      print(self.list[i])
  def deleteNode(self,value):
    if self.lastused==0:
      return "no node to delete"
    for x in range(1,self.lastused):
      if self.list[x]==value:
        self.list[x]=self.list[self.lastused]
        self.list[self.lastused]=None
        self.lastused-=1 
        return "deleted"
bina=binaryTree(8)
bina.insert("Drinks")
bina.insert("Hot")
bina.insert("Cold")
bina.insert("coffee")
bina.insert("tea")
print(bina.deleteNode("coffee"))
print()
bina.levelOrderTraversal(1)
