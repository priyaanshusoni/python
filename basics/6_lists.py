# Lists In Python 

a = [1 ,2 ,3 ,4 , 5]



a.append(7) #insert item at the end of the list

a[len(a):] = [8 , 9 , 8] #also insert item at the end of the list

a.extend([1,2,3,4])


#index() method 


print([1,2,3,4,56].index(56)) #print index of a particular value

try:
    print([1,2,3,4,56].index(56, 0 ,3)) #print index of a particular value from starIndex , to endIndex (specified)
except:
    print('No element found for this particulat search window')
    
    
#The Number of times a particular element appears in the list 

print(f'1 Appears "{a.count(1)}" times in {a}')




#Using Lists as Stack

stack = [1 ,2 ,3 ]

stack.append(4)


recent = stack.pop()

print(f"{recent} is the top most element of this stack")
    




#Implementing List as a Queue in Python


class queue:
    
    def __init__(self):
        self.data = []
        
    
    def insert(self , value):
        self.data.append(value)
        
        
    def qpop(self):
       
       return self.data.pop(0)
        



q1 = queue()

q1.insert(9)
q1.insert(2)
q1.insert(3)



print(f" first entered element is {q1.qpop()}")







