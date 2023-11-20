# # import math
# # print(dir(math))

# # def factorial(n):

# #     result =1
# #     for i in range(1, n + 1):
# #         result += i
        
# #     return result

# # print("5! = ", factorial(5))

# # import math

# # a = math.factorial(5)
# # print("5! = ", a)

# # from math import comb
# # b = math.comb(5, 2)
# # print('5 Combination 2 = ', b)

# # from math import *
# # print(pi)

# # from math import pow, sqrt

# # a = pow(2, 3)
# # b = sqrt(4)

# # print('pow(2, 3) = ', a)
# # print('sqrt(4) = ', b)

# # from math import pow as p

# # a = p(2, 3)

# # print('p(2, 3) = ', a)

# # from math import pow as p, sqrt as s

# # a = p(2, 3)
# # b = s(4)

# # print('p(2, 3) = ', a)
# # print('s(4) = ', b)

# # import math

# # a = math.pow(2, 3)
# # b = math.sqrt(4)

# # print('math.pow(2, 3) = ', a)
# # print('math.sqrt(4) = ', b)
# # del math
# # print(dir(math))

# # import math
# # a = math.pow(2, 3)
# # b = math.sqrt(4)

# # print('math.pow(2, 3) = ', a)
# # print('math.sqrt(4) = ', b)
# # del math
# # import importlib
# # import math
# # importlib.reload(math)
# # print(dir(math))

# import random
# print(random.random()) 
# print(random.randint(1, 6)) 

# import random as rd
# print(rd.random())
# print(rd.randint(1, 6))
# print(rd.randrange(1, 6))
# numlist = [10, 20, 30, 40, 50]
# rd.shuffle(numlist)
# print(numlist)
# print(rd.choice(numlist))
# print(rd.sample(numlist, 3))

# import sys
# print(sys.path)
# print('-' * 50)
# print(sys.prefix)

# import sys
# print(sys.version)
# print('-' * 50)
# print(sys.version_info)
# print('-' * 50)
# print(sys.copyright)
# print(sys.getwindowsversion())

# import os
# print(os.getcwd())
# print('-' * 50)
# print(os.listdir())
# print('-' * 50)
# print(os.name)

# import calendar
# print(calender.mmonthrange(2020, 12))
# print('-' * 20)
# print(calender.weakday(2020, 8, 31))
# print('-' * 20)
# print(calender.prmonth(2020, 8))
# print('-' * 20)
# print(calender.prmonth(2020, 12))

# text = '파이썬 프로그래밍!'
# with open('python.txt', 'w') as p:
#     p.write(text)

# import pickle

# list = ['a','b','c']
# with open('list.txt', 'wb') as f:
#     pickle.dump(list, f)

# import pickle

# list = ['a','b','c']
# with open('list.txt', 'rb') as f:
#     data = pickle.load(f)

# print(data)

# import tempfile

# filename = tempfile.mktemp()
# print(filename)

# import tempfile, os

# filename = tempfile.mktemp()
# print(filename)

# f = tempfile.NamedTemporaryFile(prefix = "mytemp",suffix = ".txt", dir = tempfile.gettempdir())
# print(f.name)


# import mycom

# print(mycom.add(3, 5))
# print(mycom.sub(3, 5))

# def add(a, b):
#     return a + b
# def sub(a,b):
#     return a - b

# PI = 3.141592

# class Circle:
#     def com1(self, r):
#         return PI * (r ** 2)

# def com2(a, b):
#     return 2*a*b

# import mymod
# print('PI = ',mymod.PI)
# a = mymod.Circle()
# print('반지름이 5일 때 원의 넓이 = ', a.com(5))

