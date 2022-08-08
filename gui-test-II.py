import tkinter as tk
from tkinter import ttk


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





# setup 

setup = tk.Tk()
setup.title('Initializing [1]')
setup.geometry("300x150")

def name_clicked():
    named = name.get()
    setup.quit()
    setup.destroy()
    
    

signin = ttk.Frame(setup)
signin.pack(padx=10, pady=10, fill='x', expand=True)

named = tk.StringVar()

# email
name_label = ttk.Label(signin, text="Welcome. Please enter your name.")
name_label.pack(fill='x', expand=True)

name = tk.StringVar()
name_entry = ttk.Entry(signin, textvariable=name)
name_entry.pack(fill='x', expand=True)
name_entry.focus()

name_button = ttk.Button(signin, text="Enter", command = name_clicked)
name_button.pack(fill='x', expand=True, pady=10)


setup.mainloop()

named = name.get()


# Pick a class!

choose = tk.Tk()
choose.title('Initializing [2]')
choose.geometry("300x180")
p1 = stats("Hawyee", 40, 12, 8, 5, False, False)

def gray():
    mage_button.state(['disabled'])
    fighter_button.state(['disabled'])
    rogue_button.state(['disabled'])
    cont_button.state(['!disabled'])
def onward():
    choose.quit()
    choose.destroy()
def mage():
    cl_pick.config(text = "You have chosen Mage.")
    clas.set("Mage")
    hp.set(70)
    ac.set(12)
    damage.set(16)
    bonus.set(8)
    strat.set("None")

    gray()

def fighter():
    cl_pick.config(text = "You have chosen Fighter.")
    clas.set("Fighter")
    hp.set(100)
    ac.set(16)
    damage.set(8)
    bonus.set(6)
    strat.set("None")
    
    gray()

def rogue():
    cl_pick.config(text = "You have chosen Rogue.")
    clas.set("Rogue")
    hp.set(85)
    ac.set(18)
    damage.set(8)
    bonus.set(8)
    strat.set("None")
    
    gray()

clas = tk.StringVar()
hp = tk.IntVar()
ac = tk.IntVar()
damage = tk.IntVar()
bonus = tk.IntVar()
strat = tk.StringVar()



cl_pick = ttk.Label(choose, text="Please choose a class.")
cl_pick.pack(fill = 'x', expand=True)
mage_button = ttk.Button(choose, text="Mage", command = mage)
mage_button.pack(fill='x', expand=True)
fighter_button = ttk.Button(choose, text="Fighter", command = fighter)
fighter_button.pack(fill='x', expand=True)
rogue_button = ttk.Button(choose, text="Rogue", command = rogue)
rogue_button.pack(fill='x', expand=True)
cont_button = ttk.Button(choose, text="Continue", command = onward)
cont_button.pack(fill='x', expand=True)
cont_button.state(['disabled'])


choose.mainloop()

p1 = stats(named, hp.get(), ac.get(), damage.get(), bonus.get(), strat.get(), clas.get())


# main game

root = tk.Tk()
root.title('D&D Is For Nerds')
root.geometry("600x240")

for i in range(0,11):
    root.columnconfigure(i, weight=1)
    
    
def attack():
    flavor.config(text = "you attacked")
def heal():
    flavor.config(text = "you healed")
    p1_s22.config(textvariable=p1.hp)
def strategize():
    flavor.config(text = "you strategized")
def dodge():
    flavor.config(text = "you dodged")
def cont():
    flavor.config(text = "onward")
    attack_button.state(['!disabled'])
    heal_button.state(['!disabled'])
    strat_button.state(['!disabled'])
    dodge_button.state(['!disabled'])
    cont_button.state(['disabled'])

# put the button functions here








































P1_colors = {'background': "#89CE94", 'foreground': "#333333"}
NPC_colors = {'background': "#86A59C", 'foreground': "#333333"}
bbeg_colors = {'background': "#7d5ba6", 'foreground': "white"}             
             
p1_name = ttk.Label(root, text="...", textvariable=p1.name, **P1_colors)
p1_name.grid(column=0, row=0, columnspan = 4, ipady=5, sticky="EW")

