from collections import deque as queue
class AVL:
  def __init__(self,data):
    self.data=data
    self.rightChild=None
    self.leftChild=None
    self.height=1 
def preorder(self,rootnode):
  if not rootnode:
    return
  print(rootnode.data)
  preorder(rootnode.leftChild)
  preorder(rootnode.rightChild)
def inorder(self,rootnode):
  if not rootnode:
    return
  inorder(rootnode.leftChild)
  print(rootnode.data)
  inorder(rootnode.rightChild)
def postorder(self,rootnode):
  if not rootnode:
    return
  postorder(rootnode.leftChild)
  postorder(rootnode.rightChild)
  print(rootnode.data)
def levelOrder(rootnode):
  cs=queue()
  cs.append(rootnode)
  while cs:
    root=cs.popleft()
    print(root.data)
    if root.leftChild is not None:
      cc.append(root.leftChild)
    if root.rightChild is not None:
      cc.append(root.rightChild)
def search(rootnode,svalue):
  if rootnode.data==svalue:
    return "value found"
  elif svalue<root.leftChild.data:
    if root.leftChild.data==svalue:
      return "value found"
    else:
      search(root.leftChild,svalue)
  else:
    if root.rightChild.data==svalue:
      return "value found"
    else:
      search(root.rightChild,svalue)
    
newAvl=AVL(10)
levelOrder(newAvl)
print(search(newAvl,10))
