class heap:
  def __init__(self,size):
    self.customList=[None]*(size+1)
    self.maxsize=size+1 
    self.heapSize=0

def peek(rootNode):
  if not rootNode:
    return "empty"
  else:
    return rootNode.customList[1]
    
def sizeofHeap(rootNode):
  if not rootNode:
    return "empty"
  else:
    return rootNode.heapSize

def levelOrder(rootnode):
  if not rootnode:
    return
  else:
    for i in range(1,rootnode.heapSize+1):
      print(rootnode.customList[i])
newBinaryItem=heap(5)
print(sizeofHeap(newBinaryItem))
  
