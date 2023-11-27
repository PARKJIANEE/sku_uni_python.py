# # 10 표준라이브러리

# # 값의 절대값을 반환한다.
# print("abs(-3) = ", abs(-3))

# # 가장 큰 값을 반환한다.
# print("max(2, 3, 5) = ", max(2, 3, 5))

# # 가장 작은 값을 반환한다.
# print("min(2, 3, 5) = ", min(2, 3, 5))

# # a^b를 반환한다.(=a**b)
# print("pow(2, 3) = ", pow(2, 3))

# # 소수점을 가까운 정수까지 반올림, 버림하여 반환한다.
# print("round(2.5) = ", round(2.5))
# print("round(2.7) = ", round(2.7))
# # 소수점을 가까운 정수까지 반올림, 버림하여 반환한다.
# print("round(3.5) = ", round(3.5))


# # 수학 라이브러리(math) 
# import math
# print("math.fabs(-2) = ", math.fabs(-2)) # 2.0 
# print("math.ceil(2.1) = ", math.ceil(2.1)) # 무조건 올림 3
# print("math.ceil(-2.1) = ", math.ceil(-2.1)) # 무조건 올림 -2
# print("math.floor(2.1) = ", math.floor(2.1)) # 무조건 내림 2
# print("math.floor(-2.1) = ", math.floor(-2.1)) # 무조건 내림 -3

# # 인터넷 엑세스(urllib)
# import urllib.request
# address = urllib.request
# check = address.urlopen('http://www.sungkyul.ac.kr')
# print(check)
# print(check.status)
# print(check.read())

# import urllib.request
# url = 'http://www.pythonchallenge.com'
# site = urllib.request.urlopen(url).read().decode('utf-8')
# print(site)

# import urllib.parse
# parse  = urllib.parse.urlparse('http://www.pythonchallenge.com/pc/def/0.html')
# print(parse)
# import urllib.parse
# parse  = urllib.parse.urlparse('https://sports.news.naver.com/index')
# print(parse)

# # 시간과 날짜(time)
# import time
# t = time.time()
# print(t)

# t = time.time()
# time_local = time.localtime(t)
# print(time_local)

# t = time.time()
# time_utc = time.gmtime(t)
# print(time_utc)

# print(time.strftime('%Y-%m-%d', time.localtime(time.time())))
# print(time.strftime('%c', time.localtime(time.time())))
# print(time.strftime('%B', time.localtime(time.time())))


# #  시간과 날짜(datetime)
# import datetime
# print(datetime.datetime.today())
# today = datetime.datetime.today()
# print(today.year, today.month, today.day, today.hour, today.minute, today.second)

# today = datetime.datetime.today()
# dday = datetime.datetime(2023, 12, 4, 12, 45, 00)
# sat = dday - today
# print(sat)

# import time
# t = time.time()
# time.sleep(10)

# t2 = time.time()

# spendtime = t2 - t 
# spendtime = int(spendtime)

# print("Before tinestemp: ", t)
# print("After timestemp: ", t2)

# import numpy as np
# ar = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(ar)
# print(type(ar))

# data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# answer = []
# for di in data:
#     answer.append(2 * di)
# print(data)
# print(answer)

# data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# x = np.array(data)
# print(x)
# print(x * 2)

# c = np.array([[0, 1, 2], [3, 4, 5]]) # 2 x 3 array
# print(c)
# print(len(c)) # 행의 갯수
# print(len(c[0])) # 얄의 갯수

# d = np.array([[[1, 2, 3, 4],
#                [5, 6, 7, 8],
#                [9, 10 , 11, 12]],
#                [[11, 12, 13, 14],
#                 [15, 16, 17, 18],
#                 [19, 20, 21, 22]]]) # 2 x 3 x 4 array 
# print(d)
# print(len(d),len(d[0]), len(d[0][0]))

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.arange(1, 11)
# y = x * 10

# plt.plot(x, y, "r")
# plt.xlabel('x line')
# plt.ylabel('y line')
# # plt.plot(x, y)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.arange(1, 5, 0.5)

# y = x * 10
# y2 = 50 - (x * 10)

# plt.plot(x, y, 'r', label = 'red')
# plt.plt(x, y2, 'k', label = 'black')
# plt.legend(loc = 'upper right')
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.arange(1, 5)
# y = x * 5

# plt.bar(x, y)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.arange(-7, 7, 0.1) 
# y = x * x

# plt.xlabel('x')
# plt.ylabel('y')

# plt.plot(x, y)
# plt.show()
