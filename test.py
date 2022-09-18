s = "aab"
dict = {}
for i in s:
    dict[i] = 1
    print(i,dict[i]) 

if dict.get('d'):
    print("a")
else: print(type(dict.get('d')))
