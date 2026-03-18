#Creating a new list with the values doubled 


singles = [ 1 ,2 ,3 ,4 ,5]

doubles = [x*2 for x in singles ]

print(doubles) # [ 2 ,4 ,6 , 8 ,10 ]



print([x for x in singles if x%2 == 0])   # [2 ,4 ]




float_nums = [ -1.1 , 3.4 , 5.7]


print([abs(x) for x in float_nums])


#storing a tuple from list_comprehnesion syntax

print([(x , x**2) for x in singles])


nested_list = [[1 ,2 ,3 ] , [4 ,5 ,6]]


[print(element) for sub_list in nested_list for element in sub_list]



