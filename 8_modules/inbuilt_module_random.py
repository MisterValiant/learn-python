# Using built-in modules

import random

for i in range(3):
    print(random.random())

for i in range(3):
    print(random.randint(10,20))

print('--Team Members--')

members=['John', 'Mary','Mosh','Sarv']
leader=random.choice(members)
print(leader)