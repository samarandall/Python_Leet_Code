s = "A man, a plan, a canal: Panama"
s = s.lower()
new_string = ""
for char in s:
    if char.isalnum():
        new_string += char
        
if new_string == new_string[::-1]:
    print("true")
else:
    print("false")