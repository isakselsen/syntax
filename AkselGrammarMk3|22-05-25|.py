

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
# Phrase Structures
NEGP  = ['NEGbar']
MEASP = []
DEGP  = ['DEGbar', 'AP']
PP    = ['MEASP', 'Pbar']
DP    = [['NP', 'POSS'], D]
NP    = ['PRON', 'NAME', 'Nbar', ['DP', 'Nbar'], ['DEGP']]
MP    = [['NP', 'Mbar'], ['CP', 'Nbar']]
VP    = [[V, 'VP'], ['Vbar']]
AP    = ['Abar']
CP    = ['Cbar']
# Prime Structures
NEGbar = ['NEG', 'VP']
DEGbar = ['DEG', 'AP']
Mbar   = [[M, 'VP'], [M, 'NEGP', 'VP']]
Nbar   = [N, 'PP', 'CP']
Pbar   = [[P, 'NP'], [P, 'MP'], [P, 'PP']]
Vbar   = [V]
Abar   = [A, 'PP', 'CP']
Cbar   = [C, 'MP']



# Grabbing Lexical Items
def GetDeterminer():                                     #returns determiner
    return random.choice(list(DeterminerDict.keys()))
def GetModal():                                          #returns modal
    return random.choice(list(ModalDict.keys()))
def GetVerb():                                           #returns verb
    return random.choice(list(VerbDict.keys()))
def GetNoun():                                           #returns noun
    return random.choice(list(NounDict.keys()))

def GenerateMP():
    return random.choice(MP)  #this is generating the empty nodes instead of the markers that eventually represent those nodes



print('Would you like to run a full test gamut? {y/n}')

if input() == 'y':
    print('The phrases:')
    print(NEGP, MEASP, DEGP, PP, DP)
    print(NP, MP, VP, AP, CP)
    print('The bars:')
    print(NEGbar, DEGbar, Mbar, Nbar, Pbar, Vbar, Abar, Cbar)
    print('Checking the \'get\' statements:')
    print(GetDeterminer, GetModal, GetVerb, GetNoun)
else:
    print('Would you like to test the phrases?')
    if input() == 'y':
        print('The phrases:')
        print(NEGP, MEASP, DEGP, PP, DP)
    else:
        print('Would you like to test the bars?')
        if input() == 'y':
            print('The bars:')
            print(NEGbar, DEGbar, Mbar, Nbar, Pbar, Vbar, Abar, Cbar)
        else:
            print('Would you like to test the get statements?')
            if input() == 'y':
                    print(GetDeterminer, GetModal, GetVerb, GetNoun)


                    
                    



#   JUNK TO GO GET TO LATER
#Vprime   = [[V], [V, NP], [V, DEGP], [V, PP], [V, CP], [V, NP, DEGP], [V, NP, PP], [V, NP, CP], [V, ]PP, CP] # FINISH MAKING ALL POSSIBLE Vprime COMBOS
