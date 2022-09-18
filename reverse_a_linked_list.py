class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None
        
def createLinkedList(list):
    head = current = ListNode(list[0])
    for number in range(1,len(list)):
        current.next = ListNode(list[number])
        current = current.next
    return head

def reverseLinkedList(head):
    current = head
    prev = None
    
    while current.next is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    head = prev
    return head
        
    
        



head = createLinkedList([1,2,3,4,5])

reverseLinkedList(head)
while head:
    print(head.val)
    head = head.next