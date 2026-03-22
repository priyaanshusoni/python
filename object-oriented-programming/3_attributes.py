"""

Basically There are two types of attributes 

1. Class Attributes 
2. Instance Attributes


"""



# Class attributes are those attributes of a class which are related to whole class rather than a single instance ( object) of the class

# These class atrributes are shared by all the instance of the class 

# For ex:- you can keep a class sttribute "num_instances" which tracks the count of the total number of instances created using a particular class




class ObjectCounter:
    num_instances = 0
    
    def __init__(self):
        ObjectCounter.num_instances+=1
        
        
instance_1 = ObjectCounter()
instance_2 = ObjectCounter()


print(ObjectCounter.__dict__)

print(f"Total Number of instances created are {instance_1.num_instances}")