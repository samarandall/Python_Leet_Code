s = "]"
local_string = ""
bool = True

if len(s) % 2 != 0: 
    print("False")
    bool = False

else:
    for char in s:
        if char == '{' or char == '[' or char == '(':
            local_string += char

        elif len(local_string) > 0:
            if char == ']':
                if local_string[-1] == '[':
                    local_string = local_string[:len(local_string)-1]
                else:
                    print("False")
                    bool = False
                        
            elif char == '}':
                if local_string[-1] == '{':
                    local_string = local_string[:len(local_string)-1]
                else:
                    print("False")
                    bool = False
                        
            else:
                if local_string[-1] == '(':
                    local_string = local_string[:len(local_string)-1]
                else:
                    print("False")
                    bool = False
                    
        else:
            bool = False
            print("False") 
                
    if bool:
        if len(local_string) != 0:
            print("False")
        else :
           print("True")