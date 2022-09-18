#
s = s = "aabcb"

def longestPalindrome(s):
    length = len(s)
    if length == 0:
        return 0
    if length == 1:
        return 1
    
    my_dict = {}
    current_length = 1

    for i in range(0,length):
        my_dict[i] = s[i]
        for a in range(0,i):
            my_dict[a] = my_dict[a] + s[i]
            curr_string = my_dict[a][::-1]
            #print(my_dict[a], curr_string)
            if my_dict[a] == curr_string:
                if len(my_dict[a]) > current_length:
                    current_length = len(my_dict[a])

    return current_length

print(longestPalindrome(s))