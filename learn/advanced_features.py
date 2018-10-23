#!/usr/bin/python
# -*- coding: utf-8 -*-

# 高级特性
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = list(range(1, 11))
print(l)

# [1x1, 2x2, 3x3, ..., 10x10]
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

# 循环的处理
L = [x * x for x in range(1, 11)]
print(L)

# 两层循环(嵌套循环)
TL = [a + b for a in 'abc' for b in 'defg']
print(TL)