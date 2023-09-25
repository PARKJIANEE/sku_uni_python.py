# str9 = ' Computer Security '
# print(str9.replace('Security','보안'))
# print(str9.replace('t','T'))
# print(str9)
# print(str9.strip())
# print(str9.lstrip())
# print(str9.rstrip())
# print(str9.split())

# str10= 'www.sungkyul.ac.kr'
# print(str10.split('.'))

# poem= ''' 우리들은 모두
# 무엇이 되고 싶다.
# 너는 나에게 나는 너에게
# 잊혀지지 않는 하나의 눈짓이 되고 싶다'''
# print(poem.splitlines())
# print("$".join(str9))
# print("+".join(str9))
# print(str9.isalpha()) #공백이 아예 없어야 TRUE
# print(str9.isnumeric())
# print(str9.isalnum()) #공백이 아예 없어야 TRUE

# a = '123'
# print(a.isalpha())
# print(a.isnumeric())
# print(a.isalnum())

# str11= 'Department of {}'
# print(str11.format('Computer'))

# str12= 'Department of {} {}'
# print(str12.format('Computer', 'Engineering'))

# str13= 'hello, {0} {1}'
# print(str13.format('Computer', 'Engineering'))

# str14= 'hello, {str1}{str2}'
# print(str14.format(str1='컴퓨터',str2='공학과'))

# str144='Department of 12345678901234567890'
# print(str144)

# str15= 'Department of {:20}'
# print(str15.format('Engineering')+'/')
# str15='Department of {:<20}' 
# # 차지하는 공간내 왼쪽 정렬
# print(str15.format('Engineering')+'/')
# str15='Department of {:>20}' 
# # 차지하는 공간내 오른쪽 정렬
# print(str15.format('Engineering')+'/')
# str15='Department of {:^20}' 
# # 차지하는 공간내 가운데 정렬
# print(str15.format('Engineering')+'/')

# 차지하는 공간을 다른 문자열로 채움
# str15='Department of {:@<20}'
# print(str15.format('Engineering')+'/')
# str15='Department of {:#>20}'
# print(str15.format('Engineering')+'/')
# str15='Department of {:$^20}'
# print(str15.format('Engineering')+'/')

# str16='원주율의 값은 {:.7f}'
# print(str16.format(3.141592653897))
# str16='원주율의 값은 {:10.4f}'
# print(str16.format(3.141592653897))

# str17= 'Computer Engineering'
# L2= [2020, 2021, 2022]
# print(len(str17))
# print(len(L2)) 
# str17= '파이썬은 정말 재미있어요!'
# print(len(str17))
# print(ord('a'))
# print(ord('ㄱ'))
# print(chr(97))
# print(chr(12593))

# print(hex(9))
# print(hex(10))
# print(hex(11))
# print(hex(12))
# print(hex(13))
# print(hex(14))
# print(hex(15))
# print(hex(16))
# print(oct(8))
# print(oct(9))
# print(oct(16))

# print(int(3.14159))
# print(3.14159)
# print(int(7/3))
# print(7/3)
# print(int('3000'))
# print('3000')

# data=int(input("정수를 입력하시오 : "))
# print(type(data))
# print(data+1)

# print(float(3))
# print(float(6/3))
# print(float('3000'))
# print(float('3.1234'))
# data=float(input("실수를 입력하시오 : "))
# print(type(data))
# print(data+1)
# age=input("나이를 입력하시오 : ")
# # age = 20
# message= age+' 번째 생일을 축하합니다'
# print(message)
