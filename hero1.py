

class SuperHero:
    people='people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def print(self):
        print(self.name, self.nickname, self.superpower, self.health_points, self.catchphrase)

    def health(self):
        self.health_points *= 2

    def __str__(self):
        return f'nickname :{self.nickname}\nsuperpower :{self.superpower}\nhealth_points :{self.health_points}'
    
    def __len__(self):
        return len(f'{self.catchphrase}')

hero = SuperHero('Питер Паркер.','Человек-паук.', 'Силы паука.', 50 , '. Никто не может выигрывать каждую битву, но ни один человек не должен сдаваться без борьбы.')

hero.print()
print('name:',hero.name)

print("Здоровье до умножения:", hero.health_points)  
hero.health()
print("Здоровье после умножения:", hero.health_points)

print(hero)
print('Длина коронной фразы:',len(hero))

print( )

# ////////////////////////////////:Космичечкий герой:///////////////////////////////////////////
class Space_Hero(SuperHero):
    
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        SuperHero.__init__(self,name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def print(self):
        print(self.name, self.nickname, self.superpower, self.health_points, self.catchphrase, self.damage, self.fly)

    def health(self):
        self.health_points **= 2

    def phrase(self):
        print('Phrase: fly in the True_phrase')
        

hero_1 = Space_Hero('Калларк.','Гладиатор.','Разрушительное дыхание.', 73 ,'. Герой которого почти не вазможно победить.', 21, False)

Space_Hero.print(hero_1)
print(hero_1)

print("Здоровье до поднятие на квадрат:", hero_1.health_points) 
hero_1.health()
print("Здоровье после поднятие на квадрат:", hero_1.health_points) 

hero_1.fly = True
hero_1.print()

hero_1.phrase()
print( )

# /////////////////////////////////:Земляной герой://///////////////////////////////////////////
class Earth_Hero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        SuperHero.__init__(self,name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def print(self):
        print(self.name, self.nickname, self.superpower, self.health_points, self.catchphrase, self.damage, self.fly)

    def health(self):
        self.health_points **= 2

    def phrase(self):
        print('Phrase: fly in the True_phrase')

    def crit(self):
        self.damage **= 2

hero_2 = Earth_Hero('Доктор Стрэндж.','Доктор Стрэндж.','Магия.', 68 ,'. Если я расскажу, что случится, — это не случится.',16, False,)

Earth_Hero.print(hero_2)
print(hero_2)

print("Здоровье до поднятие на квадрат:", hero_2.health_points) 
hero_2.health()
print("Здоровье после поднятие на квадрат:", hero_2.health_points) 

hero_2.fly = True
hero_2.print()

hero_2.phrase()

print("Damage до поднятие  в степень:", hero_2.damage) 
hero_2.crit()
print("Damage после поднятие в степень:", hero_2.damage) 
print( )

# ////////////////////////////////:Новый герой://///////////////////////////////////////////////
class villain(Earth_Hero):
    people = 'monster'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        Earth_Hero.__init__(self,name, nickname, superpower, health_points, catchphrase, damage, fly)

    def gen_x(self):
        return None
    
    def health(self):
        self.health_points **= 2

    def crit(self):
        self.damage **= 2

hero_3 = villain('Сентри.','Часавой.','молекулярное манипулирование.',83,'. может быть побежден только в том случае, если он хочет быть побежденным.', 26 , False)

Earth_Hero.print(hero_3)
print(hero_3)

print("Здоровье до поднятие на квадрат:", hero_3.health_points) 
hero_3.health()
print("Здоровье после поднятие на квадрат:", hero_3.health_points) 

print("Damage до поднятие в степень:", hero_3.damage) 
hero_3.crit()
print("Damage после поднятие в степень:", hero_3.damage)










