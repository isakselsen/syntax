

import random
from tkinter import Y

class Noun:                                                 #noun class, with: count/mass, plrurality
    def __init__(self, base_form, count, plural):
        self.base_form = base_form
        self.count     = count
        self.plural    = plural
class Verb:                                                 #verb class with: max/min args, plurality, weak/strong
    def __init__(self, base_form, maxargs, minargs, plural, weak = True):
        self.base_form = base_form
        self.maxargs   = maxargs
        self.minargs   = minargs
        self.plural    = plural
        self.weak      = weak
class Modal:                                                #modal class with: finite/infinitive
    def __init__(self, base_form, finite):
        self.base_form = base_form
        self.finite    = finite
class Determiner:                                           #determiner class with: plurality
    def __init__(self, base_form, plural):
        self.base_form = base_form
        self.plural = plural
class Pronoun:
    def __init__(self, base_form, gender, plural):
        self.base_form = base_form
        self.gender = gender
        self.plurality = plural
#some nouns
NounDict             = {}
NounDict ['love']    = ('love', False, False)
NounDict ['beans']   = ('beans', True, True)
NounDict ['sand']    = ('sand', False, False)
NounDict ['cup']     = ('cup', True, False)
NounDict ['cats']    = ('cats', True, True)
NounDict ['bravery'] = ('bravery', False, True)
NounDict ['oxen']    = ('oxen', True, True)
for word, properties in NounDict.items():
    word = Noun(*properties)
#some verbs
VerbDict               = {}
VerbDict ['wait']      = ('wait', 1, 1, True)
VerbDict ['waits']     = ('waits', 1, 1, False)
VerbDict ['resonate']  = ('resonate', 2, 1, True)
VerbDict ['resonates'] = ('resonates', 2, 1, False)
for word, properties in VerbDict.items():
    word = Verb(*properties)
#some modals
ModalDict          = {}
ModalDict ['will'] = ('will', True)
ModalDict ['may']  = ('may', True)
ModalDict ['can']  = ('can', True)
for word, properties in ModalDict.items():
    word = Modal(*properties)
#some determiners
DeterminerDict          = {}
DeterminerDict ['a']    = ('a', False)
DeterminerDict ['the']  = ('the', False)
DeterminerDict ['some'] = ('some', True)
DeterminerDict ['an']   = ('an', False)
for word, properties in DeterminerDict.items():
    word = Determiner(*properties)
#some pronouns
PronounDict          = {}
PronounDict ['it'] = ('it', None, False)
PronounDict ['she']  = ('she', 'Feminine', False)
PronounDict ['They']  = ('They', None, None)
for word, properties in PronounDict.items():
    word = Pronoun(*properties)

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
DEGP  = [['DEGbar']]
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
Vbar   = [[V], [V, 'NP'], [V, 'NP', 'PP'], [V, 'PP'], [V, 'CP']]
Abar   = [[A], [A, 'PP'], [A, 'CP'], [A, 'PP', 'CP']]
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
def GetPronoun():                                           #returns pronoun
    return random.choice(list(PronounDict.keys()))

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

def GeneratePhraseDaughters(phrases):
    next_phrase_level = []
    for phrase in phrases:
        if phrase == 'MP':
            next_phrase_level.append(GenerateMP())
        elif phrase == 'NP':
            next_phrase_level.append(GenerateNP())
        elif phrase == 'VP':
            next_phrase_level.append(GenerateVP())
        elif phrase == 'CP':
            next_phrase_level.append(GenerateCP())
        elif phrase == 'PP':
            next_phrase_level.append(GeneratePP())
        elif phrase == 'Pbar':
            next_phrase_level.append(GeneratePbar())
        elif phrase == 'Nbar':
            next_phrase_level.append(GenerateNbar())
        elif phrase == 'Cbar':
            next_phrase_level.append(GenerateCbar())
        elif phrase == 'Mbar':
            next_phrase_level.append(GenerateMbar())
        elif phrase == 'Vbar':
            next_phrase_level.append(GenerateVbar())
    print('This is the current phrase Im returning:', next_phrase_level)
    return next_phrase_level

def GeneratePhraseToNodes(starting_point):
    if 'MP' or 'NP' or 'VP' or 'CP' or 'PP' or 'Pbar' or 'Nbar' or 'Cbar' or 'Mbar' or 'Vbar' in starting_point:
        nodes = GeneratePhraseToNodes(GeneratePhraseDaughters(starting_point))
    else:
        return nodes

def SpelloutNodes(surface_structure):
    spellout = []
    for node in surface_structure:
        if node == 'D':
            spellout.append(GetDeterminer())
        elif node == 'N':
            spellout.append(GetNoun())
        elif node == 'V':
            spellout.append(GetVerb())
        elif node == 'M':
            spellout.append(GetModal())
    return spellout

def DeriveSpellout(initial_phrase):
    SpelloutNodes(GeneratePhraseToNodes(initial_phrase))





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
    elif request == 'spellout':
        print('what would you like to spellout?')
        requested_top_level_phrase = input()
        print('How many would you like to spell out?')
        numPs = int(input())
        while numPs !=0:
            print((DeriveSpellout(requested_top_level_phrase)))
            numPs -= 1

    #elif request == 'Pop Deep Structure':


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
