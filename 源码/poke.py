import random
from pprint import pprint
import os

values = list(range(2,11)) + 'J Q K A'.split()
suits = '♥ ♠ ♦ ♣'.split()
deck = ['%s  %s'%(s,v) for v in values for s in suits]
deck.append('大王')
deck.append('小王')
random.shuffle(deck)


while deck:
    os.system('cls')
    A = B =2
    
    pprint('A:')
    while A!=0:
        
        pprint(deck.pop())
        A = A-1

    pprint("   ")
    
    pprint('B')
    while B!=0:
        
        pprint(deck.pop())
        B =B-1
    input()
