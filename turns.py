# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 09:28:13 2022

@author: abackes
"""
import random


class stats:
    def __init__(self, name, hp, ac, damage, bonus, strat, clas):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.damage = damage
        self.bonus = bonus
        self.strat = strat
        self.clas = clas
        
        
def start():
    print("Welcome, adventurer. Please choose a class: \nMage    Fighter    Rogue")
    clas=input("> ")
    clas = clas.capitalize()
    if clas == "Mage":
        hp = 70
        ac = 12
        damage = 16
        bonus = 8
    elif clas == "Fighter":
        hp = 100
        ac = 16
        damage = 8
        bonus = 7
    elif clas == "Rogue":
        hp = 85
        ac = 18
        damage = 8
        bonus = 8
    else:
        print("That is not a valid input.")
        start()
    print("You have chosen {}. An excellent choice. \nBut what is your name?" .format(clas))
    name = input("> ")
    print("{}, through luck or misfortune, you have arrived at the entrance to a cavern." .format(name))
    print("Will you enter with courage?")
    print("Y/N")
    enter_v = input("> ")
    if enter_v.capitalize() == "N":
        print("Well, that is unfortunate.\n\n")
    else:
        print("Indeed, you have no reason for fear.\n\n")
        
    p1 = stats(name, hp, ac, damage, bonus, False, clas)
    
    return p1




def your_turn(p1, bbeg, npc): 
    print("\nIt is your turn.")
    print("HP: ", p1.hp)
    print("AC: ", p1.ac)
    print("Strat: ", p1.strat)
    print("BBEG HP: ", bbeg.hp)
    print("\nWhat would you like to do? Enter a number.")
    print("1. Attack   2. Strategize   3. Heal   4. Play dead")
    turn = input("> ")
    
    
    if turn == "1":
        if p1.strat == "Fighter": # roll to hit, with strategy
            to_hit = random.randint(1,20) + (p1.bonus*2)
        else: # regular roll to hit
            to_hit = random.randint(1,20) + p1.bonus
            
        if to_hit >= bbeg.ac: # do you hit?
            damage_roll = random.randint(1, p1.damage)
            if p1.strat == "Mage": # double rolled if Mage strat
                damage_roll *= 2
                p1.strat = False
            elif p1.strat == "Fighter": # add another bonus if Fighter strat
                damage_roll += p1.bonus 
                p1.strat = False  
            total_damage = damage_roll + p1.bonus
            if bbeg.strat == "rebound":
                print("The dragon was ready for the attack, and will return some of the damage.")
                bbeg.hp = bbeg.hp - int(total_damage/2)
                if p1.strat == "Rogue":
                    p1.hp -= int(total_damage/4)
                    p1.strat = False
                    print("You have done {} damage to the dragon and {} to yourself." .format(int(total_damage/2), int(total_damage/4)))
                else:
                    p1.hp -= int(total_damage/2)
                    print("You have done {} damage, both to yourself and the dragon." .format(int(total_damage/2)))
            else:
                if npc.strat == "assist":
                    total_damage = int(total_damage * 1.5)
                    print("{} has assisted you." .format(npc.name))
                bbeg.hp -= total_damage
                print("You have done {} damage." .format(total_damage))
            
        else: # miss
            print("You have missed.")        
            
    elif turn == "2":
        if p1.clas == "Mage":
            print("You focus your arcane power. Next hit will deal double damage.")
        elif p1.clas == "Rogue":
            print("You ready your reflexes. Next damage you take will be halved.")
        elif p1.clas == "Fighter":
            print("You warm up your muscles. You are more likely to hit and will do increased damage.")
        p1.strat = p1.clas
    elif turn == "3":
        heal = random.randint(2,8)
        p1.hp += heal
        print("You heal for {} hp." .format(heal))
    else:
        print("You play dead.")
        print("You will be harder to hit until your next turn.")
        p1.strat = "Dead"
        p1.ac += p1.bonus
    
    return p1, bbeg, npc




def bbeg_turn(p1, bbeg, npc):
    print("\nIt is the dragon's turn.")
    action = random.randint(1,6)   
    
    if bbeg.hp <= 25:
        print("The dragon has chosen to heal.")
        bbeg.hp = bbeg.hp + random.randint(5,10)
    elif action == 1 and bbeg.strat == False:
        print("The dragon has chosen to strategize.")
        bbeg.strat = "powerup"
    elif action == 2 and bbeg.strat == False:
        print("The dragon has chosen to strategize.")
        bbeg.strat = "rebound"
    elif action == 3 and bbeg.hp <= 75:
        print("The dragon has chosen to heal.")
        bbeg.hp += random.randint(3, 15)    
    else:
        print("The dragon has chosen to attack.")
        to_hit = random.randint(1,20) + bbeg.bonus
        if to_hit >= p1.ac: # 
            damage_roll = random.randint(1, bbeg.damage) + bbeg.bonus
            if bbeg.strat == "powerup":
                damage_roll += random.randint(1,15)
                bbeg.strat = False
            if npc.strat == "sacrifice":
                print("You would have taken {} damage, but {} moves in front of the strike and takes the damage instead." .format(damage_roll, npc.name))
                npc.hp -= damage_roll
                npc.strat = False
            elif p1.strat == "Rogue":
                damage_roll = int(damage_roll / 2)
                p1.strat = False
                print("You would have taken {} damage, but will instead take half. You now have {} HP." .format(damage_roll*2), p1.hp)
            else:
                p1.hp -= damage_roll
                print("The dragon has hit and done {} damage. You now have {} HP." .format(damage_roll, p1.hp))
        else:
            print("The dragon has missed.")


    return p1, bbeg, npc



def npc_turn(p1, bbeg, npc):
    npc.strat = False
    print("\nIt is {}'s turn." .format(npc.name))
    print("What would you like them to do?")
    print("1. Attack   2. Strategize   3. Heal")
    turn = input("> ")
    
    if turn == "1":
        to_hit = random.randint(1,20) + npc.bonus
        if to_hit >= bbeg.ac: # do you hit?
            total_damage = random.randint(1, npc.damage) + npc.bonus
            if bbeg.strat == "rebound":
                print("The dragon was ready for the attack, and will return some of the damage.")
                bbeg.hp -= int(total_damage/2)
                npc.hp -= int(total_damage/2)
                print("{} has done {} damage, both to themself and the dragon." .format(npc.name, int(total_damage/2)))
            else:
                bbeg.hp -= total_damage
                print("They have done {} damage." .format(total_damage))
        else:
            print("{} has missed." .format(npc.name))
    elif turn == "2":
        print("Your companion is strategizing.")            
        npc.strat_rand = random.randint(1,3)
        if p1.hp < 25 or npc.strat_rand == 1:
            npc.strat = "sacrifice"
        else:
            npc.strat = "assist"
    elif turn == "3":
        heal = random.randint(4, 10)
        p1.hp += heal
        print("Your companion has healed you for {} points. You now have {} HP." .format(heal, p1.hp))
    else: 
        print("Invalid input, {} looks at you with confusion." .format(npc.name))
            
            
    return p1, bbeg, npc
