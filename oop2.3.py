# class List:
#     name = 'default'
#     contact = 'default'
#     adress = 'default'
#     def set(self, name,contact,adress):
#         self.name = name
#         self.contact = contact
#         self.adress = adress
# Turat = List()
# Turat.set('Turat','564','Sovetsk')
# Kirill = List()
# Kirill.set('Kirill','43','9 mkr')
# Taalai = List()
# Taalai.set('Taalai','54','5 mkr')
# Aito = List()
# Aito.set('Aito','3','Alamedin')
# class ContactList(list):
#     name = 'default'
#     def search_by_name(self, name):
#         self.name = 1
# all_contact = ['Turat','Kirill','Taalai','Aito']
# all_contact = ContactList()
# all_contact.search_by_name(1)
# for i in range(0,5):
#     all_contact.name = str(input('name:'))
#     if all_contact.name == 'Turat':
#         print(Turat.name,Turat.contact,Turat.adress)
#     elif all_contact.name == 'Kirill':
#         print(Kirill.name,Kirill.contact,Kirill.adress)
#     elif all_contact.name == 'Taalai':
#         print(Taalai.name,Taalai.contact,Taalai.adress)
#     elif all_contact.name == 'Aito':
#         print(Aito.name,Aito.contact,Aito.adress)
#     else:
#         print('Такого контакта нет')
class List:
    def __init__(self, name, address, contact):
        self.name = name
        self.contact = contact
        self.address = address
Taalai = List('Taalai', 222, 'мкр Джал')
Umut = List('Umka', 111, '10 мкр')
Aito = List('Aito', 333, '3 мкр')
Kirill = List('Kirill', 444, '4 мкр')
Turat = List('Turatbek', 555, '5 мкр')
all = List(1,2,3)
for i in range(0,6):
    all.name=input('name: ')
    if all.name == 'Aito':
        print(Aito.name, Aito.contact, Aito.address)
    if all.name == 'Taalai':
        print(Taalai.name, Taalai.contact, Taalai.address)
    if all.name == 'Umut':
        print(Umut.name, Umut.contact, Umut.address)
    if all.name == 'Kirill':
        print(Kirill.name, Kirill.contact, Kirill.address)
    if all.name == 'Turat':
        print(Turat.name, Turat.contact, Turat.address)
    else:
        print('Такого контакта нету в списке!')