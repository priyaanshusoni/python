from raw_data import john


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




#------------Instance Attributes--------------------------------



class Car:
    
    def __init__(self , make , model , year , color):
        self.make = make
        self.model = model
        self.year = year,
        self.color = color
        
    def get_values(self):
        return  {
            self.make,
            self.color,
            self.year,
            self.model
        }
        
        
        

car1 = Car("Honda" , "S3" , "2009" , "White")

print(car1.__dict__)
print(car1.get_values())




#accessing instance attributes through class will throw an  Attribute error

# print(Car.make)


#-------------------The  .__dict__ attribute  ------------------------

"""

This .__dict__ attribute holds the all the memebrs & functions declared inside a particualr class  if it is called upon an instance it shows the related mebers on an instance and if called upon a class it shows the attributes of a particular class 

"""

class SampleClass:
    class_attr = 100
    
    
    def __init__(self , instance_attr):
        self.instance_attr = instance_attr
        
    
    def method(self):
        print(f"class attribute : {self.class_attr}")
        print(f"Instance attribute : {self.instance_attr}")



print(SampleClass.class_attr)
simple_dictionary = SampleClass.__dict__



print(simple_dictionary) 

"""
{'__module__': '__main__', 'class_attr': 100, '__init__': <function SampleClass.__init__ at 0x7c05d091d1c0>, 'method': <function SampleClass.method at 0x7c05d091d260>, '__dict__': <attribute '__dict__' of 'SampleClass' objects>, '__weakref__': <attribute '__weakref__' of 'SampleClass' objects>, '__doc__': None}

"""
print(simple_dictionary['class_attr'])


# But if we try to access this __dict__ method on a particular instance of a class (object)


sample_instance = SampleClass('instance_attribute_1')



print(sample_instance.__dict__) # {'instance_attr': 'instance_attribute_1'}





#Dynamic class and instance attributes ---------------------------------------------------------------


class Record:
    "Hold the record of something"

john_record = Record()


for field,value in john.items():
    setattr(john_record , field, value)



print(john_record.name) #Works
 