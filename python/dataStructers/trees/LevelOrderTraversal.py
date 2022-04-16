from collections import deque
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

def LevelOrderTraversal(rootnode):
  if not rootnode:
    return 
  queue=deque()
  queue.append(rootnode)
  while queue:
    curr=queue.popleft()
    print(curr.value,end=" ")
    if curr.leftChild:
      queue.append(curr.leftChild)
    if curr.rightChild:
      queue.append(curr.rightChild)
      
      
LevelOrderTraversal(new)
