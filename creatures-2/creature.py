import copy
import random

class Creature(object):
    def __init__(self,gencode=None):
        self.opcodes = { \
                         "INA" : self.__handle_INA, \
                         "INX" : self.__handle_INX, \
                         "LDA" : self.__handle_LDA, \
                         "LDX" : self.__handle_LDX, \
                         "LDY" : self.__handle_LDY, \
                         "ADDY" : self.__handle_ADDY, \
                         "MVY" : self.__handle_MVY, \
                         "BZ" : self.__handle_BZ, \
                         "BNZ" : self.__handle_BNZ, \
                         "RET" : self.__handle_RET}
        self.x = 0
        self.y = 0
        self.a = 0
        self.code=list()
        self.pc = 0
        if gencode == None:
            opnum=random.randint(2,50)
            for i in xrange(0,opnum):
                self.opcode = random.choice(self.opcodes.keys())
                self.code.append((self.opcode, random.randint(-5,5)))
        else:
            self.code = copy.deepcopy(gencode)
    def __handle_INA(self,val):
        self.a = self.a + val
    def __handle_INX(self,val):
        self.x = self.x + val
    def __handle_LDA(self,val):
        self.a = val
    def __handle_LDX(self,val):
        self.x = val
    def __handle_LDY(self,val):
        self.y = val
    def __handle_ADDY(self,val):
        self.a = self.a + self.y
    def __handle_MVY(self,val):
        self.y = self.a
    def __handle_BZ(self,val):
        if self.x == 0:
            self.pc = self.pc+val
    def __handle_BNZ(self,val):
        if self.x != 0:
            self.pc = self.pc+val
    def __handle_RET(self,val):
        self.returned = True
        

    def execute(self,val):
        self.a = val
        self.x = 0
        self.y = 0
        self.pc = 0
        self.returned = False
        counter = 0  
        while True:
            opcode = self.code[self.pc]
            self.opcodes[opcode[0]](opcode[1])
            self.pc = self.pc + 1
            counter = counter + 1
            if counter > 50:
                return self.a
            if self.pc < 0:
                self.pc = 0
            elif self.pc >= len(self.code) or self.returned:
                return self.a
    def mutate(self):
        
        mutations=random.randint(1,5)
        for i in xrange(0,mutations):
            self.opcode = random.choice(self.opcodes.keys())
            v = random.randint(0,len(self.code))
            if (v == len(self.code)):
                continue
            self.code[v] = (self.opcode, random.randint(-5,5))
#            if 4 < mut_type < 8: # insertion
#                self.opcode = random.choice(self.opcodes.keys())
#                self.code.insert(random.randint(1,len(self.code))-1, (self.opcode, random.randint(-5,5)))
##            if mut_type == 9: # remove
#                victim=random.randint(1,len(self.code))-1
#                code = self.code[0:victim]+self.code[victim+1:]
#                self.code = code


class SuperCreature(Creature):
    def __init__(self):
        super(SuperCreature,self).__init__([("LDX",2), ("MVY",0), ("LDA",0), ("ADDY",0), ("INX", -1), ("BNZ", -3), ("LDY",5), ("ADDY", 0), ("RET" , 0) ])

class Environment(object):
    def __init__(self):
        self.creatures=list() 
        for i in xrange(1,1000):
            self.creatures.append(Creature())
        print "1000"
        for i in xrange(1,1000):
            self.creatures.append(Creature())
        print "1000"
        for i in xrange(1,1000):
            self.creatures.append(Creature())
        print "1000"
        for i in xrange(1,1000):
            self.creatures.append(Creature())
        print "1000"
        for i in xrange(1,1000):
            self.creatures.append(Creature())
        print "1000"
        for i in xrange(1,1000):
            self.creatures.append(Creature())



    def generation(self, conditions, tolerance, die):
        nextgen = list()
        for creature in self.creatures:
            score = 0.0
            for cond in conditions:
                score = score + abs(float(creature.execute(cond[0])) - float(cond[1]))
            if (score/float(len(conditions)) < float(tolerance)):
                nextgen.append(creature)

        print "survived : ", len(nextgen)

        if (die == True):
            self.creatures=nextgen
        return len(nextgen)
    def duplicate(self):
        newcreatures=list()
        for c in self.creatures:
            newcreatures.append(Creature(c.code))
        self.creatures.extend(newcreatures)
    def mutate(self):
        for c in self.creatures:
            c.mutate()

    def satisfy(self,constraint):
        generation = 1
        while True:
            print generation
            remaining = e.generation(constraint,100.0/float(generation),False)
            if remaining == 0:
                print "all died.. mutation. Current population : ",len(e.creatures)
                if len(e.creatures) < 2000:
                    e.duplicate()
                e.mutate()
                continue
                
            e.generation(constraint,100.0/float(generation),True)
            if len(e.creatures) < 2000:
                e.duplicate()
            e.mutate()
            generation = generation + 1
            if generation == 50:
                break
            

e=Environment()




e.satisfy([(0,5)])
e.satisfy([(0,5),(2,9)])
e.satisfy([(0,5),(2,9),(4,13)])
e.satisfy([(0,5),(2,9),(4,13),(5,15)])
