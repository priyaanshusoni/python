# In python functon are defined by this way 

'''
def function_name([list_of_parameters]):---> punctuation which represents end of the function header 
 <body>


'''





from os import name


def print_name(name):
    print(f"Hello {name}")
    

print_name('priyanshu')




# There are different way to call a function 


#1. Positional Arguments 


def order_summary(item , quantity , price):
    print(f"In total {quantity} {item} costs INR: {quantity * price:.2f} ")
    
    

order_summary('banana' , 5 , 10)

# order_summary(5 , "banana" , 10) --> In this scenerio positional arguments can cause error 
#  Also it's unreadable sometimes ---> update_product(1234, 15, 2.55, "12-31-2025")




#2. Keyword Arguments

order_summary(price=10 , item='banana' , quantity=10) #This syntax is more better





# Return from a function 


#1. Modifying the value of the outer scope inside a function



def double(numbers):
    
    result = numbers
    print(id(result) == id(numbers)) # Refer the the same memory adresss 
    
    for i in range(len(numbers)):
        result[i] = numbers[i] * 2
    
    
    return result



numbers = [1 ,2 ,3 ,4 , 5, 6 ]
double(numbers)


print(f"numbers:- {numbers}")



#2.  Return None in some cases 

users = [
     {"username": "alice", "email": "alice@example.com"},
     {"username": "bob", "email": "bob@example.com"},
]


def find_user(username: str , user_list: list):
    
    
    for user in user_list:
        if(user['username']== username):
            return user
    
    return None


print(find_user('random' , users))




# 3. Mutable Objects as default argument
def append_to(item, target=[]):
    target.append(item)
    return target

append_to(5)
append_to(4)
print(append_to(3)) # [5 ,4, 3 ]



# 4. Variable Numbers of postional arguments in a function


def function(*args):
    print(args)
    
    
function(1,2,3,4,5,6,7) #retusn a tuple of total arguments provided


#5. Variable numbers of keyword arguments

def kw_function(**kwargs):
    print(kwargs)

kw_function(name='priyanshu' , age='30',)


#6. Keyword Only Arguments 

def calclate(x , y , * , operator):
      if operator == "+":
         return x + y
      elif operator == "-":
         return x - y
      elif operator == "*":
         return x * y
      elif operator == "/":
         return x / y
      else:
         raise ValueError("invalid operator")
     
     
print(calclate(5 ,6 , operator='+'))




# Unpacking Iterable Only Positional Arguments Like Jaavscript
def unpack(x, y, z):
    print(f"{x=}")
    print(f"{y=}")
    print(f"{z=}")
    

numbers_2 = [1,2,3]
unpack(*numbers_2)
    


