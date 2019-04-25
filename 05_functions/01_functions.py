def python_food(text):
    print("spam and eggs and {}".format(text))


python_food("Other things")


# multiple arguments functions

def python_food2(*args):
    for arg in args:
        print(arg)


python_food2("first", "second", "third")

# default values


def python_food3(*args, sep=" "):
    text = ''
    for arg in args:
        text += arg + sep
    print(text)

python_food3("first", "second", "third")


