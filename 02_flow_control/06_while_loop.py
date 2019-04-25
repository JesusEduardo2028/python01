import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}".format(highest))
guess = 0
while guess != highest:
    guess = int(input())

    if guess != answer:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")

    else:
        print("Congrats!, You got it!")
        break
