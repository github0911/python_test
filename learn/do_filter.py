#!/usr/bin/python
# -*- coding: utf-8 -*-


def is_odd(x):
    return x % 2 == 1


l = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(l)


def not_empty(s):
    return s and s.strip()


s = list(filter(not_empty,  ['A', '', 'B', None, 'C', '  ']))
print(s)


def odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(not_divisible(n), it) # 构造新序列
