# operator order
# -> numerical operators > comparison operators > Boolean operators

list = [1, 2, 3, 4, 5]
list_ = [1, 2, 3, 4, 5]

print('1 in list:', 1 in list)
print('1 not in list:', 1 not in list)
print('list_ is list:', list_ is list)  # false
print('list_ is not list:', list_ is not list)  # true

print('1 < 2 == 2:', 1 < 2 == 2)

# A and not B or C == (A and (not B)) or C

string1, string2, string3 = '', 'Hi', 'Hey'

non_null = string1 or string2 or string3
print(non_null)

# TODO: learnn warlus operators
