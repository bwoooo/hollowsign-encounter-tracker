import random

dice = [4, 6, 8, 10, 12, 20, 100]

for die in dice:
    roll = random.randint(1, die)
    print(f"Rolled a d{die}: {roll}")