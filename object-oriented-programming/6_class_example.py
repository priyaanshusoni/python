from datetime import datetime


class Employee:
    company = "Example, Inc."
    
    
    def __init__(self , name , birth_date):
        
        self.name = name
        self.birth_date = birth_date
    
    
    
    @property
    def birth_date(self):
        return self._birth_date
        
    
    
    @birth_date.setter
    
    def birth_date(self , value):
        if  isinstance(value , str):
          self._birth_date = datetime.fromisoformat(value)
        else:
            raise ValueError('Provide a Valid Date please')
        
    
    def compute_age(self):
        today = datetime.today()
        
        age = today.year - self.birth_date.year
        
        birthday = datetime(
            today.year,
            self.birth_date.month,
            self.birth_date.day
        )
        if today < birthday:
            age -= 1
        return age
        
        
        
        
        
   
a = Employee('Manasvi' , '2003-12-16')
   
   
print(a.birth_date)


a.birth_date = '2003-09-27'
        
        
print(a.birth_date)