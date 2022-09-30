
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
def get_k_element_from_end_2_pointers(node,k):
    r = 0
    l = r-k
    left_node = node
    while l < 0:
        l+=1
        node = node.next
    
    while node:
        node = node.next 
        left_node = left_node.next
    
    return left_node 
        
        
def get_k_element_from_end(node,k): #o(n+k)
    stack = list()
    while node:
        stack.append(node)
        node = node.next
    res = 0
    for i in range(k):
        res = stack.pop()
    return res

node = Node(2)
node.next = Node(3)
node.next.next = Node(8)
node.next.next.next = Node(2)
node.next.next.next.next = Node(5)

print(get_k_element_from_end_2_pointers(node,2).val)