def isIsomorphic(s,t):
    if len(s) != len(t):
        return False
    t_map = dict()   
    s_map = dict()

    for i in range(len(s)):
        if t[i] not in t_map and s[i] not in s_map:
            s_map[s[i]] = t[i]
            t_map[t[i]] = s[i]
        
        elif s_map.get(s[i]) != t[i] or t_map.get(t[i]) != s[i]:
            return False
        
    return True
        
print(isIsomorphic('foo','bar'))
print(isIsomorphic('paper','title'))
print(isIsomorphic("badc","baba"))