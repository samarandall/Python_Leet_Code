n = 38
def climbStairs(n):
    dict = {
        0 : 0,
        1 : 1,
        2 : 2
    }
    def myFunction(n):
        if n in dict:
            return dict[n]
        dict[n] = myFunction(n-1) + myFunction(n-2)
        return dict[n]
    return myFunction(n)

        

print(climbStairs(n))