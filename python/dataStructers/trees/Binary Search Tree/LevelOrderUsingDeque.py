from collections import deque
class BinarySearchTree:
  def __init__(self,value):
    self.value=value
    self.rightChild=None
    self.leftChild=None

def insertNode(rootnode,values):
    if rootnode.value is None:
      rootnode.value=values
    elif rootnode.value>=values:
      if rootnode.leftChild is None:
        rootnode.leftChild=BinarySearchTree(values)
      else:
        insertNode(rootnode.leftChild,values)
    else:
      if rootnode.rightChild is None:
        rootnode.rightChild=BinarySearchTree(values)
      else:
        insertNode(rootnode.rightChild,values)
    return "entered successfully"

def levelOrder(rootnode):
  if not rootnode:
    return
  else:
    cc=deque()
    cc.append(rootnode)
    while cc:
      root=cc.popleft()
      print(root.value)
      if root.leftChild is not None:
        cc.append(root.leftChild)
      if root.rightChild is not None:
        cc.append(root.rightChild)
        
  

BST=BinarySearchTree(None)
print(insertNode(BST,30))
print(insertNode(BST,10))
print(insertNode(BST,40))
print(insertNode(BST,60))
levelOrder(BST)
