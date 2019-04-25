from vampire import Vampire


class VampireKing(Vampire):

    def __init__(self, name):
        super().__init__(name=name)
        self._hit_points = 140

    def take_damage(self, damage):
        damage = damage // 4
        super().take_damage(damage)
