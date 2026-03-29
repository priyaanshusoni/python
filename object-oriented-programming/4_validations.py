#How to apply a validation of a particular class attribute suppose if there's a circle class which accepts radius at the time of object creatin how would you apply a validation logic to only accepts valid radius ?




class Circle:
    
    
    def __init__(self, radius):
        self.radius = radius
        
    
    
    @property
    def radius(self):
        print('Getter Called')
        return self._radius
    
    
    @radius.setter
    
    def radius(self , value):
        print("Setter Called")
        
        if isinstance(value , int | float) and value > 0:
            self._radius = value
        else:
            raise ValueError("Only Positive or Floating Numbers are accepted as radius")
        
        
    @radius.deleter
    def radius(self):
        print('Deletter Called')
        del self._radius
           


prop = Circle.radius

print({
    "getter" : prop.fget is not None,
    "setter" : prop.fset is not None,
    "deleter": prop.fdel is not None,
})

# {'getter': True, 'setter': True, 'deleter': False}



circle1 = Circle(4)


print(circle1.radius)
del circle1.radius
