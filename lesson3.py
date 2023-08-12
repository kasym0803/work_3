# инкапсуляция
# 1 капсула
# 2 уровни защиты
# 3 публичный,приватный,скрытый

class Bank:

    
    def __init__(self, name, age, money, password):
        self.__name = name
        self.__age = age
        self.__money = money
        self.__passw = password

    @property
    def name(self):
        return self.__name
    
    @property
    def age(self):
        return  self.__age
    
    @property
    def money(self):
        return self.__money

    
    def pname(self):
        print(f'name:{self.__name}\nage:{self.__age}\nmoney:{self.__money}\npassword:{self.__passw}')

    
    def __ppas(self):
        print(self.__passw)


    def pasww(self):
        self.__ppas()

beka = Bank('бека', 20, 0, '12345678987543')

beka.__money = 123456789
print(beka.__money)

beka.pname()

beka.__passw = '0'

print(beka.__passw)
beka.pasww()

