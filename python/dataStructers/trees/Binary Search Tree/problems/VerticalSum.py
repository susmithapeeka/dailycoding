class newNode:
  def __init__(self,value):
    self.value=value
    self.rightChild=None
    self.leftChild=None
def verticalSumUtil(root, hd, Map):
  if root is None:
    return
  verticalSumUtil(root.leftChild,hd-1,Map)
  if hd in Map.keys():
    Map[hd]+=root.value
  else:
    Map[hd]=root.value
  verticalSumUtil(root.rightChild,hd+1,Map)
def verticalSum(root):
    Map={}
    verticalSumUtil(root,0,Map)
    for i,j in Map.items():
      print(i,"=",j)

if __name__ == "__main__": 
      
    '''      Create the following Binary Tree
              1
            /    \
          2        3
         / \      / \
        4   5    6   7 
    '''
    root = newNode(1) 
    root.leftChild = newNode(2) 
    root.rightChild = newNode(3) 
    root.leftChild.leftChild = newNode(4) 
    root.leftChild.rightChild = newNode(5) 
    root.rightChild.leftChild = newNode(6) 
    root.rightChild.rightChild = newNode(7)
      
    print("Following are the values of vertical "
          "sums with the positions of the "
          "columns with respect to root")
      
    verticalSum(root)
