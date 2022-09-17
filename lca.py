class TreeNode:
    def __init__(self, node_value):
        self.node_val = node_value
        self.left = None
        self.right = None

def lowestCommonAncestor(root, p, q):
    if not root:
        return root
        
    if root.node_val == p or root.node_val == q:
        return root

    left = lowestCommonAncestor(root.left,p,q)
    right = lowestCommonAncestor(root.right,p,q)
        
    if left and right:
            return root
        
    if left:
        return left
        
    return right
        
root = TreeNode(6)
root.left = TreeNode(2)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

print(lowestCommonAncestor(root,2,8).node_val)