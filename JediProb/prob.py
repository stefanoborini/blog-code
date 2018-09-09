import sys
import random

def isCaught(no_of_jedis):
    for i in xrange(no_of_jedis):
        caught = (random.randint(1,10) == 1)
        if caught:
            return True
    return False

no_of_jedis=int(sys.argv[1])

no_one_caught = 0
at_least_one_caught = 0
for n in xrange(100000):
    if isCaught(no_of_jedis):
        at_least_one_caught += 1
    else:
        no_one_caught += 1


print no_of_jedis, no_one_caught/1000.0, at_least_one_caught/1000.0


