def fib(n):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


fib(1000)

f = fib
f(1000)

print(id(fib) == id(f))
print(f(0))


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


# ask_ok('Do you really want to quit?')
# ask_ok('OK to overwrite the file?', 2)
# ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

i = 5


def f(arg=i):
    print(arg)


i = 6
f()


def f(a, L=[]):
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))


def f_better(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


print(f_better(1))
print(f_better(2))
print(f_better(3))


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any ", kind, "?")
    print("-- I'm sorry, we're all out of ", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


def standard_arg(arg):
    print(arg)


def pos_only_arg(arg, /):
    print(arg)


def kwd_only_arg(*, arg):
    print(arg)


def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


standard_arg('Hi')
standard_arg(arg='Hi')
pos_only_arg('Hi')
# pos_only_arg(arg='Hi') # error!
# kwd_only_arg('Hi') # error !
kwd_only_arg(arg='Hi')
combined_example('Hi', 'Hi', kwd_only='Hi')


def foo(name, /, **kwds):
    return 'name' in kwds


print(foo(1, **{'name': 2}))
