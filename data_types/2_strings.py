# print('C:\some\name') # error!
print(r'C:\some\name')

print("""\
Hello\
안녕하세요\
니하오\
""")

print("""
Hello
안녕하세요
니하오
""")

print(3 * 'boom! ' + 'lol')

print('boom!' 'lol') # only for string literals
print('안녕하세요! '
      '저는 송강찬입니다! '
      '뭐요?')

# prefix = 'Py'
# print(prefix 'thon') # error!

word = 'abcdefg'
print(word[0])
print(word[-1])
print(word[5])
print(word[0:2])
print(word[2:])
print(word[-2:])

#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1

# word[40] # out of range !!
print(word[40:0])
print(len(word))

# string is IMMUTABLE!!