#functions in Python 


import test


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




# In python if a function does not have a return value it returns NONE


def no_return(name: str):
   pass
    
    

print(no_return('john')) # returns None

# Passing arguments by name & or by position 





def test1(name , age , work=''):
    print(f"{name} is {age} years old and currently working as a {work}")




# test1( name='Priyanshu' , 23 , 'Software Engineer') Error --> Keywords args must come after positional args

"""
Once you use a keyword argument, all arguments after it must also be keyword arguments.
""" 




