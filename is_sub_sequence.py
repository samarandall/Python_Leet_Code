def isSubsequence(s,t):
    if len(s) > len(t):
        return False
    if len(s) == 0:
        return True
    for char in t:
        if s[0] == char:
            s = s[1:]
        if len(s) == 0:
            return True
    return False
            
    
print(isSubsequence('abc', 'ahbgdc'))