"""Lambda Functions"""

get_sum = lambda x, y: x + y


print(get_sum(3, 4))

print(type(get_sum))


# using map


numbers = [1, 2, 3, 4, 5, 6]

ans = map(lambda x: x**2, numbers)


ans2 = filter(lambda x: x % 2 == 0, numbers)

print(list(ans))
print(list(ans2))
