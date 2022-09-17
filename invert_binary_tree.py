class TreeNode:
    def __init__(self, node_val):
        self.node_val = node_val
        self.left = None
        self.right = None
        
def invertBinaryTree(root):
    if not root:
        return None
        
    left = invertBinaryTree(root.left)
    right = invertBinaryTree(root.right)
    
    root.left = right
    root.right = left
    return root

def printTree(root):
    if not root:
        return None
    left = printTree(root.left)
    right = printTree(root.right)
    
    print(root.node_val)
    return root
    

root = TreeNode(6)
root.left = TreeNode(2)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

printTree(root)
printTree(invertBinaryTree(root))