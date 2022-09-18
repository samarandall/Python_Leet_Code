n = 2
bad = 2

def isBadVersion(i):
    if i >= bad:
        return True
    return False

def firstBadVersion(n):
    left = 0
    right = n
    midpoint = n//2
    last = -1
    if n == 0:
        return 0
    if n == 1:
        return 1
    while midpoint > left and midpoint <= right:
        if isBadVersion(midpoint):
            last = midpoint
            right = midpoint
            midpoint = (right+left)//2
        else:
            left = midpoint
            midpoint = (left+right)//2 + 1
    return last

print(firstBadVersion(n))