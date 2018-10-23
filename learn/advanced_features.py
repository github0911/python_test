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

'''
字符串转换
print(str.upper())          # 把所有字符中的小写字母转换成大写字母
print(str.lower())          # 把所有字符中的大写字母转换成小写字母
print(str.capitalize())     # 把第一个字母转化为大写字母，其余小写
print(str.title())          # 把每个单词的第一个字母转化为大写，其余小写
'''
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = []
L3 = []
for s in L1:
    if isinstance(s, str):
        L2.append(s.lower())
        L3.append(s.upper())

print(L2)
print(L3)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')


# 生成器 generator

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

# 这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return "done"


fib(6)


# 迭代器


from collections import Iterable, Iterator

print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance((), Iterable))

print(isinstance([], Iterator))
