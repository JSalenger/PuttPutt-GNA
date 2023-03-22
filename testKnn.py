from random import random
from V import V
import time

class score:
    def __init__(self) -> None:
        self.v = V(random() * 5, random() * 5, 0)
        self.id = 0
        self.distances = {}

l = [score() for _ in range(100)]

sTime = time.time()

for k, v in enumerate(l):
    v.id = k

for j, v in enumerate(l):
    for i in l[j+1:]:
        # compute distances in remaining members
        dist = v.v - i.v
        if v.id < i.id:
            name = str(v.id) + str(i.id)
            v.distances[name] = dist
        else:
            name = str(i.id) + str(v.id)
            v.distances[name] = dist
        
    v.distances = {k: v for k, v in sorted(v.distances.items(), key=lambda item: item[1])}

print(l[0].distances)

print("running time: " + str(time.time() - sTime))