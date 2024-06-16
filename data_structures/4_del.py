a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del a[0]
print(a)

del a[2:4]
print(a)

del a[:]
print(a)

a = [1, 2, 3, 4, 5]
del a
# print(a) # error! a is not defined
