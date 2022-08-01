import time
from TWP2.MyClass  import Army
from TWP2.MyClass  import Tank

#tank_ussr = Army('Полк Рокоссовский', 200, 100)
#tank_hitler = Army('Армия Гота', 200, 100)
#tank_outher = Army('Третья сторона', 200, 100)


#tank_ussr.get_shot(tank_hitler)
#tank_ussr.get_shot(tank_hitler)

#time.sleep(2)

#tank_ussr.get_shot(tank_outher)
#tank_ussr.get_shot(tank_outher)

#time.sleep(2)

tank1 = Tank('Т34', 250, 100)
tank2 = Tank('Т56', 500, 150)

tank1.get_shot(tank2)
tank2.get_defend()
tank1.get_shot(tank2)

print('конец')