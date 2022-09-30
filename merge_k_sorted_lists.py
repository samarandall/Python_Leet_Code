class ListNode:
    def __init__(self, x=0,next = None):
        self.val = x
        self.next = next


def mergeKLists(lists):
    def sort_lists(a,b):
        res = temp = ListNode()
        while a and b:
            if a.val < b.val:
                temp.next = a
                temp = temp.next
                a = a.next
            else:
                temp.next = b
                temp = temp.next
                b = b.next
        if a or b:
            temp.next = a if a else b
            
        return res.next
        
    if not lists:
        return []
        
    queue = list()
        
    for l in lists:
        queue.append(l)

    while len(queue) > 1:
        queue.append(sort_lists(queue.pop(0),queue.pop(0)))
        
    return queue[0].val

node1 = ListNode(1)
node1.next = ListNode(4)
node1.next.next = ListNode(5)

node2 = ListNode(1)
node2.next = ListNode(3)
node2.next.next = ListNode(4)

node3 = ListNode(2)
node3.next = ListNode(6)

mergeKLists([node1,node2,node3])
        