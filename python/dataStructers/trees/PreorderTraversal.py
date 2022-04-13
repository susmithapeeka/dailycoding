class Tree:
  def __init__(self,value):
    self.value=value
    self.leftChild=None
    self.rightChild=None
    
new=Tree("drinks")
hot=Tree("hot")
soft=Tree("cold")
new.leftChild=hot
new.rightChild=soft
def PreorderTraversal(rootnode):
    if not rootnode:
      return
    print(rootnode.value)
    PreorderTraversal(rootnode.leftChild)
    PreorderTraversal(rootnode.rightChild)
  
PreorderTraversal(new)
