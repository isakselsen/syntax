

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
    def __init__(self, finite, tense):
        self.finite = finite
        self.tense  = tense
class Determiner:
    def __init__(self, plural):
        self.plural = plural
class Preposition:
    def __init__(self):
        pass
class Adjective:
    def __init__(self):
        pass
class Complimentizer:
    def __init__(self):
        pass
    
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
ModalDict ['will'] = (True, 'future')
ModalDict ['may']  = (True, 'future')
ModalDict ['can']  = (True, 'future')
for word, properties in ModalDict.items():
    word = Modal(*properties)
#some determiners
DeterminerDict          = {}
DeterminerDict ['a']    = (False)
DeterminerDict ['the']  = (False)
DeterminerDict ['some'] = (True)
DeterminerDict ['an']   = (False)
for word, properties in DeterminerDict.items():
    word = Determiner(properties)
#some prepositions
PrepositionDict            = {}
PrepositionDict ['around'] = ()
PrepositionDict ['near']   = ()
PrepositionDict ['from']   = ()
for word, properties in PrepositionDict.items():
    word = Preposition(*properties)
#some adjectives
AdjectiveDict                 = {}
AdjectiveDict ['hungry']      = ()
AdjectiveDict ['rotund']      = ()
AdjectiveDict ['thoughtless'] = ()
for word, properties in AdjectiveDict.items():
    word = Adjective(*properties)
#some complimentizers
ComplimentizerDict         =  {}
ComplimentizerDict ['and'] = ()
for word, properties in ComplimentizerDict.items():
    word = Complimentizer(*properties)


# Lexical Item Names
M    = "modal"
V    = "verb"
P    = "preposition"
N    = "noun"
D    = "determiner"
A    = "adjective"
C    = "complimentizer"
NEG  = "not"
DEG  = "degree"
NAME = "name"
PRON = "pronoun"
POSS = "possessive marker"
NULL = ""
# Phrase Structures
NEGP  = [['NEGbar']]
MEASP = [['UNKNOWN']]
DEGP  = [['DEGbar', 'AP']]
PP    = [['MEASP', 'Pbar']]
DP    = [['Dbar']]
NP    = ['PRON', 'NAME', ['DP', 'Nbar']]
MP    = [['NP', 'Mbar']]                                 # MPs should also contain NPs
VP    = [['Vbar', 'VP'], ['Vbar']]
AP    = [['Abar']]
CP    = [['Cbar']]
# Prime Structures
NEGbar = [['NEG', 'VP']]
DEGbar = [['DEG', 'AP']]
Pbar   = [[P, 'NP'], [P, 'MP'], [P, 'PP']]
Dbar   = [[D]]
Nbar   = [[N], [N, 'PP']]                                # Nbars should also contain CPs
Mbar   = [[M, 'VP'], [M, 'NEGP', 'VP']]
Vbar   = [[V], [V, 'NP'], [V, 'NP', 'PP'], [V, 'PP']]
Abar   = [[A, 'PP']]                                     # Abars should also contain CPs
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
def GetPreposition():
    return random.choice(list(PrepositionDict.keys()))
def GetAdjective():
    return random.choice(list(AdjectiveDict.keys()))
def GetComplimentizer():
    return random.choice(list(Complimentizer.keys()))

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
    return random.choice(MP)             #this is generating the empty nodes instead of the markers that eventually represent those nodes
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
def GenerateDbar():
    return random.choice(Dbar)
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
    JJ = 'y'
    starting_mp = GenerateMP()
    print(f'this is the starting MP: \n{starting_mp}')
    while JJ == 'y':
        one_layer_down = MoveOneLayerDeeper(starting_mp)
        print(f'This should be one layer down from the last layer: \n{one_layer_down}')
        print(f'would you like to apply again? (y/n)')
        starting_mp = one_layer_down
        JJ = input()



    

