class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def hasPathSum(node, s):
        ans = 0
        subSum = s - node.data
 
        # If we reach a leaf node and sum becomes 0, then
        # return True
        if(subSum == 0 and node.left == None and node.right == None):
            return True
 
        # Otherwise check both subtrees
        if node.left is not None:
            ans = ans or hasPathSum(node.left, subSum)
        if node.right is not None:
            ans = ans or hasPathSum(node.right, subSum)
 
        return ans
 
    
s = 21
root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.right = Node(5)
root.left.left = Node(3)
root.right.left = Node(2)

print(hasPathSum(root,21))
