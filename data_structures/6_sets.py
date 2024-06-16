s = {1, 1, 1, 2, 3, 3, 4, 5, 5, 5, 5}
print(s)

# empty_set = {} # dictionary!!
empty_set = set()
print(len(empty_set))
a = set('aabbccccdddeeff')
b = set('ddddeeeefffggghhhiii')
print(a)
print(b)
print('a - b : ', a - b)  # 차집합
print('a | b : ', a | b)  # 합집합
print('a & b : ', a & b)  # 교집합
print('a ^ b : ', a ^ b)  # 각 여집합

print({x for x in 'abracadabra' if x not in 'abc'})
