import math
import random


size = 20
for i in range(size):
    angle = random.uniform(0, 2 * math.pi)
    print(math.sin(angle))
