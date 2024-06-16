## looping techniques
games = {'fps': 'half-life', 'rpg': 'elder scrolls', 'quiz': '369'}
for k, v in games.items():
    print(k, v)

print()

for i, v in enumerate(['zero', 'one', 'two', 'three']):
    print(i, v)

print()

questions = ['How are you?', 'what is your name?', 'how is the weather today ?']
answers = ["I'm good!", 'My name is Chan', 'It is rainy']

for q, a in zip(questions, answers):
    print(q, a)

print()

for i in reversed(range(1, 10, 2)):
    print(i)

print()
unsorted = 'bcdagef'
for c in sorted(unsorted):
    print(c)

print()
for c in sorted(set('dddddddbbbbbbcccccccaaaa')):
    print(c)
