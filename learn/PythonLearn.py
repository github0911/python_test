# -*- coding: utf-8 -*-
import time
import calendar
import keyword
from Card import*
from Game import*

print(keyword.kwlist)
# 第一个注释
print("第一个注释 注释已 # 开头")
localtime = time.localtime(time.time())
print(localtime)

# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# 获取某月日历
cal = calendar.month(2019, 7)
print(cal)

print("Hello world!")
# 操作符
print("-------操作符 start-------")
x = 2 ** 3
print("2 ** 3 指数运算 = {}".format(x))
x = 2 % 3
print("2 % 3 取模运算 = {}".format(x))
x = 4 // 2
print("4 // 2 整除 = {}".format(x))
x = 4 / 3
print("4 / 3 除法 = {}".format(x))
x = 4 * 3
print("4 * 3 乘法 = {}".format(x))
x = 4 + 3
print("4 + 3 加法 = {}".format(x))
x = 4 - 3
print("4 - 3 减法 = {}".format(x))
print("-------操作符 end-------")

# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# 可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。

for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != j) and (j != k) and (i != k):
                print(i, j, k)

# 逻辑操作符
print("------- 逻辑操作符 and or not start-------")
print("逻辑操作符 与 and 1 != 2 and 2 != 3 {}".format(1 != 2 and 2 != 3))
print("逻辑操作符 或 or 1 != 2 or 2 != 3 {}".format(1 != 2 or 2 != 3))
# 将关键字 not 放置在表达式的前面，将改变表达式的求值结果，逆转为原本结果的对立值。
print("逻辑操作符 非 not 1 != 2 {}".format(not 1 != 2))
print("------- 逻辑操作符 and or not end-------")

# 条件语句 if elif else

x = 5
if x == 5 :
    print("x == 5 {}".format(x == 5))
else :
    print("x != 5")

if x == 1:
    print("x == 1 {}".format(x == 1))
elif x == 2:
    print("x == 2 {}".format(x == 2))
elif x == 3:
    print("x == 5 {}".format(x == 5))
else:
    print("都不相等")

x = 8
if x < 8:
    print("x 小于 8")
else:
    print("x 大于或等于 8")

x = 21

if x <= 10:
    print("x > 10")
elif x > 10 and x <= 25:
    print("x > 10 and x <= 25")
elif x > 25:
    print("x > 25")

# 函数 函数应该做一件事。做好这件事。只能做这一件事。

# 函数必须包含return 如果函数没有return语句，则会返回None

x = int("110")
print(x)

# 数组定义的方式 fruit = list() or fruit = ["orange"] 数组符号是 []
# fruit = list()
# print(fruit)
fruit = ["orange"]
print(fruit)
fruit.append("apple")
print(fruit)
fruit.pop()
print(fruit)
fruit.append("lemon")
print(fruit)
fruit.reverse()
print(fruit)
print(len(fruit))
result = "apple" in fruit
print(result)
result = "apple" not in fruit
print(result)
# 字典定义的方式 my_dict = dict() my_dict = {} 字典符号是{}
my_dict = dict()
print(my_dict)
my_dict["first"] = "dict"
print(my_dict)

words = ["P", "y", "t", "h", "o", "n", "!", "!", "."]
one = "".join(words)
print(one)
one = " ".join(words)
print(one)
s = "   python    is     very good"
print(s.strip())
print(s.replace(" ", ""))

# 面向对象编程有四大概念：封装、抽象、多态、继承

card1 = Card(12, 2)
print(card1)
card2 = Card(11, 3)
print(card2)
print(card1 < card2)

game = Game()
game.play_game()