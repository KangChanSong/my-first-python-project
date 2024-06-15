words = ['cat', 'dog', 'horse']
for w in words:
    print(w, len(w))

users = {'Hans': 'active', 'Chan': 'inactive', 'Bob': 'active'}

print(users.items())

for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

print(users)

active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

print(active_users)
