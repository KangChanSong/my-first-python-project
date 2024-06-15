for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, ' equals ', x, ' * ', n // x)
            break
    else:
        print(n, ' is a prime number')

# In a for loop, the else clause is executed after the loop reaches its final iteration.
# In a while loop, it’s executed after the loop’s condition becomes false.
# In either kind of loop, the else clause is not executed if the loop was terminated by a break.

# a try statement’s else clause runs when no exception occurs,
# and a loop’s else clause runs when no break occurs

for n in range(2, 10):
    if n % 2 == 0:
        print('Found an even number ', n)
        continue
    print('Found an odd number ', n)
