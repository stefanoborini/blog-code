import copy
import random

MAX_CODE_LEN=100
CODE_LEN_TOLERANCE=5
CODE_LEN_TOL_PROBABILITY = 0.1

MAX_STACK_LEN=10
STACK_LEN_TOLERANCE=2
STACK_LEN_TOL_PROBABILITY = 0.1

STARTING_ENERGY=25 
STARTING_ENERGY_TOLERANCE = 5
STARTING_ENERGY_TOL_PROBABILITY=0.3

DUPLICATE_ENERGY = 40
MUTATION_RATE=0.1




class Enzyme(object):
    opcodes = { \
            "ADD_VAL" : self.__handle_ADD_VAL, \
            "ADD_MEM" : self.__handle_ADD_MEM, \
            "AND_VAL" : self.__handle_AND_VAL, \
            "AND_MEM" : self.__handle_AND_MEM, \
            "BPL"     : self.__handle_BPL, \
            "BMI"     : self.__handle_BMI, \
            "BEQ"     : self.__handle_BEQ, \
            "BNE"     : self.__handle_BNE, \
            "CMP_VAL" : self.__handle_CMP_VAL, \
            "CMP_MEM" : self.__handle_CMP_MEM, \
            "CPX_VAL" : self.__handle_CPX_VAL, \
            "CPX_MEM" : self.__handle_CPX_MEM, \
            "CPY_VAL" : self.__handle_CPY_VAL, \
            "CPY_MEM" : self.__handle_CPY_MEM, \
            "DEC"     : self.__handle_DEC, \
            "DEX"     : self.__handle_DEX, \
            "DEY"     : self.__handle_DEY, \
            "EOR_VAL" : self.__handle_EOR_VAL, \
            "EOR_MEM" : self.__handle_EOR_MEM, \
            "INC"     : self.__handle_INC,
            "INX"     : self.__handle_INX, \
            "INY"     : self.__handle_INX, \
            "JMP"     : self.__handle_JMP, \
            "JSR"     : self.__handle_JSR, \
            "LDA"     : self.__handle_LDA, \
            "LDX"     : self.__handle_LDX, \
            "LDY"     : self.__handle_LDY, \
            "NOP"     : self.__handle_NOP, \
            "ORA_VAL" : self.__handle_ORA_VAL, \
            "ORA_MEM" : self.__handle_ORA_MEM, \
            "PHA"     : self.__handle_PHA, \
            "PLA"     : self.__handle_PLA, \
            "STA"     : self.__handle_STA, \
            "STX"     : self.__handle_STX, \
            "STY"     : self.__handle_STY, \
            "TAX"     : self.__handle_TAX, \
            "TXA"     : self.__handle_TXA, \
            "TAY"     : self.__handle_TAY, \
            "TYA"     : self.__handle_TYA, \
            "RET"     : self.__handle_RET
    def __init__(self):
        self.x = 0
        self.y = 0
        self.a = 0
        self.mem = dict()
        self.stack = list()
        self.code = list()
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
        if gencode == None:
            opnum=random.randint(2,50)
            for i in xrange(0,opnum):
                self.opcode = random.choice(self.opcodes.keys())
                self.code.append((self.opcode, random.randint(-5,5)))
        else:
            self.code = copy.deepcopy(gencode)

class Creature(object):
    def __init__(self,gencode=None):
        self.enzymes = list()
        self.tasks = dict()
        self.energy = STARTING_ENERGY 
        if (random.random() < STARTING_ENERGY_TOL_PROBABILITY):
            self.energy = self.energy + random.randint(-STARTING_ENERGY_TOLERANCE,STARTING_ENERGY_TOLERANCE)
        
    def feed(self,task,input,expected):
        




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
