import random

def unique_surnames(population):
    return len(set(population))

def generation(male_population, female_population):
    new_male_population = []
    new_female_population = []
    for children_surname in map(lambda x: x[0], zip(male_population, female_population)):
        num_of_children = random.choice([0]*4+ [1]*8+ [2]*16+ [3]*8+ [4]*5)
        for i in xrange(num_of_children):
            append_to_population = random.choice( [lambda : new_male_population.append(children_surname), lambda : new_female_population.append(children_surname)])
            append_to_population() 
    return (new_male_population, new_female_population) 

surname_syllabes = [ "ta", "wa", "ka", "ga", "ku", "wu", "gu", "shi", "te", "we", "ke", "ge", "ti", "wi", "ki", "ko", "to", "go", "wo", "ma" ]
male_population = []
female_population = []
for i in xrange(10000):
    name = random.choice(surname_syllabes) +random.choice(surname_syllabes) +random.choice(surname_syllabes) +random.choice(surname_syllabes)
    append_to_random_population = random.choice( [lambda : male_population.append(name), lambda : female_population.append(name)])
    append_to_random_population()

for g in xrange(0,1000):
    print g, len(male_population+female_population), unique_surnames(male_population+female_population)
    if len(male_population+female_population) == 0: break
    male_population, female_population = generation(male_population, female_population)