npc_name = ttk.Label(root, text = "NPC", **NPC_colors)
npc_name.grid(column=4, row=0, columnspan = 4, ipady=5, sticky="EW")

bbeg_name = ttk.Label(root, text = "BBEG", **bbeg_colors)
bbeg_name.grid(column=8, row=0, columnspan = 4, ipady=5, sticky="EW")


p1_s1 = ttk.Label(root, text = "HP", **P1_colors)
p1_s2 = ttk.Label(root, text = "AC", **P1_colors)
p1_s3 = ttk.Label(root, text = "Strategy", **P1_colors)
p1_s11 = ttk.Label(root, text="...", textvariable=hp, **P1_colors)
p1_s22 = ttk.Label(root, text="...", textvariable=ac, **P1_colors)
p1_s33 = ttk.Label(root, text="...", textvariable=strat, **P1_colors)

npc_s1 = ttk.Label(root, text = "NPC S1", **NPC_colors)
npc_s2 = ttk.Label(root, text = "NPC S2", **NPC_colors)
npc_s3 = ttk.Label(root, text = "NPC S3", **NPC_colors)
npc_s11 = ttk.Label(root, text = "NPC HP", **NPC_colors)
npc_s22 = ttk.Label(root, text = "NPC AC", **NPC_colors)
npc_s33 = ttk.Label(root, text = "NPC STRAT", **NPC_colors)

bbeg_s1 = ttk.Label(root, text = "BBEG S1", **bbeg_colors)
bbeg_s2 = ttk.Label(root, text = "BBEG S2", **bbeg_colors)
bbeg_s3 = ttk.Label(root, text = "BBEG S3", **bbeg_colors)
bbeg_s11 = ttk.Label(root, text = "???", **bbeg_colors)
bbeg_s22 = ttk.Label(root, text = "???", **bbeg_colors)
bbeg_s33 = ttk.Label(root, text = "BBEG strat?", **bbeg_colors)

hp_grid = [p1_s1, p1_s11, npc_s1, npc_s11, bbeg_s1, bbeg_s11]
ac_grid = [p1_s2, p1_s22, npc_s2, npc_s22, bbeg_s2, bbeg_s22]
strat_grid = [p1_s3, p1_s33, npc_s3, npc_s33, bbeg_s3, bbeg_s33]

for i in range(1, 4):
    c = 0
    if i == 1:
        for l in hp_grid:
            l.grid(column=c, row=i, columnspan = 2, ipadx=15, ipady=5, sticky="EW")
            c +=2
    if i == 2:
        for l in ac_grid:
            l.grid(column=c, row=i, columnspan = 2, ipadx=15, ipady=5, sticky="EW")
            c +=2
    if i == 3:
        for l in strat_grid:
            l.grid(column=c, row=i, columnspan = 2, ipadx=15, ipady=5, sticky="EW")
            c +=2



















flavor = ttk.Label(root, text= "Here's what's up", background = "#333333", foreground="white")
flavor.grid(column=0, row=4, columnspan = 12, ipady=15, sticky="EW")

attack_button = ttk.Button(root, text = "Attack")
attack_button.grid(column = 0, row = 5, columnspan = 3, sticky="EW")
attack_button.configure(command=attack)

heal_button = ttk.Button(root, text = "Heal")
heal_button.grid(column = 3, row = 5, columnspan = 3, sticky="EW")
heal_button.configure(command=heal)

strat_button = ttk.Button(root, text = "Strategize")
strat_button.grid(column = 6, row = 5, columnspan = 3, sticky="EW")
strat_button.configure(command=strategize)

dodge_button = ttk.Button(root, text = "Play dead")
dodge_button.grid(column = 9, row = 5, columnspan = 3, sticky="EW")
dodge_button.configure(command=dodge)

cont_button = ttk.Button(root, text = "Continue")
cont_button.grid(column = 9, row = 6, pady = 5, columnspan = 3, sticky="EW")
cont_button.configure(command=cont)



attack_button.state(['disabled'])
heal_button.state(['disabled'])
strat_button.state(['disabled'])
dodge_button.state(['disabled'])

root.mainloop()































