
""" only works on leetcode
    head_list = temp_list = ListNode()
            
    while list1 and list2:
        if list1.val < list2.val:
            temp_list.next = list1
            temp_list = temp_list.next
            list1 = list1.next
        else:
            temp_list.next = list2
            temp_list = temp_list.next
            list2 = list2.next
        
    if list2 or list1:
        temp_list.next = list2 if list2 else list1
          
    head_list = head_list.next
            
    return head_list
    """