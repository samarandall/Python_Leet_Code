class TreeNode:
    def __init__(self, node_val):
        self.val = node_val
        self.left = None
        self.right = None

def levelOrder(root):
    if not root:
        return []
    queue = list() #keeps track of next node
    queue.append(root)
    
    depth = dict() #knows the depth of the node
    depth[root] = 0
    
    return_list = list() 
    return_list.append([root.val])
    
    level = list() #values of the node in the current level
    curr_level = 1
    
    while queue:
        node = queue.pop(0)
        if curr_level != depth.get(node):
            if level:
                return_list.append(level)
            level = list()
            curr_level = depth.get(node)
        
        if node.left:
            depth[node.left] = depth[node] + 1
            queue.append(node.left)
            level.append(node.left.val)
            
        if node.right:
            depth[node.right] = depth[node] + 1
            queue.append(node.right)
            level.append(node.right.val)
    return return_list   
        
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(levelOrder(root))