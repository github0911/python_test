import logging
logging.basicConfig(level=logging.WARNING)


def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


s = power(5, 2)
print("power {}".format(s))


def fact(x):
    if x == 1:
        return x
    return x * fact(x - 1)


n = fact(4)
# print("fact {}".format(n))
logging.warning(" fact {} ".format(n))


def range_demo(x):
    #
    for n in range(x):
        print("range_demo {}".format(n))


r = range_demo(5)

x = 50


def function_global():
    global x

    print("x is ", x)
    x = 5
    print("change global x is ", x)


function_global()
print("Value of x is ", x)


def function_default(message, times=1):
    print(message * times)


function_default("hello")
function_default("world")
function_default("!", 10)


def function_keys(a=5, b=6, c=7):
    """
    function 关键字

    """
    print("keys a is ", a, ", b is ", b, ", c is ", c)


function_keys(b=10)
print(function_keys.__doc__)


import sys
import os

print("The command line arguments are:")
for i in sys.argv:
    print(i)

print("\n\n The python path is ", sys.path, "\n")
print(os.getcwd())

"""
from..import 语句
警告：一般来说，你应该尽量避免使用 from...import 语句，
而去使用 import 语句。这是为了避免在你的程序中出现名称冲突，同时也为了使程序更加易读。
"""


"""
Python 中有四种内置的数据结构——列表（List）、元组（Tuple）、字典（Dictionary）和集合（Set）
"""

if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')




