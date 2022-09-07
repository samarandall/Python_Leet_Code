from contextlib import AbstractAsyncContextManager
from operator import truediv
from re import A


s = "abcdeafgh"
local_max = 0
global_max = 1
if len(s) > 0:
    while local_max < len(s):
        if local_max == 0:
            local_max = 1
            
        else:    
            if s[local_max] in s[:local_max]:
                s = s[s.find(s[local_max])+1:]
                local_max = 0
            
            else:
                local_max = local_max + 1

                if(global_max < local_max):
                    global_max = local_max
            
else:
    global_max = 0

print(global_max)