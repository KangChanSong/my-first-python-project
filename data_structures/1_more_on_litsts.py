list = [1, 2, 3, 4, 5]

list.append(6)
print(list)

list[len(list):] = [7]
print(list)

list.insert(len(list), 8)
print(list)

list.insert(99, 0)  # ? 되넹..
print(list)

iterable = range(9, 11)
list.extend(iterable)
print(list)

list.append(0)
list.remove(0)
print(list)

pop1 = list.pop()
print('pop:', pop1, 'list:', list)

pop2 = list.pop(len(list) - 1)
print('pop:', pop2, 'list:', list)

index = list.index(5)
print('index: ', index)

# index = list.index(5, 5, len(list) - 1) # error!

list.append(1)
print('count: ', list.count(1), 'list: ', list)

list.sort()  # built-in library 참조
print('sort: ', list)

list.reverse()
print('reverse: ', list)

print('list.copy() == list[:]: ', list.copy() == list[:])
