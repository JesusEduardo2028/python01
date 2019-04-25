# In python3 all classes inherit from object by default so this is exacty as class Enemy
class Enemy(object):

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self._name = name
        self._hit_points = hit_points
        self._lives = lives
        self._alive = True

    def take_damage(self, damage):
        remaining_points = self._hit_points - damage
        if remaining_points >= 0:
            self._hit_points = remaining_points
            print("{0._name} took {1} points damage and have left {0._hit_points} points".format(self, damage))
        else:
            self._hit_points = 0
            self._lives -= 1
            if self._lives > 0:
                print("{0._name} lost a life".format(self))
            else:
                self._alive = False
                print("{0._name} is dead".format(self))

    def __str__(self):
        return "Name: {0._name}, Lives: {0._lives}, Hit points: {0._hit_points}".format(self)


class Troll(Enemy):

    def __init__(self, name):
        # Python2 way: using superclass init method
        # Enemy.__init__(self, name=name, lives=1, hit_points=23)
        super(Troll, self).__init__(name,1, 23)

    def grunt(self):
        print("Me {0._name}. {0._name} stomp you!".format(self))

