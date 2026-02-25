#Python varibles are reference to the object , basically everything is an object in python 



# a is a tag/name given to a object whose value is => 10

a = 10; 
b = 10;
print(id(a))  #address of a 
print(id(b)) #adreess of b 

print(id(a)==id(b)) #true

 # 1. The both adress are same because python does not store values for different variable in diffrent memory addresses just like c orJava , it just stores the value and attach a tag name (variable name) to that value
 # 2. python create memory for the VALUE , not for the VARIABLE , that is why address of both a & b are same





