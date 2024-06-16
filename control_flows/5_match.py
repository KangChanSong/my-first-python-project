def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 401 | 403 | 404:
            return "Not Allowed"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"


print(http_error(403))


def printPoint(point):
    match point:
        case (0, 0):
            return "Origin"
        case (0, y):
            return f"Y={y}"
        case (x, 0):
            return f"X={x}"
        case (x, y):
            return f"X={x}, Y={y}"
        case _:
            raise ValueError("Not a point")


print(printPoint((1.0, 0)))


class Point:
    __match_args__ = ('y', 'x')  # 패턴 매칭 시 순서 지정

    def __init__(self, x, y):
        self.x = x
        self.y = y


def where_is(point):
    match point:
        case Point(0, 0):
            print("Origin")
        case Point(0, y):
            print(f"Y={y}")
        case Point(x, 0):
            print(f"X={x}")
        case Point(x, y) if x == y:
            print(f"X and Y are same: X={x}, Y={y}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")


where_is(Point(1, 0))
where_is(Point(1, 1))

from enum import Enum


class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'


color = Color(input("'Enter your choice of 'red', 'blue' or 'green': "))


def print_color(color):
    match color:
        case Color.RED:
            print("I see red!")
        case Color.GREEN:
            print("Grass is green")
        case Color.BLUE:
            print("I feel blue")


print_color(color)
