def kClosest(points, k):
    return sorted(points, key = lambda x: x[0]**2 + x[1]**2)[:k]
        

print(kClosest([[6,10],[-3,3],[-2,5],[0,2]],3))
                            