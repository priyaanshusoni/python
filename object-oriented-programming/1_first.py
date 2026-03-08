
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



    
    
    


