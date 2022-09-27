# Q1
import random

def create_random():

    rand = []
    for i in range(100):
        rand.append(i + 1)
    rand = random.sample(rand, 100)

    return rand