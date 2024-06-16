squares = []
for x in range(10):
    squares.append(x ** 2)

print(squares)
print(x)  # variable still exists

squares.clear()
squares = list(map(lambda x: x ** 2, range(10)))
print(squares)

squares.clear()
squares = [x ** 2 for x in range(10)]
print(squares)

print([(x, y) for x in range(4) for y in range(4) if x != y])

vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec for num in elem])

from math import pi

print([str(round(pi, i)) for i in range(1, 6)])

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print([[row[i] for row in matrix] for i in range(4)])
print(list(zip(*matrix)))
