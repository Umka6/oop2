class House:
    s = 'default'
    t = 'default'
    def abc(self,s,t):
        self.t = input('Enter type:')
        self.s = int(input('Enter the area:'))

class Furniture(House):
    locker = '2'
    table = 'default'
    bed = 'default'
    def furn(self,locker,table,bed):
        self.locker = 2
        self.table = 1.5
        self.bed = 4

a = Furniture()
a.abc(1,2)
a.furn(1,2,3)
print('тип дома',a.t,'площадь дома',a.s,'\nсписок мебели внутри дома: кровать, шкаф,стол')
d =(a.s -(a.locker+a.table+a.bed))
if d > 0:
    print('Осталось',d, 'кв.м свободных мест')
else:
    print('Нет места для мебели')