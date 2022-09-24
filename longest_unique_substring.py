s = "abcdeafgh"
    
def lengthOfLongestSubstring(s):
    if len(s) == 0:
        return 0
    local_max = 0
    global_max = 1
    while local_max < len(s):
        if local_max == 0:
            local_max = 1
        elif s[local_max] in (s[:local_max]): # a find b
            s = s[s.find(s[local_max])+1:]
            local_max = 0
        else:
            local_max += 1
            if local_max > global_max:
                global_max = local_max
    
    return global_max

print(lengthOfLongestSubstring(s))