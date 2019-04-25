class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0

    """
        the attributes are encapsulated but they are not hidden
        getters a setters is not good practice in python (try not to use them)
        Chances are you don't need those but you can create if they are completely necessary
    """

    def _set_level(self, level):
        if level > 0:
            delta = level - self._level
            self.score += (delta * 1000)
            self._level = level
        else:
            print('Level Cannot be lower than 1')

    def _get_level(self):
        return self._level

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print('lives cannot be negative')
            self._lives = 0

    # Alternative getter syntax
    @property
    def score(self):
        return self._score

    # Alternative setter syntax
    @score.setter
    def score(self, score):
        self._score = score

    # If we don't add a method to use for the setter the attribute becomes read only!
    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score: {0.score}".format(self)
