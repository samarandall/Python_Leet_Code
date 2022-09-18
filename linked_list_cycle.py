class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
def createLinkedList(list):
    head = current = ListNode(list[0])
    for number in range(1,len(list)):
        current.next = ListNode(list[number])
        current = current.next
    return head
    
def hasCycle(head):
    if not head:
        return False
    queue = []
    map = {}
    queue.append(head)
    while queue:
        node = queue.pop(0)
        if node.next:
            queue.append(node.next)
        if map.get(node):
            return True
        map[node] = node.next
        
    return False
    

head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next

linked_list = createLinkedList([-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5])

print(hasCycle(linked_list))
print(hasCycle(head))