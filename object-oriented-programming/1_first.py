
class computer:
    """
    A class basically can have properties and it can have behaviour , 
    here properties are the variables for the class ,
    it's behavior is defined by class methods ( functions)
    """
    
    
    # test_variable = 10 -> This is a class variable , not a instance variable so it will be shared by all instances of class (object)
    
    brand_name = "MacBook"
    
    #__init__ is a special method that runs automatically when an object is created.
    
    def __init__(self , version='i3' , space='256GB SSD'):
        self.cpu = version
        self.capacity = space
        
        
    def config(self):
        print(f"The CPU for your machine is {self.cpu} with {self.capacity} space by {self.brand_name}")


comp1 = computer()
comp2 = computer("i5" , "1TB SSD")

print(type(comp1)) # <class 'computer'>

comp1.config()
comp2.config()





# Methods in a Class 


"""

There are two types of methods in a Class 
1. Static Methods-->  ( called with every other object)
2. Class Methods --> Method specifically related to a Class , not a object 

"""


class class_methods:
    brand = "Priyanshu.co"
    
    
    # pass class here in as a argument that we want to refer 
    
    """
    
    A class method receives the class as implicit first argument,
just like an instance method receives the instance.
To declare a class method, use this idiom:
    """
    
    @classmethod
    def info(cls):

        return cls.brand
    





# print(class_methods.info('s')) #AttributeError: 'str' object has no attribute 'brand'


print(class_methods.info()) 



        
        
        


        
    



#static methods in class


class Circle:

    # __init__ is a special instance method (constructor)
    # it runs automatically when you create an object
    # 'self' refers to the specific object being created
    def __init__(self, radius):
        self.radius = radius  # storing radius on the object itself

    # INSTANCE METHOD
    # - has 'self' as first parameter
    # - can access object's data (self.radius)
    # - must be called on an object: c.area()
    # - different objects can give different results
    def area(self):
        return 3.14 * self.radius ** 2

    # STATIC METHOD
    # - @staticmethod decorator tells Python: "no self needed here"
    # - cannot access object data (no self, no radius)
    # - called on the class directly: Circle.is_valid_radius(5)
    # - always gives the same result regardless of any object
    # - just a helper function "parked" inside the class
    @staticmethod
    def is_valid_radius(r):
        return r > 0


# --- using them ---

c = Circle(5)

# calling instance method — needs an object (c)
print(c.area())                    # 78.5

# calling static method — no object needed, called on class itself
print(Circle.is_valid_radius(-3))  # False

























    
    
    


