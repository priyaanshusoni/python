


print("Hello, World!")
print(5/5)
print(5//5)
print(5**2)


# String s 

s = "Priyanshu";


# characters from index 0 to 4 - 1
print(s[0:4]) 

# If i ommit the first index it , defaults to 0

print(s[:4])

# if i ommit the last index it , defaults to len(s)
print(s[3:])

# negative indexing
print(s[-4:-1])


# Formula 

# S[i:] + s[:i] = s 
#


print(s[2:] + s[:2])  # ryanshu + Pi = Priyanshu




s = 'Google India LLC'


print(len(s))  # length of string




listExample = [1, 2, 3, 4, 5]
listExample2 = ['a', 'b', 'c', 'd', 'e'
]

temp = listExample[1:4]   #slicing returns a new list 
print(temp)

listExample2.append('f')  # adding an element to the list
print(listExample + listExample2)  # concatenation of lists





# Python stores the refrence of the list not the actual list when we assign one list to another
listA = [1, 2, 3]
listB = listA

listB.append(4)
print(listA)  # both listA and listB will reflect the change

