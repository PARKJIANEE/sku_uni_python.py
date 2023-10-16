a=int(input('1에서 100사이의 정수를 입력하세요 : '))
if(a==100) :
    print('입력한 정수가 100입니다')
    print('a = %d' % a)
if(a<100) :
    print('입력한 정수가 100보다 적음')
    print('a = %d' % a)

    print('프로그램 종료')

a=int(input('1에서 100사이의 정수를 입력하세요 : '))
if(a<100) :
    print('입력한 a의 값은 %d이며 100보다 작음' % a)
else :
    print('입력한 a의 값은 %d이며 100보다 큼' % a)

print('프로그램 종료')

a=int(input('1에서 10사이의 정수를 입력하세요 : '))
if(a % 2 == 0) :
    print('입력한 a의 값은 %d이며 짝수임' % a)
else :
    print('입력한 a의 값은 %d이며 홀수임' % a)

print('프로그램 종료')

a=int(input('-10에서 10사의 정수를 입력하세요 : '))
if(a >= 0) :
    if(a == 0) :
        print('입력한 정수는 0임')
    else :
        print('입력한 정수는 %d이고 양수임' % a)
else :
    print('입력한 정수는 %d이고 음수임' % a)

age=int(input('나이를 입력하세요 : '))
score=int(input('점수를 입력하세요 : '))
if age >= 20 :
    if score >= 80 :
        print('합격입니다!')
    else :
        print('점수가 낮아 불합격입니다!')
else : 
    print('너무 어려서 불합격입니다!')

money=int(input('지갑에 얼마 있습니까?'))
if money >= 3000 :
    print('과자를 사먹자~~')
elif money >= 1000 :
    print('껌을 사먹어야지~~')
    # pass
else :
    print('공기나 마시자 ㅠ.ㅠ')


a=int(input('-10에서 10 사이의 정수를 입력하세요 : '))
if(a>10) :
    print('입력한 정수는 %d이고 10보다 큼' % a)
elif(a>0) :
    print('입력한 정수는 %d이고 양수임' % a)
elif(a==0) :
    print('입력한 정수는 0임')
elif(a<-10) :
    print('입력한 정수는 %d이고 -10보다 작음' % a)
else :
    print('입력한 정수는 %d이고 음수임' % a)

pocket=[]
pocket.append(input('주머니에 있는 것은?(money,card,...) : '))
if 'money' in pocket :
    print('택시 타고 가자~~')
elif 'card' in pocket :
    print('모범택시 타고 가자^^')
else :
    print('걸어가야겠따 :)')
# print('포켓안에 무엇이 들어 있을까요?',pocket)

score = int(input('점수를 입력하세요 : '))
if score >= 90 :
    grade = 'A'
elif score >= 80 :
    grade = 'B'
elif score >= 70 :
    grade = 'C'
elif score >= 60 :
    grade = 'D'
else :
    grade = 'F'
print('{0}점은 "{1}" 학점입니다.'.format(score,grade))

score = int(input('점수를 입력하세요 : '))
if(score >= 95) and (score <= 100) :
    grade = 'A'
elif score >= 90 :
    grade = 'A'
elif score >= 85 :
    grade = 'B+'
elif score >= 80 :
    grade = 'B'
elif score >= 75 :
    grade = 'C+'
elif score >= 70 :
    grade = 'C'
elif score >= 65 :
    grade = 'D+'
elif score >= 60 :
    grade = 'D'
else :
    grade = 'F'
if score > 100 or score <0 :
    print('점수는 0에서 100까지 입력해야 합니다')
else :
    print('{0}점은 "{1}" 학점입니다.'.format(score,grade))

