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

class Car:

    def __init__(self, name,model,price):
        self.mame = name
        self.model = model
        self.price = price
        self.fuel = 100
        self.run = 0
        self.color = 'orange'
        self.no2 = False

    def move(self,distance):
        if distance > 0:

            self.run += distance


car1 = Car('Tesla','XS',90000)
car1.move(240)
print(car1.run)


