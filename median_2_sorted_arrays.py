'''
first if o(n/2)
'''
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = (len(nums1) + len(nums2))
        is_even = False
        
        if total_len % 2 == 0:
            is_even = True
        
        half_len = total_len//2 
        i = 0
        res = list()
        
        while (nums1 or nums2) and i <= half_len:
            if nums1 and nums2:
                if nums1[0] < nums2[0]:
                    res.append(nums1.pop(0))
                else:
                    res.append(nums2.pop(0))
                
            elif nums1:
                res.append(nums1.pop(0))

            else:
                res.append(nums2.pop(0))
                
            i += 1
            
        if is_even:
            return (res.pop()+res.pop())/2
        return res.pop()
    
    '''
    o(log(n))
    '''
    
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    
