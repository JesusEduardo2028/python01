""" When a class contains object from a different class like in this example,
    where a duck has a wing object attribute so it can use the attributes and methods from a wing """


class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print('Weee, this is fun')
        elif self.ratio == 1:
            print('This is hard work, but im flying')
        else:
            print('I think ill just walk')


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)

    def fly(self):
        self._wing.fly()

    def walk(self):
        print('Waddle, waddle, waddle')

    def swim(self):
        print('Come on it, the water is lovely')

    def quack(self):
        print('Quack, quack')


#def test_duck(duck):
#    duck.walk()
#    duck.swim()
#    duck.quack()


class Penguin():

    def walk(self):
        print('Waddle, waddle i waddle too')

    def swim(self):
        print('Come on but its chilly this far south')

    def quack(self):
        print("Are you 'avin' a larf? I'm a penguin")


if __name__ == '__main__':
    donald = Duck()
    donald.fly()


