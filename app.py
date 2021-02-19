#person Class
class Person:
    '''
    This is a simple Class
    '''
    def __init__(self,name,email):
        self.__name = name
        self.__email = email
        pass
    def log(self):
        print(self.__dict__)

    


    @property
    def name(self):
        print(self.__name)
    @name.setter
    def name(self,name):
        self.__name = name


    @property 
    def email(self):
       print(self.__email)
   
    def sendEmail(self,msg):
        print(f'To:{self.email }')
        print(f'Message:{msg}')

    

    def __str__(self):
        return f'Name:{self.__name},Email:{self.__email}'

# Teacher Class
class Teacher(Person):
    
    def __init__(self,name,email,salary,subject):

        super().__init__(name,email)
        self.__salary = salary
        self.__subject = subject
        pass
   
    @property
    def salary(self):
        print(self.__salary)
    @salary.setter
    def salary(self,salary):
        self.__salary = salary 

    @property
    def subject(self):
        print(self.__subject)
    @subject.setter
    def subject(self,subject):
        self.__subject = subject             

  

#Student Class

class Student(Person):
   
    def __init__(self,name,email,fee,subjects):
        super().__init__(name,email)
       
        self.__fee = fee
        self.__subjects = subjects
        pass
   
    


   
    @property
    def fee(self):
        print(self.__fee)
    @fee.setter
    def fee(self,fee):
        self.__fee = fee

    @property
    def subjects(self):
        print(self.__subjects)
    @subjects.setter
    def subjects(self,subjects):
        self.__subjects = subjects             

   

person = Person('Test','test@example.com')
person.log() 
print(person)   

teacher = Teacher('Tanvir Rifat','tr9836859@gmail.com',5000,'Python programming')
teacher.log()

student = Student('Gazi','gazi@gmail.com','50000',['python','Php','Laravel'])
student.log()




