for i in range(5):
    print(i)

print(list(range(5, 10)))
print(list(range(10, 100, 30)))
print(list(range(-10, -100, -30)))

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i], len(a[i]))

print(range(10))
print(sum(range(10)))
# range() does not make lists so it saves spaces
