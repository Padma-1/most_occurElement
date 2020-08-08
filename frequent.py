from random import random

x = [int(random()*5)for i in range (20)]
print(x)#[4, 1, 2, 1, 4, 4, 4, 0, 2, 2, 2, 2, 1, 4, 2, 2, 4, 4, 2, 1]


myset = set(x)
print(set(x))#{0, 1, 2, 4}

highest = None#or put 0
frequent = 0

for item in myset:
    freq =x.count(item)

    if freq > frequent:
        frequent = freq
        highest = item
print(highest)#2
