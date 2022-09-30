s = "abcdeafgh"
    
def lengthOfLongestSubstring(s):
    charSet = set()
    l = 0
    global_max = 0
    local_max = 0
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
            local_max -= 1
        charSet.add(s[r])
        local_max += 1
        if local_max > global_max:
            global_max = local_max
    return global_max

print(lengthOfLongestSubstring(s))
print(lengthOfLongestSubstring("abcabcbb"))