squares = [1,4,9,16,25]
print(squares)
print(squares[0])
print(squares[1:4])
print(squares[-3:])

print(squares + [36, 49, 64, 81, 100])

squares[0] =9999
print(squares) # lists are mutable!!
squares.append(36)
print(squares)

all_types = [1, 1.5, 'F']
print(all_types)

rgb = ['Red', 'Green', 'Blue']
rgba = rgb
print(id(rgba) == id(rgb)) # they reference the same object
rgba.append('Alph')
print(rgb)

correct_rgba = rgba[:] # shallow copy
print(id(rgba) == id(correct_rgba)) # different references
correct_rgba[-1] = 'Alpha'
print(correct_rgba)
print(rgba)

letters = ['a', 'b', 'c', 'd', 'e']
print(len(letters))
letters[1:3] = ['B', 'C']
print(letters)
letters[1:3] = []
print(letters)
letters[:] = []
print(letters)

alphabets = ['a', 'b', 'c']
numbers = [1,2,3,4,5]
nested = [alphabets, numbers]
print(nested)
print(nested[0])
print(nested[1][3])