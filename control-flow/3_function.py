#functions in Python 


def fibN(n):    #fibonacci series of length n 
    ans = []
    first = 0
    second = 1
    ans.append(first)
    ans.append(second)
    for i in range(2,n):
        third = first + second
        ans.append(third)
        first = second
        second = third
        
    return ans
        
        
print(fibN(n=4)) #keyword argument
print(fibN(2)) # non-keyword argument
print(fibN(10))