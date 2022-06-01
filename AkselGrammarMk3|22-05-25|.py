

import random
from tkinter import Y

class Noun:
    def __init__(self, count, plural):
        self.count  = count
        self.plural = plural
class Verb:
    def __init__(self, maxargs, minargs, plural, weak):
        self.maxargs = maxargs
        self.minargs = minargs
        self.plural  = plural
        self.weak    = weak
class Modal:
    def __init__(self, finite):
        self.finite = finite
class Determiner:
    def __init__(self, plural):
        self.plural = plural
#some nouns
NounDict             = {}
NounDict ['love']    = (False, True)
NounDict ['sand']    = (False, True)
NounDict ['cup']     = (True, False)
NounDict ['cats']    = (True, True)
NounDict ['bravery'] = (False, True)
NounDict ['oxen']    = (True, True)
for word, properties in NounDict.items():
    word = Noun(*properties)
#some verbs
VerbDict               = {}
VerbDict ['wait']      = (1, 1, True, True)
VerbDict ['waits']     = (1, 1, False, True)
VerbDict ['resonate']  = (2, 1, True, True)
VerbDict ['resonates'] = (2, 1, False, True)
for word, properties in VerbDict.items():
    word = Verb(*properties)
#some modals
ModalDict          = {}
ModalDict ['will'] = (True)
ModalDict ['may']  = (True)
ModalDict ['can']  = (True)
for word, properties in ModalDict.items():
    word = Modal(properties)
#some determiners
DeterminerDict          = {}
DeterminerDict ['a']    = (False)
DeterminerDict ['the']  = (False)
DeterminerDict ['some'] = (True)
DeterminerDict ['an']   = (False)
for word, properties in DeterminerDict.items():
    word = Determiner(properties)

# Lexical Item Names
M    = "modal"
V    = "verb"
P    = "preposition"
N    = "noun"
D    = "determiner"
A    = "adjective"
C    = "complimentizer"
NP   = "noun phrase"
NEG  = "not"
DEG  = "degree"
NAME = "name"
PRON = "pronoun"
POSS = "possessive marker"
NULL = ""
# Phrase Structures
NEGP  = ['NEGbar']
MEASP = ['UNKNOWN']
DEGP  = [['DEGbar', 'AP']]
PP    = [['MEASP', 'Pbar']]
DP    = [['NP', 'POSS'], D]
NP    = ['PRON', 'NAME', 'Nbar', ['DP', 'Nbar'], ['DEGP', 'Nbar'], ['DP', 'DEGP', 'Nbar']]
MP    = [['NP', 'Mbar'], ['Mbar']]
VP    = [[V, 'VP'], ['Vbar']]
AP    = [['Abar']]
CP    = [['Cbar']]
# Prime Structures
NEGbar = [['NEG', 'VP']]
DEGbar = [['DEG', 'AP']]
Mbar   = [[M, 'VP'], [M, 'NEGP', 'VP']]
Nbar   = [[N, 'PP', 'CP']]
Pbar   = [[P, 'NP'], [P, 'MP'], [P, 'PP']]
Vbar   = [[V], [V, 'NP'], [V, 'NP', 'PP'], [V, 'PP']]
Abar   = [[A, 'PP', 'CP']]
Cbar   = [[C, 'MP']]



# Grabbing Lexical Items
def GetDeterminer():                                     #returns determiner
    return random.choice(list(DeterminerDict.keys()))
def GetModal():                                          #returns modal
    return random.choice(list(ModalDict.keys()))
def GetVerb():                                           #returns verb
    return random.choice(list(VerbDict.keys()))
def GetNoun():                                           #returns noun
    return random.choice(list(NounDict.keys()))

def GenerateNEGP():
    return random.choice(NEGP)
def GenerateMEASP():
    return random.choice(MEASP)
def GenerateDEGP():
    return random.choice(DEGP)
def GeneratePP():
    return random.choice(PP)
def GenerateDP():
    return random.choice(DP)
def GenerateMP():
    return random.choice(MP)  #this is generating the empty nodes instead of the markers that eventually represent those nodes
def GenerateNP():
    return random.choice(NP) 
def GenerateVP():
    return random.choice(VP)
def GenerateAP():
    return random.choice(AP)
def GenerateCP():
    return random.choice(CP)

def GenerateNEGbar():
    return random.choice(NEGbar)
def GenerateDEGbar():
    return random.choice(DEGbar)
def GeneratePbar():
    return random.choice(Pbar)
def GenerateMbar():
    return random.choice(Mbar)
def GenerateNbar():
    return random.choice(Nbar)
def GenerateVbar():
    return random.choice(Vbar)
