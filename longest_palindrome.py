#longest palindrome that can be built from 'n' by rearanging letter

s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"

def longestPalindrome(s):
    my_dict = {}
    total = 0
    dict_contains_odd_val = False
    for i in s:
        if my_dict.get(i):
            my_dict[i] += 1
        else:
            my_dict[i] = 1
    for i in my_dict:
        curr_dict_val_is_odd = my_dict[i] % 2
        if curr_dict_val_is_odd == 1:
            total += my_dict[i]-1
            dict_contains_odd_val = True
        else:
            total += my_dict[i]
    
    if dict_contains_odd_val:
        total+=1
    return total

print(longestPalindrome(s))