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
        insertNode(rootnode.rightChild,value)
    return "entered successfully"
def Preorder(rootnode):
  if not rootnode:
     return
  print(rootnode.value)
  Preorder(rootnode.leftChild)
  Preorder(rootnode.rightChild)
def inorder(rootnode):
  if not rootnode:
    return
  inorder(rootnode.leftChild)
  print(rootnode.value)
  inorder(rootnode.rightChild)

def postOrder(rootnode):
  if not rootnode:
    return
  postOrder(rootnode.leftChild)
  postOrder(rootnode.rightChild)
  print(rootnode.value)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
BST=BinarySearchTree(None)
print(insertNode(BST,30))
print(insertNode(BST,10))
print(insertNode(BST,40))
Preorder(BST)
print()
inorder(BST)
print()
postOrder(BST)
