# class Human():
#
#     def __init__(self,name,age):
#         self.human_name = name
#         self.age = age
#
#     def __str__(self):
#         return self.human_name
#
#     def happy_bday(self):
#         self.age = self.age +1
#
#
# human2 = Human('Maksim', 7)
# human2.happy_bday() #добавляет +1 к self.age

# class Car:
#
#     def __init__(self,name,model,price,speed):
#         self.name = name
#         self.model = model
#         self.price = price
#         self.state = 100
#         self.fuel = 100
#         self.run = 0
#         self.color = 'orange'
#         self.no2 = False
#         self.broken = False
#         self.speed = speed
#
#
#     def move(self,distance):
#         if distance > 0:
#             result = 20/100
#             result = distance * result
#             self.fuel -= result
#             self.run += distance
#
#     def broke(self,item):
#         if item == 'stolb':
#             self.state = self.state - 20
#             self.price -= 10000
#         elif item == 'car':
#             self.state = self.state - 40
#             self.price -= 20000
#         elif item == 'human':
#             self.state = self.state - 10
#
#     def check_broken(self):
#         if self.state < 50:
#             self.broken = True
#
#     def build(self):
#         self.no2 = True
#         self.speed += 30
#         self.price += 15000
#
#
# car1 = Car('tesla','XS',90000,390)
# car1.broke('stolb')
# car1.broke('stolb')
# car1.broke('stolb')
# car1.check_broken()
# car1.build()
# print(car1.broken,car1.state,car1.price,car1.speed)


# class Planet:
#
#     def __init__(self,name,position,size):
#         self.name = name
#         self.position = position
#         self.size = size
#         self.humanity = False
#         self.monsters = True
#         self.water = False
#         self.oxygen = False
#         self.sun = True #Вращается ли вокруг солнца какого нибудь
#         self.temp = -273
#         self.gasoline = True
#
#     def monster_check(self):
#         if self.humanity == False:
#             self.monsters == True
#         else:
#             self.monsters == False
#
#     def gas_check(self):
#         if self.size > 500:
#             self.gasoline = True
#         else:
#             self.gasoline = False
#
#     def water_check(self):
#         if self.water == True:
#             self.humanity = True
#         else:
#             self.humanity = False
#
#     def position_check(self):
#         if self.position == 'Близко к солнцу':
#             self.temp = self.temp + 200
#             self.humanity = False
#         elif self.position == 'Далеко от солнца':
#             self.temp = self.temp - 200
#             self.humanity = False
#         else:
#             self.temp = 89
#             self.humanity = True
#
#
#     def temp_check(self):
#         if self.humanity == True:
#             self.temp = 89
#
#
#     def description(self):
#         print(f'Имя: {self.name}, местонахождение: {self.position}, размер: {self.size}, человечество: {self.humanity}, '
#               f'монстры: {self.monsters}, вода: {self.water}, кислород: {self.oxygen}, вокруг солнца: {self.sun}, температура: {self.temp}, '
#               f'газы: {self.gasoline}')
#
# planet1 = Planet('Pluton','Близко к солнцу',400)
# planet1.temp_check()
# planet1.monster_check()
# planet1.gas_check()
# planet1.position_check()
# planet1.temp_check()
# planet1.temp_check()
# planet1.description()

# class Person:
#
#     def __init__(self, name, race):
#         self.name = name
#         self.race = race
#         self.stamina = 100
#         self.agility = 100
#         self.strenght = 100
#         self.health = 100
#         self.intellegence = 100
#         self.level = 1
#         self.armor = 20
#         self.speed = 20
#         self.damage = 40
#         self.expirience = 0
#
#
#     def lvlup(self, exp):
#         exp_list = [20, 30, 40, 100, 500, 1000]
#         i = 0
#         for i in range(len(exp_list)):
#             i = self.level - 1
#             if exp_list[i] <= exp:
#                 print(exp)
#                 exp -= exp_list[i]
#
#                 self.level += 1
#                 self.stamina += 13
#                 self.agility += 13
#                 self.strenght += 13
#                 self.intellegence += 13
#                 self.expirience = exp
#
#
#     def equip(self, item):
#         items_list = ['sword', 'boots', 'heavy_armor', 'light_armor', 'bow', 'staff', 'potion']
#
#         if item == 'sword':
#             self.damage += 50
#             self.strenght += 40
#         elif item == 'boots':
#             self.speed += 10
#         elif item == 'heavy_armor':
#             self.armor += 50
#             self.stamina -= 50
#             self.speed -= 20
#             self.health += 500
#             self.strenght += 50
#         elif item == 'light_armor':
#             self.armor += 10
#             self.stamina += 50
#             self.health += 200
#             self.strenght += 20
#             self.agility += 10
#
#         elif item == 'bow':
#             self.agility += 40
#             self.damage += 50
#
#         elif item == 'staff':
#             self.intellegence += 100
#             self.health += 70
#
#         elif item == 'potion':
#             self.stamina += 2
#             self.agility += 2
#             self.strenght += 2
#             self.health += 2
#             self.intellegence += 2
#             self.armor += 2
#             self.speed += 2
#             self.damage += 2
#
#
# person1 = Person(name='abrakadabra', race='human')
# person1.lvlup(2000)
# print(person1.name, person1.race, person1.speed, person1.level, person1.agility,person1.strenght,person1.stamina,person1.damage,
#       person1.health,person1.intellegence,person1.armor
#       )
# person1.equip('potion')