year=int(input('연도를 입력하세요 : '))
if(((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)) :
    print('%d년은 윤년입니다.' % year)
else :
    print('%d년은 평년입니다.' % year)

for i in range(50) :
    print('Hello, World!')

sum = 0
for n in range(1,10) :
    sum=sum+n

    print(sum)

sum_even = 0
sum_odd = 0
for n in range(1,101) :
    if n% 2 == 0 :
        sum_even += n
    else :
        sum_odd += n
print('짝수의 합 = ', sum_even) 
print('홀수의 합 = ', sum_odd)

for i in range(10) :
    print(i, end=' ')
print()

for i in range(1,15) :
    print(i, end=' ')
print()

for i in range(1,15,2) :
    print(i,end=' ')
print()

for i in range(15,-1,-1) :
    print(i, end=' ')
print()

l1 = list(range(10))
l2 = list(range(0,10,2))
l3 = list(range(10,-1,-1))
print(l1); print(l2); print(l3)

for i in range(1,10) :
    guguLine = ""
    for k in range(2,10) :
        guguLine += str("%d%d=%2d, " % (k,i,k*i))
    print(guguLine)

L_1 = ['one', 'two', 'three']
for i in L_1 :
    print(i)
L_2 = [(1,5), (2,6), (3,7)]
for(a,b) in L_2 :
    print(a+b)

score = [90,25,67,45,80]
number = 0 
for s in score :
    number = number +1 
    if s >= 60 :
        continue
    print('%d번 학생 %d점으로 합격입니다. 축하합니다!' % (number,s))

x=int(input('숫자를 입력하세요 : '))
for i in range(1,x+1) :
    print('+',*i)

x=int(input('가로의 숫자를 입력하세요 : '))
y=int(input('세로의 숫자를 입력하세요 : '))
for i in rnage(y,0,-1) :
    print('*' *x)

x=int(input('숫자를 입력하세요 : '))
for i in range(1,x+1,1) : 
    print((x-i) * ' '+'* '* i)

x=int(input('숫자를 입력하세요 : '))
for i in range(1,x+1) :
    if not(i % 5 == 0) :
        print(i,end = ' ')
print() 

x=int(input('숫자를 입력하세요 : '))
a=1
for i in range(0,11) : 
    print('{0:6,}'.format(a<<i),end='-')
print()

num = 0
while num < 5 :
    print('파이썬 프로그래밍!')
    num += 1

num = int(input('반복할 횟수 : '))
i=0
while i<num : 
    print('파이썬 프로그래밍!')
    i += 1

i,hap =0,0
num1,num2,num3=0,0,0
num1=int(input("시작 값을 입력하세요 : "))
num2=int(input("끝값을 입력하세요 : "))
num3=int(input("증감값을 입력하세요 : "))
i=num1
while i < num2 +1 :
    hap =hap + i
    i = i + num3
print("%d에서 %d까지 증가시간 값의 합계 : %d" % (num1,num2,num3,hap))

import random
i=0
while i != 5 :
    i = random.randint(1,6)
    print()
print('드디어', i, '가 나왔네요~~')

hap,a,b=0,0,0
while True :
    a=int(input("첫 번째 수를 입력하세요(0을 입력하면 종료) : "))
    if a== 0 :
        break
    b=int(input("두 번째 수를 입력하세요 : "))
    hap=a+b 
    print("%d + %d = %d" % (a,b,hap))

print("0을 입력해 반복문을 탈출했습니다")

while True :
    num=int(input('점수를 입력하세요(음수는 종료) : '))
    if num < 0 :
        break
    
    if num >100 :
        print('올바른 정수가 아닙니다.\n 0~100 사이의 정수를 입력하세요\n')
        continue

if score >= 90 :
    grade = 'A'
elif score >= 80 :
    grade = 'B'
elif score >= 70 :
    grade = 'C'
elif score >= 60 :
    grade = 'D'
else :
    grade = 'F'
if num == 100 :
    grade += '+'
elif num > 60 :
    if(num % 10 >= 5) :
        grade += '+'
print('{0}점은 "{1}" 학점입니다.'.format(score,grade))

while True :
    num=int(input('정수를 입력하시오(0은 종료) : '))
    if not num : 
        break
    if num < 0 :
        print('양의 정수로 입력하시오 \n')
        continue
    count = 0
    for i in range(1,num+1) :
        if num % 1 == 0 :
            print('{0:5}'.format(i),end=' ')
            count += 1
print()
print('{0}의 약수의 개수 {1}개입니다.\n'.format(num,count))