def GenerateAbar():
    return random.choice(Abar)
def GenerateCbar():
    return random.choice(Cbar)

def GenPhraseToNodeMP():
    EMPEE = GenerateMP()
    for ConstitL1 in EMPEE:
        if ConstitL1 == ['NP', 'Mbar']:
            for ConstitL2 in ConstitL2:
                if ConstitL2 == 'NP':
                    ConstitL2 = GenerateNP()
                elif ConstitL2 == 'Mbar':
                    ConstitL2 = GenerateMbar()
        elif ConstitL1 == ['Mbar']:
            ConstitL1 = GenerateMbar()
    return EMPEE



def Query():
    print('What would you like to do?')
    request = input()
    if request == 'full test':
        print('The phrases:')
        print(f'NEGP = {NEGP}, MEASP = {MEASP}, DEGP = {DEGP}, PP = {PP}, DP = {DP}, \nNP = {NP}, MP = {MP}, \nVP = {VP}, AP = {AP}, CP = {CP}')
        print('The bars:')
        print(f'NEGbar = {NEGbar}, DEGbar = {DEGbar}, Mbar = {Mbar}, Nbar = {Nbar}, \nPbar = {Pbar}, Vbar = {Vbar}, Abar = {Abar}, \nCbar = {Cbar}')
        print('Checking the \'get\' statements:')
        print(GetDeterminer(), GetNoun(), GetModal(), GetVerb())

    elif request == 'phrase test':
        print('The phrases:')
        print(f'NEGP = {NEGP}, MEASP = {MEASP}, DEGP = {DEGP}, PP = {PP}, DP = {DP}, \nNP = {NP}, MP = {MP}, \nVP = {VP}, AP = {AP}, CP = {CP}')
    elif request == 'bar test':
        print('The bars:')
        print(f'NEGbar = {NEGbar}, DEGbar = {DEGbar}, Mbar = {Mbar}, Nbar = {Nbar}, \nPbar = {Pbar}, Vbar = {Vbar}, Abar = {Abar}, \nCbar = {Cbar}')
    elif request == 'get test':
        print(GetDeterminer(), GetNoun(), GetModal(), GetVerb())
    
    elif request == 'MP':
        print('How many MPs would you like to print?')
        numPs = int(input())
        while numPs !=0:
            print(GenerateMP())
            numPs -= 1
    elif request == 'NP':
        print('How many NPs would you like to print?')
        numPs = int(input())
        while numPs !=0:
            print(GenerateNP())
            numPs -= 1
    elif request == 'VP':
        print('How many NPs would you like to print?')
        numPs = int(input())
        while numPs !=0:
            print(GenerateVP())
            numPs -= 1
    elif request == 'CP':
        print('How many CPs would you like to print?')
        numPs = int(input())
        while numPs !=0:
            print(GenerateCP())
            numPs -= 1
    elif request == 'PP':
        print('How many PPs would you like to print?')
        numPs = int(input())
        while numPs !=0:
            print(GeneratePP())
            numPs -= 1

    elif request == 'Pbar':
        print('How many Pbars would you like to print?')
        numPs = int(input())
        while numPs !=0:
            print(GeneratePbar())
            numPs -= 1
    elif request == 'Nbar':
        print('How many Nbars would you like to print?')
        numPs = int(input())
        while numPs !=0:
            print(GenerateNbar())
            numPs -= 1
    elif request == 'Cbar':
        print('How many Cbars would you like to print?')
        numPs = int(input())
        while numPs !=0:
            print(GenerateCbar())
            numPs -= 1
    elif request == 'Mbar':
        print('How many Mbars would you like to print?')
        numPs = int(input())
        while numPs !=0:
            print(GenerateMbar())
            numPs -= 1
    elif request == 'Vbar':
        print('How many Vbars would you like to print?')
        numPs = int(input())
        while numPs !=0:
            print(GenerateVbar())
            numPs -= 1

    elif request == 'P2N MP':
        print('How many MPs would you like to generate to the nodes?')
        numPs = int(input())
        while numPs !=0:
            print(GenPhraseToNodeMP())
            numPs -= 1

    print('\nAnything else? (y/n)')
    if input() == 'y':
        Query()

    


print('')
print('')

Query()

print('\nThank you.  Program ended.')

print('')
print('')







#   JUNK TO GO GET TO LATER
#Vprime   = [[V], [V, NP], [V, DEGP], [V, PP], [V, CP], [V, NP, DEGP], [V, NP, PP], [V, NP, CP], [V, ]PP, CP] # FINISH MAKING ALL POSSIBLE Vprime COMBOS
