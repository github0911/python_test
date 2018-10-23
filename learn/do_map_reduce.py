#!/usr/bin/python
# -*- coding: utf-8 -*-

L = [1, 2, 3, 4]

# 一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，
# 并把结果作为新的Iterator返回。


def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print(r)

l = list(map(str, [1, 3, 5, 7, 9, 11]))
print(l)

# reduce
from functools import reduce


def add(x, y):
    return x + y

# 再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算


r = reduce(add, L)
print(r)


def fn(x, y):
    return x * 10 + y


i = reduce(fn, [1, 3, 5, 7, 9])
print(i)


def normalise(name):
    if isinstance(name, str):
        return name.title()


L1 = ['adam', 'LISA', 'barT']
L2 = map(normalise, L1)
print(L2)