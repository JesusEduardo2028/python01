from enemy import Enemy
import random


class Vampire(Enemy):

    def __init__(self, name):
        super(Vampire, self).__init__(name, 12, 1)

    def dodges(self):
        if random.randint(1, 3) == 1:
            print("****** {0._name} dodges attack *******".format(self))
            return True
        else:
            return False

    def take_damage(self, damage):
        if not self.dodges():
            super(Vampire, self).take_damage(damage)
