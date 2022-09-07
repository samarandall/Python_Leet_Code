s = "[]"
par_dict = {'(':')','{':'}','[':']'}
stack = []
bool = True

if len(s) % 2 != 0:
    print("false")
else:
    for char in s:
        if char in par_dict.keys():
            stack.append(char)
        else:
            if stack == []:
                print("False")
            elif char != par_dict[stack.pop()]:
                print("False")
                
print("true")
