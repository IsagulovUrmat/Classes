# row = int(input())
#
# lst_str = []
# i = 0
# while i < row:
#     string = input()
#     lst_str.append(string)
#     i += 1
#
# count = 0
# new_lst = []
# check = 'NO'
# for j in lst_str:
#     if 'OO' not in j:
#         new_lst.append(j)
#     elif count == 1:
#         new_lst.append(j)
#         continue
#     else:
#         check = 'YES'
#         print(check)
#         count += 1
#         j = j.replace('OO', '++',1)
#         new_lst.append(j)
#
# if check == 'NO':
#     print(check)
# else:
#     for k in new_lst:
#         print(k)

import random


class Student:

    def __init__(self,name,age,surname,group):
        self.name = name
        self.surname = surname
        self.age = age
        self.group = group
        self.points = []
        self.grade = 1
        self.avg = 0

    def marks(self,point):
        if 0 < point < 100:
            self.points.append(point)

    def average(self):
        averag = sum(self.points) / 100
        self.avg = averag







student1 = Student(name='Asan',age='45',surname='Kulikov',group='IB1-17')




i = 0
while i < 100:
    x = random.randint(20,100)
    student1.marks(x)
    i = i + 1

student1.average()

print(student1.name,student1.points,student1.avg)


