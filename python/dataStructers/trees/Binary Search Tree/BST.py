class BinarySearchTree:
  def __init__(self,value):
    self.value=value
    self.rightChild=None
    self.leftChild=None

def insertNode(rootnode,value):
    if rootnode.value==None:
      rootnode.value=value
    elif rootnode.value>value:
      if rootnode.leftChild==None:
        rootnode.leftChild=value
      else:
        insertNode(rootnode.leftChild,value)
    else:
      if rootnode.rightChild==None:
        rootnode.rightChild=value
      else:
        insertNode(rootnode.rightChild,value)
    return "entered successfully"
