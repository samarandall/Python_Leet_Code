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
    prev = None
    temp = None
    while head:
        
        #head = 1
        
        temp = head
        ''' temp = 1
            temp = 2
            temp = 3
        '''
        head = head.next
        '''head = 2
            head = 3
            head = None
        '''
        
        temp.next = prev
        '''temp.next = None
            temp.next = 1
            temp.next = 2
        '''
        
        prev = temp
        ''' prev = 1
            prev = 2
            prev = 3
        '''
        '''temp total      | head
            1->None        | 2->3->None
            2->1->None     | 3->None
            3->2->1->None  | None

            1->2->3
            None<-1        2->3
            None<-1<-2     3
            None<-1<-2<-3  None
            
        '''
        
    return temp

head = createLinkedList([1,2,3,4,5])

reverseLinkedList(head)
