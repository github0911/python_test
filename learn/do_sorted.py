#!/usr/bin/python
# -*- coding: utf-8 -*-

s = sorted([36, 5, -12, 9, -21])
print(s)

s = sorted([36, 5, -12, 9, -21], key=abs)
print(s)

s = sorted([36, 5, -12, 9, -21], key=abs, reverse=True)
print(s)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 元组


def by_name(t):
    return t[0]


def by_score(t):
    return t[1]

L2 = sorted(L, key=by_name)

L3 = sorted(L, key=by_score, reverse=True)

print(L2)
print(L3)