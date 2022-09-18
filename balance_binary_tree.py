class TreeNode:
    def __init__(self, node_val):
        self.node_val = node_val
        self.left = None
        self.right = None

def isBalanced(root):
    





root1 = TreeNode(6)
root1.left = TreeNode(2)
root1.left.left = TreeNode(0)
root1.left.right = TreeNode(4)
root1.left.right.left = TreeNode(3)
root1.left.right.right = TreeNode(5)
root1.right = TreeNode(8)
root1.right.left = TreeNode(7)
root1.right.right = TreeNode(9)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(2)
root2.left.right = TreeNode(3)
root2.left.left = TreeNode(3)
root2.left.left.left = TreeNode(4)

root3 = TreeNode(1)
root3.left = TreeNode(2)
root3.left.left = TreeNode(3)



print(isBalanced(root1))
print(isBalanced(root2))
print(isBalanced(root3))
print(isBalanced(None))