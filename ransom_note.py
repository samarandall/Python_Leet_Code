def canConstruct(note,magazine):
    while note:
        z = magazine.find(note[0])
        if z >= 0:
            magazine = magazine[:z] + magazine[z+1:]
            note = note[1:]
        else: 
            return False
    return True
            


print(canConstruct('aa','ab'))
print(canConstruct('aa','aa'))