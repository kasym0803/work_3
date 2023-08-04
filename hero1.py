

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

        