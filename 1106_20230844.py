
def print_10times_star():
    print('*'*10)

print_10times_star()


def plus(v1, v2):
    result = 0
    result = v1+v2
    return result

hap = plus(100, 200)
print(hap)



def plus(v1, v2):
    """이 함수는  v1과 v2를 더한 뒤 결과를 반환하는 함수입니다."""
    result = 0
    result = v1+v2
    return result

hap = plus(100, 200)
print(hap)
print(plus.__doc__)


def add_multi(n1, n2):
    return n1+n2, n1*n2

result = add_multi(5, 10)
print(result)       # 반환값이 여러개인 경우 반환값을 튜플로 값을 반환한다


def two_times(n):
    return print(n*2)

two_times(5)
two_times('abc')

two_times([1, 2, 3])
two_times((1, 2, 3))


def add_print(a, b):
    print("%d, %d의 합은 %d입니다." %(a, b, a+b))

add_print(1, 9)
hap = add_print(3, 4)   
print(hap)      # 반환값이 없기 때문에, hap이라는 변수를 출력하면 반환값이 없기 때문에 hap의 변수안에는 None이라는 값이 출력된다



def hi():
    return "Hi 파이썬 프로그래밍"

aha = hi()
print(aha)



def hi_2():
    print('Hi파이썬 프로그래밍')

hi_2()



def student_info(name, phone, id_no='비공개'):
    print('이름 : ', name)
    print('휴대폰 : ', phone)
    print('주민번호 : ', id_no)
    print()

student_info('김철수', '010-1234-5678', '11111111-29292929') 
student_info('김철수', '010-1234-5678')                     # 함수의 id_no의 기본값을 비공개로 설정해두었기 때문에 비공개로 출력이 된다. 


def add_m(*args):
    result = 0
    for i in args:
        result = result + i
    return result

r1 = add_m(1, 2, 3)
print('r1 = ', r1)

r2 = add_m(1, 2, 3, 4)
print('r2 = ', r2)

r3 = add_m(1, 2, 3, 4, 5, 6)
print('r3 = ', r3)


def value_times(times, *values):
    # 가변 매개변수의 자료형을 사용할시에 *을 사용한 가변 매개변수의 경우 Tuple형태로 자료형이 저장된다.
    for value in values:
        print(times * value)

value_times(3, 1, 2, 3, 4, 5)


def f_a():
    num = 20
    print('f_a()의 num값 %d' %num)
    # 지역변수의 num을 사용하였다.

def f_b():
    print('f_b()의 num값 %d' %num)
    # 전역변수의 num을 사용하였다

num=10
f_a()
f_b()



def f_a():
    global num     # 지역 안에서 전역변수 사용하기
    num = 20
    print('f_a()의 num값 %d' %num)

num=10
f_a()
print('전역변수 num값  %d' %num)


def calc(v1, v2, op):
    result = 0
    if op == '+':
        result = v1+v2
    elif op == '-':
        result = v1-v2
    elif op == '*':
        result = v1*v2
    elif op == '/':
        if v2 == 0:
            return 'error'
        else:
            result = v1/v2
    elif op == '**':
        result = v1 ** v2
    return result
    
res, var1, var2, oper = 0, 0, 0, ''
while True:
    oper = input('연산자를 입력하세요(+, -, *, /, **, 종료 : q)')
    if oper == 'q':
        print("프로그램을 종료합니다.")
        break
    var1 = int(input('첫 번째 수를 입력하세요 : '))
    var2 = int(input('첫 번째 수를 입력하세요 : '))
    res = calc(var1, var2, oper)
    if res == 'error':
        print('0으로 나누면 안되용~~')
    else:
        print('##계산기 : ',var1, '과 ', var2, '의 ', oper,' 의 결과는 ', res, '입니다.')
    print('계산된 값은 ', res, '입니다.')



def add(n, m):
    return n+m

print('add함수 : ', add(2, 5))
print('lambda함수', (lambda n, m : n+m)(2, 5))



product1 = 1
lis = [1, 2, 3, 4]
for num in lis:
    product1 = product1 * num
print('product1 = ', product1)

# reduce()를 사용하는 경우 처리하기
from functools import reduce
product2 = reduce((lambda x, y : x*y), [1, 2, 3, 4])
print('product2 = ', product2)

 

def cube(y):
    return y * y * y

g = lambda x: x * x * x
print('print(g(7)) = ', g(7))
print('print(cube(5))', cube(5))



li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
print('li = ', li)
final_list_filter = list(filter(lambda x : (x%2 !=0), li))
print('print(final_list_filter) = ', final_list_filter)


final_list_map = list(map(lambda x: x*2, li))
print('print(final_list_map) = ', final_list_map)



a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a_lambda = list(map(lambda x : str(x) if x % 2 == 0 else x, a))
print(f'a = {a}')
print('a_lambda = ', a_lambda)



b_lambda = list(map(lambda x: str(x) if x ==1 else float(x) if x==2 else x+10, a))
print('b_lambda = ', b_lambda)


def f(x):
    if x == 1:
        return str(x)
    elif x == 2:
        return float(x)
    else:
        return x+10
    
c_lambda = list(map(f, a))
print('c_lambda', c_lambda)
