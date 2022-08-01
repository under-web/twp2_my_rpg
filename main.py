import time
from events import trigger_event
from Person import Person



def main():
    hero = Person('Harvy', 100, 10, 20)  # создаем объект герой
    while True:
        hero.get_move()  # герой идет
        time.sleep(2)
        trigger_event(hero)  # что то происходит с героем
        if hero.get_health() <= 0:
            break
    print("[-----------------------------]")
    print("[----------GAME OVER----------]")
    print("[-----------------------------]")

if __name__ == '__main__':
    main()
