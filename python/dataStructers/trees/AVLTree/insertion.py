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
      cs.append(root.leftChild)
    if root.rightChild is not None:
      cs.append(root.rightChild)
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
def gethead(rootnode):
  if not rootnode:
    return 0 
  return rootnode.height
def rightRotation(disbalancedRoot):
  newroot=disbalancedRoot.leftChild
  disbalancedRoot.leftChild=disbalancedRoot.leftChild.rightChild
  newroot.rightChild=disbalancedRoot
  disbalancedRoot.height=1+max(gethead(disbalancedRoot.leftChild),gethead(disbalancedRoot.rightChild))
  newroot.height=1+max(gethead(disbalancedRoot.leftChild),gethead(disbalancedRoot.rightChild))
  return newroot
def leftRotation(disbalancedRoot):
  newroot=disbalancedRoot.rightChild
  disbalancedRoot.rightChild=disbalancedRoot.rightChild.leftChild
  newroot.leftChild=disbalancedRoot
  disbalancedRoot.height=1+max(gethead(disbalancedRoot.leftChild),gethead(disbalancedRoot.rightChild))
  newroot.height=1+max(gethead(disbalancedRoot.leftChild),gethead(disbalancedRoot.rightChild))
  return newroot
def getbalance(rootnode):
  if not rootnode:
    return 0 
  return gethead(rootnode.leftChild)-gethead(rootnode.rightChild)
  
def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVL(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)
    
    rootNode.height = 1 + max(gethead(rootNode.leftChild), gethead(rootNode.rightChild))
    balance = getbalance(rootNode)
    if balance > 1 and nodeValue < rootNode.leftChild.data:
        return rightRotation(rootNode)
    if balance > 1 and nodeValue > rootNode.leftChild.data:
        rootNode.leftChild = leftRotation(rootNode.leftChild)
        return rightRotation(rootNode)
    if balance < -1 and nodeValue > rootNode.rightChild.data:
        return leftRotation(rootNode)
    if balance < -1 and nodeValue < rootNode.rightChild.data:
        rootNode.rightChild = rightRotation(rootNode.rightChild)
        return leftRotation(rootNode)
    return rootNode
  
       
newAVL=AVL(30)
newAVL = insertNode(newAVL, 10)
newAVL = insertNode(newAVL, 15)
newAVL = insertNode(newAVL, 20)
levelOrder(newAVL)
