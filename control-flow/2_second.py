# The break & continue statements 


#the range function in Python takes three parameters => 1. start , 2. stop , 3. steps to increment 

for iterable in range(2, 10,3): print(iterable)




# break statement breaks out of inner most loop ( for loop in this example )

for  i in range(2,10):
    for j in range(2, i):
        if(i % j ==0):
            print(f"{i} is divisible by {j}")
        else:
            print(f"{i} is not  divisible by {j}")



"""
Match Statements in Python (Similiar to Switch-Case in Javascript)
"""


#Let's create a function which returns the Error message for a particular HTTP status code 

def http_error(status_code ):
    match status_code:
        case 400:
            return "Bad Request"
        case 401:
            return "UnAuthorized"
        case 404:
            return "Not-Found"
        case _:
            return "Something went wrong"
    
    
    
status_code_1 = http_error(401)
status_code_2 = http_error(403)
status_code_3 = http_error(404)
print(f"{status_code_1} \n {status_code_2} \n {status_code_3}")