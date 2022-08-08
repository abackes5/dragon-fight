"""

import tkinter as tk
from tkinter import ttk

class stats:
    def __init__(self, name, hp, ac, damage, bonus, strat, clas):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.damage = damage
        self.bonus = bonus
        self.strat = strat
        self.clas = clas

root = tk.Tk()
root.title('Initializing [2]')
root.geometry("300x180")

x=15
p1 = []

def statify(x):
    p1 = ["Hawyee", 40, x, 8, 5, False, False]

    return p1

def onward():
    root.quit()
    root.destroy()

name_button = ttk.Button(root, text="Test", command = lambda: p1 == statify(x))
name_button.pack(fill='x', expand=True, pady=10)

cont_button = ttk.Button(root, text="Continue", command = onward)
cont_button.pack(fill='x', expand=True)

root.mainloop()

print(p1)
"""

from tkinter import * 
 
class stats:
    def __init__(self, name, hp, ac, damage, bonus, strat, clas):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.damage = damage
        self.bonus = bonus
        self.strat = strat
        self.clas = clas


root=Tk() 
 
def method2(): 
    x="Done it !" 
    y = 86
    m.set(x)
    n.set(y)

 
m=StringVar() 
n = IntVar()
b1=Button(root, text="Click", command=method2).pack() 
lb1=Label(root, text="...", textvariable=m).pack() 
lb2=Label(root, text="...", textvariable=n).pack() 

root.mainloop()

print(m.get())
print(type(m))
print(n.get())
print(type(n))

#p1 = stats(m.get(), n.get(), 2, 2, 2, False, False)
print(p1.name, p1.hp, p1.ac)










