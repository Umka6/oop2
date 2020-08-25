# class Animal:
#     name = 'default'
#     hunger = 6
#     def eat(self,name):
#         self.name = 'def'
# class Cat(Animal):
#     name = 'Cat'
#     m ='mua'
#     def meow(self, m, name):
#         self.name = input('name:')
#         self.m = int(input(('сколько раз муакает:')))
# d = Cat()
# d.meow(1,2)
# if d.m>=5:
#     print('Мяу')
#     for i in range(5, d.m):
#         user = input('Накормите кошку')
# else:
#     print('не маукаять')
#
#
# class Dog(Animal):
#     name = 'Dog'
#     b = 'bark'
#     def bark(self, b, name):
#         self.name = input('name:')
#         self.b = int(input(('сколько раз лает:')))
# c = Dog()
# c.bark(1,2)
# if c.b >= 5:
#     print('Гав')
#     for i in range(5,c.b):
#         user = input('Накормите собаку')
# else:
#     print('не гавкать')

class Animal:
    def __init__(self,name,m,breed):
        self.name = name
        self.m = m
        self.breed = breed

katya = Animal('Katay',6,'sfinks')
if katya.m>=5:
     print('Мяу')
     for i in range(5, katya.m):
         user = input('Накормите кошку:')
else:
     print('не маукаять')
sharik = Animal('Sharik',4,'german')
if sharik.m >= 5:
     print('Гав')
     for i in range(5,sharik.m):
         user = input('Накормите собаку:')
else:
     print('не гавкать')
print(katya.name, katya.m,katya.breed)
print(sharik.name, sharik.m,sharik.breed)
# dog = Dog()
# cat.meow(name=input('Enter the name:'),hunger=int(input('Enter:')))
# cat.eat()
# dog.bar(name=input('Enter the name:'),hunger=int(input('Enter:')))
# dog.eat()
