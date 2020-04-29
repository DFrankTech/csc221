# Simulates flipping a coin 1,000 times. Without debugger
import random
heads = 0
for i in range(1, 1001):
    if random.randint(0, 1) == 1:
        heads = heads + 1
    if i == 500:
        print('Halfway done!')
print('Heads came up ' + str(heads) + ' times.')

# The random.randint(0, 1) call ➊ will return 0 half of the time and 1 the other half of the time.
# This can be used to simulate a 50/50 coin flip where 1 represents heads.
