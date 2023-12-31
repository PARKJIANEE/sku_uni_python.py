# # 튜플 
# T1 = ()
# print('T1=',T1)
# T2_i = (1)
# print('T2_i=', T2_i)
# T2 = (1,)
# print('T2=', T2)
# print('type(T2)=', type(T2))
# print('type(T2_i)=', type(T2_i))
# T3 = (1,2,3)
# print('T3=', T3)
# T4 = 4,5,6
# print('T4=', T4)
# T5 = ('a','b', ('ab','cd'))
# print('T5=', T5)
# T6 = T3 + T4
# print('T6=', T6)

# # 튜플은 요소 삭제 불가
# del T3[0] # 튜플은 del 지원 하지 않음
# T3[0] = 11  # 튜플에서 지원 하지 않음

# # 튜플과 리스트의 상호변환
# tuple1 = (1,2,3,4)
# list1 = list(tuple1)
# list1.append(5)
# print('tuple1=',tuple1)
# print('list1=',list1)
# tuple1 = tuple(list1)
# print('tuple1=',tuple1)

# # 튜플과 리스트를 이용한 여러개의 변수를 한 번에 생성
# a,b,c = [1,2,3]
# a1,b1,c1 = (11,12,13)
# print('a=',a)
# print('b=',b)
# print('c=',c)
# print('a1=',a1)
# print('b1=',b1)
# print('c1=',c1)

# # count
# print('# count #')
# a = (1,2,3,2,4,2,3,4,2)
# print('a=',a)
# print('a.count(2)=',a.count(2))
# print()

# # index
# print('# index #')
# a = (1,4,3,2)
# b = ('s','t','r') 
# print('a=',a)
# print('b=',b)
# print('a.index(4)=',a.index(4))
# print("b.index('r')=",b.index('r'))
# print('a.index(0)=',a.index(0)) # 오류
# print()

# # len
# print('# len #')
# print('a=',a)
# print('len(a)=',len(a))
# # max
# print('max(a)=',max(a))
# # min
# print('min(a)=',min(a))
# # sum
# print('sum(a)=',sum(a))

# # 튜플의 + 연산
# T1 = (2,5,7)
# T2 = (3,5,9)
# T3 = T1 + T2
# print(T3)
# T3 = T2 + T1
# print(T3)
# T3 += (11,13)
# print(T3)
# # 튜플의 * 연산
# T1 = (2,5,7)
# print(T1)
# print(T1*2)
# # 튜플의 비교 연산 # True | False
# T1 = (2,5,7)
# T2 = (2,5,6)
# print(T1 == T2)
# print(T1 < T2)
# print(T1 > T2)

# # 딕셔너리
# print('# 딕셔너리 #')
# dic1 = {}
# print('dic1=',dic1)
# dic2 = dict()
# print('dic2=',dic2)
# dic1 = {'name':'홍길동', 'phone':'010-1234-5678', 'birth':'03/01'}
# print('dic1=',dic1)
# dic2 = {'점수':[99,85,90]}
# print('dic2=',dic2)
# dic1['major']='컴퓨터공학'
# print('dci1=',dic1)
# dic1['birth']='05/01'
# print('dic1=',dic1)
# print("dic1['name']=",dic1['name'])
# print("dic1['major']=",dic1['major'])

# 딕셔러니 함수와 메소드

# # del
# print('# del #')
# dic1 = {'name':'홍길동', 'phone':'010-1234-5678', 'birth':'03/01'}
# print('dic1=',dic1)
# del(dic1['phone']) # dic1의 phone와 phone의 값을 삭제
# print('dic1=',dic1)
# del dic1['name'] # dic1의 name과 name의 값을 삭제
# print('dic1=',dic1)
# print()

# # pop
# print('# pop #')
# dic1 = {'name':'홍길동', 'phone':'010-1234-5678', 'birth':'03/01'}
# print('dic1=',dic1)
# print("dic1.pop('name')=",dic1.pop('name'))
# print('dic1=',dic1)
# print()

# # popitem
# print('# popitem #')
# dic1 = {'name':'홍길동', 'phone':'010-1234-5678', 'birth':'03/01'}
# print('dic1=',dic1)
# print("dic1.popitem()=",dic1.popitem())
# print("dic1.popitem()=",dic1.popitem())
# print('dic1=',dic1)
# print()

# # keys
# print('# keys #')
# dic1 = {'name':'홍길동', 'phone':'010-1234-5678', 'birth':'03/01'}
# print('dic1.keys()=',dic1.keys())
# print()

# #values
# print('# values #')
# print('dic1.values()=',dic1.values())
# print()

# #items
# print('# items #')
# print('dic1.items=',dic1.items())
# print()

# # len
# print('# len #')
# dic1 = {'name':'홍길동', 'phone':'010-1234-5678', 'birth':'03/01'}
# print('len(dic1)=',len(dic1)) # 딕셔너리 키의 개수
# print()

