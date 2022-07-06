# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 08:12:32 2022

@author: abackes
"""
import turns

# Dragon stats
class stats:
    def __init__(self, name, hp, ac, damage, bonus, strat, clas):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.damage = damage
        self.bonus = bonus
        self.strat = strat
        self.clas = clas

bbeg = stats("Dragon", 100, 18, 12, 9, False, False)
npc = stats("Hawyee", 40, 12, 8, 5, False, False)


p1 = turns.start()
if p1.clas == "Mage":
    flavor = "glass cannon"
elif p1.clas == "Fighter":
    flavor = "jack of all trades"
elif p1.clas == "Rogue":
    flavor = "wiley one"
    
    
print("You are: {}, a {}." .format(p1.name, flavor))
print("HP: ", p1.hp)
print("AC: ", p1.ac)
print("Damage: ", p1.damage)




print("\nwhoa dude there's a dragon\n")

#turns = [1, 1, 2, 3, 2]



for i in range(30):
    if p1.hp <= 0:
        break
    elif bbeg.hp <= 0:
        break
    print("Round ", i+1)
    for i in range(5):
        if p1.hp <= 0:
            break
        elif bbeg.hp <= 0:
            break
        if i == 0:
           if p1.strat == "Dead":
               p1.ac -= p1.bonus
               p1.strat = False
           p1, bbeg, npc = turns.your_turn(p1, bbeg, npc)  
        elif i == 1:
            p1, bbeg, npc = turns.your_turn(p1, bbeg, npc) 
        elif i == 2:
            if bbeg.strat == "rebound":
                bbeg.strat = False
            p1, bbeg, npc = turns.bbeg_turn(p1, bbeg, npc) 
        elif i == 3:
            p1, bbeg, npc = turns.bbeg_turn(p1, bbeg, npc) 
        elif i == 4 and npc.hp > 0:
            p1, bbeg, npc = turns.npc_turn(p1, bbeg, npc)
        elif npc.hp <= 0:
            print("{} has perished, and will not have a turn." .format(npc.name))
            
            
            

if p1.hp <= 0:
    print("You have been eaten by the dragon. Better luck next time.")
elif p1.hp > 0:
    if bbeg.hp > 0:
        print("Congradulations, you have escaped.")
    elif bbeg.hp <= 0:
        print("Congradulations, you have slain the dragon.")

    
