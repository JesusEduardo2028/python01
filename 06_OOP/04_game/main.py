from player import Player
from enemy import Enemy, Troll
from vampire import Vampire
from vampire_king import VampireKing

# player is how the file is named

tim = Player('Tim')
random_monster = Enemy('Basic Enemy', 12, 1)

"""
    Getters and Setters in python follow the same principle like in java or c sharp but syntax stays the same after 
    they are defined
"""

print("*** GAME START ***")

pug = Troll('Pug')
print("Ugly Troll - {}".format(pug))

ug = Troll('Ug')
print("Another Troll - {}".format(ug))

urg = Troll('Urg')
print(urg)

pug.grunt()
ug.grunt()
urg.grunt()

drakula = Vampire('drakula')
print(drakula)

pug.take_damage(2)
print(pug)

drakula.take_damage(2)
print(drakula)

while drakula._alive:
    drakula.take_damage(1)
    #print(drakula)

super_draku = VampireKing('KING D.')
print(super_draku)
while super_draku._alive:
    super_draku.take_damage(49)
