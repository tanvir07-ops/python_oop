'''
p = {}

p['name'] = 'Tanvir Rifat'
p['email'] = 'tanvir@example.com'

print(p)
'''

class Person:
    def __init__(self,name,email):
        self.__name = name
        self.__email = email

    def log(self):
        print(self.__dict__)

    @property
    def name(self):
        print(self.__name)

    @property
    def email(self):
        print(self.__email)

    @name.setter
    def name(self,name):
        self.__name = name          

    @email.setter
    def email(self,email):
        self.__email = email    

    def __str__(self):
        return f'Name : {self.__name}, Email : {self.__email}'

person= Person('Tanvir Rifat','tanvir@example.com')
person.name = 'Tanvir Hassan Rifat'
person.email = 'Tanvir@gmail.com'

person.log()
print(person)


class Guardian(Person):
    def __init__(self,name,email,fee):
        super().__init__(name,email)
        
        self.__fee = fee

    @property
    def fee(self):
        print(self.__fee)

    @fee.setter
    def fee(self,fee):
        self.__fee = fee


guardian = Guardian('Rabeya Begum','rabeya@example.com',200000)
guardian.log()
print(guardian)






      