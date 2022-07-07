import random
decision = input("You want to roll the dice Y/N")
if  decision=='y'or decision=='Y':
    print(random.randint(1,6))