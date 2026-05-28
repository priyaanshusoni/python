# write a program to print nth fibinacci number


def fib(n: int)-> int:
    
    
    if n==0 or n==1:
        return n
    
    return fib(n-1) + fib(n-2)





def fib_list(n: int)-> list:
    
    # n = 5
    
    ans = []
    
    
    
    first =0
    second = 1
    
    ans.append(first)
    ans.append(second)
    
    n-=2
    
    while n:
        n-=1 # 4 , 3
        third = first+second # 1 , 2 
        ans.append(third) 
        first = second # 1 , 1
        second = third # 1 , 2
    
    
    return ans
        
        
        
    
    







print(fib(1))
print(fib(2))
print(fib(3))
print(fib_list(5))