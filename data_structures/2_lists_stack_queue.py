stack = [1, 2, 3, 4, 5]
print('stack: ', stack)

stack.append(6)
stack.append(7)
print('stack: ', stack)

print('stack.pop(): ', stack.pop())
print('stack: ', stack)
print('stack.pop(): ', stack.pop())
print('stack: ', stack)

from collections import deque

print()
queue = deque([1, 2, 3, 4, 5])
print('queue: ', queue)
queue.append(6)
queue.append(7)
print('queue: ', queue)

print('queue.popleft(): ', queue.popleft())
print('queue: ', queue)
print('queue.popleft(): ', queue.popleft())
print('queue: ', queue)
