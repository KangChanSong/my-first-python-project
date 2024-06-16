tel = {'me': '01030809839', 'mom': '01027555988', 'dad': '01055399839'}
print(tel)
print(tel['dad'])
del tel['mom']
tel['bro'] = '01022221111'
print(tel)

print(list(tel))
print(sorted(tel))
print('me' in tel)
print('mom' not in tel)

print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
print({x: x ** 2 for x in range(1, 4)})
print(dict(one=1, two=2, three=3))
