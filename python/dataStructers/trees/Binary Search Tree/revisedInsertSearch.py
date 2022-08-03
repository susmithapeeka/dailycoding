class BinarySearchTree:
  def __init__(self,value):
    self.value=value
    self.leftChild=None
    self.rightChild=None
def insertNode(rootNode,ivalue):
  if rootNode.value is None:
    rootNode.value=ivalue
  elif rootNode.value>=ivalue:
    if rootNode.leftChild is None:
      rootNode.leftChild=BinarySearchTree(ivalue)
    else:
      insertNode(rootNode.leftChild,ivalue)
  else:
    if rootNode.rightChild is None:
      rootNode.rightChild=BinarySearchTree(ivalue)
    else:
      insertNode(rootNode.rightChild,ivalue)
  return "Entered value"
def preOrder(rootNode):
  if not rootNode:
    return
  print(rootNode.value)
  preOrder(rootNode.leftChild)
  preOrder(rootNode.rightChild)

def searchgeeks(root,key):
     
    # Base Cases: root is null or key is present at root
    if root is None or root.value == key:
        return root
 
    # Key is greater than root's key
    if root.value < key:
        return searchgeeks(root.rightChild,key)
   
    # Key is smaller than root's key
    return searchgeeks(root.leftChild,key)

b=BinarySearchTree(13)
insertNode(b,8)
insertNode(b,17)
preOrder(b)
print(searchgeeks(b,20))