def MoveOneLayerDeeper(top_layer):
    bottom_layer = []
    for constituant in top_layer:
        if constituant   == 'modal':
            bottom_layer.append(GetModal())
        elif constituant == 'verb':
            bottom_layer.append(GetVerb())
        elif constituant == 'preposition':
            bottom_layer.append(GetPreposition())
        elif constituant == 'noun':
            bottom_layer.append(GetNoun())
        elif constituant == 'determiner':
            bottom_layer.append(GetDeterminer())
        elif constituant == 'adjective':
            bottom_layer.append(GetAdjective())
        elif constituant == 'complimentizer':
            bottom_layer.append(GetComplimentizer())
        elif constituant == 'NEG':
            bottom_layer.append('not')
        elif constituant == 'degree':                        # FIX THIS, THIS IS A STOPGAP
            bottom_layer.append('degree')                    
        elif constituant == 'NAME':                          # FIX THIS, THIS IS A STOPGAP
            bottom_layer.append('Jerry')          
        elif constituant == 'PRON':
            bottom_layer.append()
        elif constituant == 'MP':
            bottom_layer.append(GenerateMP())
        elif constituant == 'VP':
            bottom_layer.append(GenerateVP())
        elif constituant == 'NP':
            bottom_layer.append(GenerateNP())
        elif constituant == 'DP':
            bottom_layer.append(GenerateDP())
        elif constituant == 'PP':
            bottom_layer.append(GeneratePP())
        elif constituant == 'AP':
            bottom_layer.append(GenerateAP())
        elif constituant == 'CP':
            bottom_layer.append(GenerateCP())
        elif constituant == 'Mbar':
            bottom_layer.append(GenerateMbar())
        elif constituant == 'Vbar':
            bottom_layer.append(GenerateVbar())
        elif constituant == 'Nbar':
            bottom_layer.append(GenerateNbar())
        elif constituant == 'Dbar':
            bottom_layer.append(GenerateDbar())
        elif constituant == 'Pbar':
            bottom_layer.append(GeneratePbar())
        elif constituant == 'Abar':
            bottom_layer.append(GenerateAbar())
        elif constituant == 'Cbar':
            bottom_layer.append(GenerateCbar())
        elif constituant == 'NEGbar':
            bottom_layer.append(GenerateNEGbar())
        elif constituant == 'DEGbar':
            bottom_layer.append(GenerateDEGbar())
    return bottom_layer
        

        

# def GenPhraseToNodeMP():                          #should generate an MP down to the nodes ('N', 'Det', 'P', etc)
#     EMPEE = GenerateMP()
#     print(f'This is an MP that will be used to generate a sentence: {EMPEE}')
#     for level_one_Constituent in range(len(EMPEE)):
#         if level_one_Constituent == ['NP', 'Mbar']:
#             for ConstitL2 in level_one_Constituent:
#                 if ConstitL2 == 'NP':
#                     ConstitL2 = GenerateNP()
#                 elif ConstitL2 == 'Mbar':
#                     ConstitL2 = GenerateMbar()
#         elif level_one_Constituent == ['Mbar']:
#             level_one_Constituent = GenerateMbar()
#     return EMPEE

# def GenPhraseToNodeMP():                          #should generate an MP down to the nodes ('N', 'Det', 'P', etc)
#     EMPEE = GenerateMP()
#     for ConstitL1 in range(len(EMPEE)):
#         if ConstitL1 == ['NP', 'Mbar']:
#             for ConstitL2 in ConstitL1:
#                 if ConstitL2 == 'NP':
#                     ConstitL2 = GenerateNP()
#                 elif ConstitL2 == 'Mbar':
#                     ConstitL2 = GenerateMbar()
#         elif ConstitL1 == ['Mbar']:
#             ConstitL1 = GenerateMbar()
#     return EMPEE

#   TRY RETURNING RATHER THAN PRINTING # THANK YOU MIN

def Query():
    print(f'What would you like to do?')
    request = input()
    if request == 'full test':
        print(f'     The phrases:\nNEGP =  {NEGP}\nMEASP = {MEASP}\nDEGP =  {DEGP}\nPP =    {PP}\nDP =    {DP}\nNP =    {NP}\nMP =    {MP}\nVP =    {VP}\nAP =    {AP}\nCP =    {CP}')
        print('     The bars:')
        print(f'NEGbar = {NEGbar}\nDEGbar = {DEGbar}\nMbar = {Mbar}\nNbar = {Nbar}\nPbar = {Pbar}\nVbar = {Vbar}\nAbar = {Abar}\nCbar = {Cbar}')
        print('     The \'get\' statements:')
        print(f'determiner = {GetDeterminer()}\nNoun = {GetNoun()}\nModal = {GetModal()}\nVerb = {GetVerb()}')

    elif request == 'phrase test':
        print('The phrases:')
        print(f'NEGP = {NEGP}\nMEASP = {MEASP}\nDEGP = {DEGP}\nPP = {PP}\nDP = {DP}, \nNP = {NP}\nMP = {MP}\nVP = {VP}\nAP = {AP}\nCP = {CP}')
    elif request == 'bar test':
        print('The bars:')
        print(f'NEGbar = {NEGbar}\nDEGbar = {DEGbar}\nMbar = {Mbar}\nNbar = {Nbar}, \nPbar = {Pbar}\nVbar = {Vbar}\nAbar = {Abar}bar test\nCbar = {Cbar}')
    elif request == 'get test':
        print(f'determiner = {GetDeterminer()}\nNoun = {GetNoun()}\nModal = {GetModal()}\nVerb = {GetVerb()}')
    
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
        print('How many VPs would you like to print?')
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
    elif request == 'DP':
        print('How many DPs would you like to print?')
        numPs = int(input())
        while numPs !=0:
            print(GenerateDP())
            numPs -= 1

    elif request == 'Pbar':
        print('How many Pbars would you like to print?')
        numPs = int(input())
        while numPs !=0:
            print(GeneratePbar())
            numPs -= 1
    elif request == 'Dbar':
        print('How many Dbars would you like to print?')
        numPs = int(input())
        while numPs !=0:
            print(GenerateDbar())
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
