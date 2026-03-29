# Methods and Types of Methods in a class 
"""

1. Class Methods
2. Instace Methods 
3. Static Methods 

"""




class Car:
    
    def __init__(self , make , model , year , color):
        self.make = make
        self.model = model
        self.year = year,
        self.color = color
        self.started = False
        self.speed = 0
        self.max_speed = 200
        
  
  
  #-------------------------------------Instance Methods --------------------------------------------------------------
  
  
   #The first parameter has access to the object instance which points to the current object it is commonly written as 'self' , although you can name it anything 
  
    def start(self): 
        self.started = True
        print(f"{self.model} started")
       
        
    
    def stop(self):
        self.started = False
        self.speed = 0
        print(f"{self.model} stopped")
        
    
    def apply_break(self, value):
        if self.speed - value >=0:
            self.speed-=value
            print(f"Reducing Speed to {self.speed} km/h")
            
        else:
            
            self.speed = 0
            print('Car is stopped now ')
            
    
    
    def accelarate(self , value):
        if not self.started:
            print('Please Start the Car')
            return 
        
        elif self.speed+value<=self.max_speed:
            
              self.speed += value
              print(f'Accelarating to {self.speed} km/h')
              
        else:
             self.speed = self.max_speed
            
             print(f"Accelerating to {self.speed} km/h...")

            
        
        
     
     
     
     
     
     
     
     
     

car1 = Car("Mahindra","XUV 700" , "2026" , "white")



car1.start()
car1.accelarate(50)
car1.accelarate(70)
car1.apply_break(30)
car1.accelarate(300)
car1.stop()


#Another syntax using direct classname

Car.start(car1)
# Car.accelarate(50) #TypeError: Car.accelarate() missing 1 required positional argument: 'value'


Car.accelarate(car1 , 50)







# ------------------------Class  Methods -------------------------------------------------



"""
A class method is a method that takes the class object as the first parameter instead of taking 'self' , so a common python convention is to provide it as 'cls' argument

"""

