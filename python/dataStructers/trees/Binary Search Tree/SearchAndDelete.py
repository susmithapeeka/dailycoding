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

def searchNode(rootNode, nodeValue):
    if rootNode.value == nodeValue:
        print("The value is found")
    elif nodeValue < rootNode.value:
        if rootNode.leftChild.value == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild.value == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.rightChild, nodeValue)

def minvalue(rootNode):
  curr=rootNode
  while(curr.leftChild is not None):
    curr=curr.leftChild
  return curr

def delete(rootNode,dvalue):
  if rootNode is None:
    return rootNode
  if dvalue<rootNode.value:
    rootNode.leftChild=delete(rootNode.leftChild,dvalue)
  elif dvalue>rootNode.value:
    rootNode.rightChild=delete(rootNode.rightChild,dvalue)
  else:
    if rootNode.leftChild is None:
      temp=rootNode.rightChild
      rootNode=None
      return temp
    if rootNode.rightChild is None:
      temp=rootNode.leftChild
      rootNode=None
      return temp
    temp=minvalue(rootNode.rightChild)
    rootNode.data=temp.data
    rootNode.rightChild=delete(rootNode.rightChild,temp.data)
  return rootNode
  
def deleteBST(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The BST has been successfully deleted"

BST=BinarySearchTree(None)
print(insertNode(BST,30))
print(insertNode(BST,10))
print(insertNode(BST,40))
print(insertNode(BST,60))
print(searchNode(BST,20))
