# -*- coding: utf-8 -*-
import logging
logging.basicConfig(level=logging.INFO)


class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError("bad score")

    def get_grade(self):
        if self.__score > 90:
            return "A"
        elif 70 < self.__score <= 90:
            return "B"
        else:
            return "C"

    def jump(self):
        return ""


stu = Student("just.do.it", 88)
print("stu name {}".format(stu.get_name()))
# stu.set_score(-1)
print("stu grade {}".format(stu.get_grade()))