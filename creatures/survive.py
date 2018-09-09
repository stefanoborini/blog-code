import random

normal = 500
mutated = 1

normal_survive_prob = 0.90
mutated_survive_prob = 0.91


for generation in xrange(1,1000):
    normal -= int(normal * (1-normal_survive_prob))
    mutated -= int(mutated*(1-mutated_survive_prob))

    normal *= 2
    mutated *= 2

    total = normal + mutated 
    print "Generation %d -- normal : %d %%  mutated : %d %% " % (generation, 100*normal/total, 100*mutated/total)


