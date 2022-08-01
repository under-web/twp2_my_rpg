
class Army:
    def __init__(self, name, health, attack):
        self.health = health
        self.attack = attack
        self.name = name

    def get_shot(self, enemy):  # передаем обьект по которому стреляем
        if not enemy.health <= 0:
            print(f'{self.name} атакует {enemy.name}')
            enemy.set_damage(self.attack)

    def set_damage(self, hit):  # внутреннея реализация урона
        if not self.health <= 0:
            self.health = self.health - hit
            #print(f'[Количество {self.name} {self.health} ед.]')
            #print('')
        else:
            del self

    def get_name(self):
        return self.name

    def get_status_health(self):
        return self.health

    def __del__(self):
        print(f'Объект {self.name} уничтожен!')


class Tank(Army):
    def get_defend(self):
       self.health = self.health * 2
       print(f'{self.name} укрепился теперь его здоровье {self.health}')
       return self.health