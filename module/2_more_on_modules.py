from fibo import fib

fib(500)

# fibo.fib(500) error! fibo is not defined

from fibo import *

fib(500)

import fibo as fib

fib.fib(100)

from fibo import fib as fibonacci

fibonacci(100)

# each module is only imported once per interpreter session.
