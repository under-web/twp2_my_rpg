import random
import time
from Person import Person


def battle_activate(hero, enemy):
    '''
    Логика боя
    :param hero:
    :param enemy:
    :return:
    '''
    print(f'Появился {enemy.name} Он перед вами!!! Что делать?')
    print('1 - атака')
    print('2 - убежать')
    action = int(input())

    if action == 1:
        time.sleep(3)
    elif action == 2:
        print('Убегаем')
        return None

    while True:
        enemy.get_attack(hero)  # гоблин атакует героя
        hero.get_attack(enemy)  # атакуем гоблина
        time.sleep(2)

        if (enemy.get_health() <= 0) or (hero.get_health() <= 0):
            break
        else:
            continue


def trigger_event(hero):
    """
    Функция - генератор случайных событий
    :param hero: обьект с которым происходит событие
    :return:
    """

    if random.randint(1, 100) < 20:  # ивент с гоблином 20 % вероятностью
        time.sleep(5)
        goblin = Person(f'Goblin {str(random.randint(1, 100))}', 30, 4, 8)  # создаем обьект гоблин

        battle_activate(hero, goblin)

    if random.randint(1, 100) < 10:  # ивент с великаном 10 % вероятность
        time.sleep(5)
        bigman = Person(f'Bigman {str(random.randint(1, 100))}', 40, 9, 18)

        battle_activate(hero, bigman)
