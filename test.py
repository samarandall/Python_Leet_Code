s = "anagram"
t = "nagaram"
if len(s) != len(t):
    print("False")
        
s_map = {}
t_map ={}
        
for i in range(len(s)):
    s_map[s[i]] = s_map.get(s[i], 0) + 1
    t_map[t[i]] = t_map.get(t[i], 0) + 1
            
print(s_map == t_map)