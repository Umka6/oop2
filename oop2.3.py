class List:
    name = 'default'
    contact = 'default'
    adress = 'default'
    def set(self, name,contact,adress):
        self.name = name
        self.contact = contact
        self.adress = adress
Turat = List()
Turat.set('Turat','564','Sovetsk')
Kirill = List()
Kirill.set('Kirill','43','9 mkr')
Taalai = List()
Taalai.set('Taalai','54','5 mkr')
Aito = List()
Aito.set('Aito','3','Alamedin')
class ContactList(list):
    name = 'default'
    def search_by_name(self, name):
        self.name = 1
all_contact = ['Turat','Kirill','Taalai','Aito']
all_contact = ContactList()
all_contact.search_by_name(1)
for i in range(0,5):
    all_contact.name = str(input('name:'))
    if all_contact.name == 'Turat':
        print(Turat.name,Turat.contact,Turat.adress)
    elif all_contact.name == 'Kirill':
        print(Kirill.name,Kirill.contact,Kirill.adress)
    elif all_contact.name == 'Taalai':
        print(Taalai.name,Taalai.contact,Taalai.adress)
    elif all_contact.name == 'Aito':
        print(Aito.name,Aito.contact,Aito.adress)
    else:
        print('Такого контакта нет')