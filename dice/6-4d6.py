import sys
import random

count = {}
for i in xrange(1,1000000):
    collection = []
    for j in xrange(0,6):
        extraction = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6) ]
        #print extraction
        collection.append( sum( sorted( extraction )[1:] ) )
    #print collection 
    bonuses = map(lambda x: (x-10)/2, collection)
    #print bonuses
    total_bonus = sum(bonuses)
    #print total_bonus

    if total_bonus < 3:
        #print "too low, excluded"
        continue
    
    if not count.has_key(total_bonus):
        count[total_bonus]=0
    count[total_bonus] += 1

total_extractions = sum(count.values())
for bonus,occurrences in sorted(count.items()):
    print bonus,occurrences/float(total_extractions)

