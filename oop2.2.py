class Car:
    make = 'default'
    model = 'default'
    year = 1
    fuel = 70
    def drive(self, make, model, year, fuel):
        self.make = input('Country:')
        self.model = input('Model:')
        self.year = int(input('Date:'))
        self.fuel = int(input('Petrol:'))
car = Car()
car.drive(1,2,3,4)
print('Страна:',car.make,'\nмарка:',car.model,'\nГод выпуска:',car.year,'\nБензин в баке:',car.fuel)



class Add(Car):
    odometer = 0
    def __dictance(self, odometer):
        self.odometer = car.fuel*10
a = Add()
a._Add__dictance(1)
print('на', a.odometer,' км хватает бензина')
class Subtrack(Car):
    fuel = 70
    def __fuel(self,fuel):
        self.fuel = fuel


v = Subtrack()
v._Subtrack__fuel(int(Car.fuel - int(input('dictance:'))*10))
print('осталось',v.fuel,'литр бензина')
if v.fuel > 0:
    print("Let's drive")
else:
    print("Need more fuel, please, fill more")
        
