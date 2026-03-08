# Ths if control flow in python ha if , else & else keywords 


"""


age = int(input("Enter your age\n"));


if age >= 18:
    print("You are eligible to vote. ")
elif age<18:
    print("You are not eligible to vote.")
    
"""


    
# In Python there can be zero or more elif parts for if statements , and "else" part is optional 




# For loop control flow in Python 

# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(f"{w} has length of {len(w)}")  #string concatenation using f "..." method.
    
    
# To Iterate over  indices of a sequence , we can combine range() & len() function like this 
items = ['Mary', 'had', 'a', 'little', 'lamb']

for i in range(len(items)):
    print(f"At index {i} , {items[i]} is placed.")



