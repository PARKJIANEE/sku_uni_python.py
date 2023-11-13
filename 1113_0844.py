# # Chapter 07
# class Student: # 클래스 정의
#     def __init__(self, name): # 행위(method), init(생성자)
#         self.name = name # self(자신)
    
# student1 = Student("홍길동")
# student2 = Student("김철수")
# print("인스턴스 student1의 이름 = ", student1.name)
# print("인스턴스 student2의 이름 = ", student2.name)

# print("인스턴스 student1의 타입 = ",type(student1))
# print("인스턴스 student2의 타입 = ",type(student2))

# student3 = Student("김성결")
# print("인스턴스 student3의 이름 = ", student3.name)
# print("인스턴스 student3의 타입 = ",type(student3))

# class Student:
#     def __init__(self, name, email, phone): 
#         self.name = name 
#         self.email = email
#         self.phone = phone

# student1 = Student ("홍길동", "hong1234@email.net", "010-1234-5678")
# student2 = Student ("김철수", "kim1234@gmail.com", "010-3456-7890")
# print("인스턴스 student1의 이름 = ", student1.name)
# print("인스턴스 student1의 이메일 = ", student1.email)
# print("인스턴스 student1의 전화번호 = ", student1.phone)
# print()
# print("인스턴스 student2의 이름 = ", student2.name)
# print("인스턴스 student2의 이메일 = ", student2.email)
# print("인스턴스 student2의 전화번호 = ", student2.phone)

# class Student:
#     def __init__(self, name, email, phone): 
#         self.name = name 
#         self.email = email
#         self.phone = phone

#     def to_print(self):
#         return "{}\t{}\t{}".format( 
#         self.name,
#         self.email,
#         self.phone)
    
# students = [
#     Student("홍길동", "hong1234@email.net", "010-1234-5678"),
#     Student("김철수", "kim1234@gmail.com", "010-3456-7890"),
#     Student("홍길동", "hong1234@email.net", "010-1234-5678"),
#     Student("김철수", "kim1234@gmail.com", "010-3456-7890")
#     ]
# print("이름", "email", "phone", sep='\t\t')
# print('-' * 50)

# for student in students:
#     print(student.to_print())

# student1 = Student("김성결", "kim1234@email.net", "010-1234-5678")
# print(student1.to_print())
# del students
# print(student1.to_print())

# class Student1:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __eq__(self, other):
#         return self.name == other.name
#     def __ne__(self, other):
#         return self.name != other.name
#     def __gt__(self, other):
#         return self.name > other.name
#     def __ge__(self, other):
#         return self.name >= other.name
#     def __lt__(self, other):
#         return self.name < other.name
#     def __le__(self, other):
#         return self.name <= other.name
    
# student = Student1("김철수", 23)
# student1 = Student1("홍길동", 23)

# print(student == student1)
# print(student != student1)
# print(student > student1)
# print(student >= student1)
# print(student < student1)
# print(student <= student1)

# class Registration:
#     regi_num = 0 # 클래스 변수
#     def __init__(self, name): # 생성자 메소드 
#         self.name = name # 인스턴스 변수
#         Registration.regi_num += 1
#     def __del__(self):
#         Registration.regi_num -= 1

# student1 = Registration("홍길동")
# student2 = Registration("김철수")

# print(student1.name)
# print(student2.name)
# print(Registration.regi_num)
# del student1
# print(f"수강신청철회한 학생이 발생한 이후의 등록학생수: {Registration.regi_num}")

# class UnderSelf:
#     def meth1(self): # self는 클래스로부터 만들어진 인스턴스 그 자체를 의미함
#         print("python 1")
#     def meth2(self):
#         print("pyhton 2")

# s1 = UnderSelf()
# s1.meth1()
# print('id(s1) = ', id(s1))
# s1.meth2()