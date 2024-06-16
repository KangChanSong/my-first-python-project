# sequence data types : strings , lists , tuple , range

t = 1, 2, 'hi!'
print(t[0])
print(t)

one, two, hi = t
print(one)
print(two)
print(hi)

# one, two = t # error!

u = t, (3, 4, 5)
print(u)

# t[0] = 9999 # error! tuples are immutable!

v = ([1, 2, 3], [3, 2, 1])
print(v)

# empty tuple
empty = ()
singletone = 'single',
print(empty)
print(singletone)
