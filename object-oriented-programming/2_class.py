"""
A bit theory :



1. You use classes to model complex data structures and behaviors in a modular way.
2. You define classes in Python using the class keyword, and instantiate them to create objects.
3. A class is a blueprint, while an object is an instance of a class.
4. Methods define behaviors, while attributes store data within class instances.
5. Instance attributes are unique to each object, while class attributes are shared across all instances of the class.

Think of a class like it is a blueprint of something , for example 'class House' , is basically a blue of a house through this blue print you can create many other houses (objects) , because they all will followa same kind of blueprint ( structure) 


"""


import math



class Circle:
    
    # author_name = 'Priyanshu' by default all the members of a class are public to make ir private just put a leading underscore at the start 
    _author_name = 'priyanshu'
    def __init__(self , radius):
        self.radius = radius
        
        

        
        
    def calculate_area(self):
        return format(math.pi * self.radius **2, ".2f")
    
    
    
    

circle_1 = Circle(5)

print(f"Area of circle with radius -> {circle_1.radius} is : {circle_1.calculate_area()}")