# # clear
# print('# clear #')
# dic1 = {'name':'홍길동', 'phone':'010-1234-5678', 'birth':'03/01'}
# dic1.clear()
# print('dic1.clear=',dic1) # 딕셔너리 모든 요소 삭제
# print('len(dic1)=',len(dic1))
# print()

# # get
# print('# get #')
# dic1 = {'name':'홍길동', 'phone':'010-1234-5678', 'birth':'03/01', 'major':'컴퓨터공학과'}
# print("dic1.get('major')=",dic1.get('major'))
# print("dic1['major']=",dic1['major'])
# print("dic1.get('grade')=",dic1.get('grade'))
# print("dic1['grade]=",dic1['grade'])
# print()

# # update
# print('# update #')
# dic1 = {'name':'홍길동', 'phone':'010-1234-5678', 'birth':'03/01'}
# print('dic1=',dic1)
# dic1 = {'name':'김철수', 'phone':'010-1234-5678', 'birth':'03/01', 'grade':'1', 'address':'Seoul'}
# print('업데이트된 dic1=',dic1)
# dic1.update(name = '김영희', birth = '12/25', grade = '4')
# print('업데이트된 dic1=',dic1)
# print()

# # pretty print, pprint()
# from pprint import pprint as pp
# pp(dic1)

# # 집합
# # 집합은 값만 모아 놓은 딕셔너리의 특수한 형태로 중복을 허용하지 않고 순서 없다는 특징
# print('# 집합 #')
# set1 = {1,2,3,4,2,3,4,5,3,4,5,7,7,7,7,7}
# print('set1=',set1)
# list1=['국어','영어','수학','영어','국어']
# print('list1=',list1)
# print('set(list1)=',set(list1))
# # print(set1[0])
# print()

# # add
# print('# add #')
# # set1.add(6)
# set1 = {1,2,3,4,2,3,4,5,3,4,5,7,7,7,7,7}
# print('set1=',set1.add(6))
# print('set1=',set1)
# print()

# # update
# print('# update #')
# set1 = {1,2,3,4,2,3,4,5,3,4,5,7,7,7,7,7}
# set1.update([9,10])
# print('set1=',set1)
# print()

# # remove
# print('# remove #')
# set1 = {1,2,3,4,2,3,4,5,3,4,5,7,7,7,7,7}
# print('set1=',set1)
# set1.remove(7) # 집합 set1에서 원소 7을 삭제
# print('set1=',set1)
# set1.remove(7) # 집합 set1에 삭제하려는 원소 7이 없으면 오류
# print('set1=',set1)
# print()

# # discard
# print('# discard #')
# set1 = {1,2,3,4,2,3,4,5,3,4,5,7,7,7,7,7}
# set1.discard(7) # 집합 set1에서 원소 7을 삭제
# print('set1=',set1)
# print()

# # clear
# print('# clear #')
# set1 = {1,2,3,4,2,3,4,5,3,4,5,7,7,7,7,7}
# set1.clear()
# print('set1=',set1)
# print('set1=',set1.clear())
# print()

# # in
# print('# in #')
# set1 = {1,2,3,4,2,3,4,5,3,4,5,7,7,7,7,7}
# print('5 in set1 = ',5 in set1)
# print('11 in set1 = ',11 in set1)
# print()

# # set
# print('# set #')
# set1 = {1,2,3,4,2,3,4,5,3,4,5,7,7,7,7,7}
# set1 = set('python world') # 문자열을 집합 set1으로
# print('set1=',set1)
# print()

# # range
# print('# range #')
# set1 = {1,2,3,4,2,3,4,5,3,4,5,7,7,7,7,7}
# set1 = set(range(10)) # 연속적인 숫자로 집합 set1을
# print('set1=',set1)
# print()

# # 집합의 연산자 - (합집합 : |, 교집합 : &, 차집합 : -, XOR : ^)
# print('<집합의 연산자>')
# set1 = {0,1,2,3,4,5}
# set2 = {4,5,7,8,2,1}
# print('# 합집합 #')
# print('set1=',set1)
# print('set2=',set2)
# print('set1 | set2 = ',set1 | set2)
# print('set.union(set1,set2) = ',set.union(set1,set2))
# print('\n# 교집합 #')
# print('set1 & set2 = ',set1 & set2)
# print('set.intersection(set1,set2) = ',set.intersection(set1,set2))
# print('\n# 차집합 #')
# print('set1 - set2 = ', set1 - set2)
# print('set.difference(set1,set2) = ',set.difference(set1,set2))
# print('set2 - set1 = ', set2 - set1)
# print('set.difference(set2,set1) = ',set.difference(set2,set1))
# print('\n# XOR연산 #')
# print('set1 ^ set2 = ',set1 ^ set2)
# print('set.symmetric_difference(set1,set2) = ',set.symmetric_difference(set1,set2))
# print()
