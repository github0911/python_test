#!/usr/bin/python
# -*- coding: utf-8 -*-


def calc_sum(*args):
    x = 0
    for n in args:
        x = x + n
    return x


print(calc_sum(1, 3, 5, 7))


def lazy_sum(*args):
    def sum():
        x = 0
        for n in args:
            x = x + n
        return x
    return sum

# 每次调用都会返回一个新的函数，即使传入相同的参数


f = lazy_sum(1, 3, 5, 7)
f2 = lazy_sum(1, 3, 5, 7)

print(f())
print(f == f2)

# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())

# 匿名函数
# is_odd = lambda x: x % 2 == 1

L = list(filter(lambda x: x % 2 == 1, range(1, 20)))
print(L)