# from raw_data import A


class A:
    
    
    def __init__(self):
        print('A init called')
    
    def f1(self):
        print('f1 works')
    
    def f2(self):
        print('f2 works')    
        
class B(A):
    #class B Inherits a 
    
    
    
    
    def f3(self):
        print('f3 works')
    
    def f4(self):
        print('f4 works')
        
        

class C(B):
    
    #multilevel inheritance
    
    def __init__(self):
        super().__init__() #used to access parent class's attributes
        print('C init called')
    
    
    
  
        


obj = A()
obj.f1()
        
obj2 = B()
obj2.f1()


obj3 = C()

obj3.f2()





