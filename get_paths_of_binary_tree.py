class TreeNode():
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None
        
def get_paths(root):
    if not root:
        return None
    
    parent = dict()
    parent[root] = None
    queue = list()
    queue.append(root)
    
    res = list()
    
    while queue:
        node = queue.pop()
        if node.left:
            parent[node.left] = node
            queue.append(node.left)
        if node.right:
            parent[node.right] = node
            queue.append(node.right)

        elif not node.left and not node.right:
            temp = list()
            dummy = node
            while dummy:
                temp.append(dummy.val)
                dummy = parent[dummy]
            res.append(temp[::-1])
    
    return res


root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.right.right = TreeNode(4)
root.right.left = TreeNode(5)

print(get_paths(root))
                