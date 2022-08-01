import random


class Person:
    step = 0

    def __init__(self, name, health, min_attack, max_attack):
        self.name = name
        self.health = health
        self.min_attack = min_attack
        self.max_attack = max_attack

    def get_health(self):
        return self.health

    def get_attack(self, enemy):
        real_attack = random.randint(self.min_attack, self.max_attack)
        enemy.health = enemy.health - real_attack
        print(f'{self.name} атакует {enemy.name} наносит урон {real_attack}. '
              f'Теперь здоровье {enemy.name} равно {enemy.health}')

        self.get_health_status() # проверка жив ли обьект
        enemy.get_health_status()

    def get_move(self):
        self.step += 1
        print(f'{self.name} двигается и делает {self.step} шаг(ов)')

    

    def get_health_status(self):
        if self.health <= 0:
            print(f'{self.name} УБИТ!')
            self.__del__() # уничтожает обьект



    def __del__(self):
        pass