import pokebase as pb
from tkinter import *   
import tkinter as tk

rows = ["Name: ", "Type: ", "Height: ", "Weight: ", "Base experience: ", "HP: ","Attack: ", "Defense: ", "Special attack:", "Special defense: ", "Speed: ", "Type advantage: ", "Chance of winning: "]

root = Tk()
root.geometry("300x400")
root.title("Pokemons comparer")
root.configure(bg='gray18')

poke1_var=tk.StringVar()
poke2_var=tk.StringVar()
def getChance(x, y):
    chance = 50
    for i in range (2,11):
        if x[i] > y[i]:
            chance += 5
        if x[i] < y[i]:
            chance -= 5
    return chance

def getMulti(x, y):
    multi = 1
    
    typeIDone = 0
    if ((x[1] == "fighting") or (x[1] == "rock") or (x[1] == "steel") or (x[1] == "ground")):
        typeIDone = 1
    if ((x[1] == "fire") or (x[1] == "normal") or (x[1] == "electric") or (x[1] == "ice") or (x[1] == "water")):
        typeIDone = 2
    if ((x[1] == "grass") or (x[1] == "poison") or (x[1] == "fairy") or (x[1] == "bug")):
        typeIDone = 3
    if ((x[1] == "dark") or (x[1] == "ghost") or (x[1] == "flying") or (x[1] == "dragon") or (x[1] == "psychic") or (x[1] == "shadow" or (x[1] == "unknown"))):
        typeIDone = 4  
        
    typeIDtwo = 0
    if ((y[1] == "fighting") or (y[1] == "rock") or (y[1] == "steel") or (y[1] == "ground")):
        typeIDtwo = 1
    if ((y[1] == "fire") or (y[1] == "normal") or (y[1] == "electric") or (y[1] == "ice") or (y[1] == "water")):
        typeIDtwo = 2
    if ((y[1] == "grass") or (y[1] == "poison") or (y[1] == "fairy") or (y[1] == "bug")):
        typeIDtwo = 3
    if ((y[1] == "dark") or (y[1] == "ghost") or (y[1] == "flying") or (y[1] == "dragon") or (y[1] == "psychic") or (y[1] == "shadow" or (y[1] == "unknown"))):
        typeIDtwo = 4              
    
    if ((typeIDone == typeIDtwo-1) or ((typeIDone == 4) and (typeIDtwo == 1))):
        multi = 2
        
    if ((typeIDone == typeIDtwo+1) or ((typeIDone == 1) and (typeIDtwo == 4))):
        multi = 0
    
    return multi

def submit():
 
    poke1=poke1_var.get()
    poke2=poke2_var.get()
     
    pokemon1 = pb.pokemon(poke1)
    pokemonOne = []
    pokemonOne.extend((pokemon1.name.capitalize(), pokemon1.types[0].type.name, pokemon1.height, pokemon1.weight, pokemon1.base_experience, pokemon1.stats[0].base_stat, pokemon1.stats[1].base_stat, pokemon1.stats[2].base_stat, pokemon1.stats[3].base_stat, pokemon1.stats[4].base_stat, pokemon1.stats[5].base_stat))
    
    pokemon2 = pb.pokemon(poke2)
    pokemonTwo = []
    pokemonTwo.extend((pokemon2.name.capitalize(), pokemon2.types[0].type.name, pokemon2.height, pokemon2.weight, pokemon2.base_experience, pokemon2.stats[0].base_stat, pokemon2.stats[1].base_stat, pokemon2.stats[2].base_stat, pokemon2.stats[3].base_stat, pokemon2.stats[4].base_stat, pokemon2.stats[5].base_stat))
    
    multi = getMulti(pokemonOne, pokemonTwo)
    pokemonOne.append(multi)
    multi = getMulti(pokemonTwo, pokemonOne)
    pokemonTwo.append(multi)
    
    chance = getChance(pokemonOne, pokemonTwo)
    pokemonOne.append(chance)
    chance = getChance(pokemonTwo, pokemonOne)
    pokemonTwo.append(chance)
    
    count = 0
    for x in rows:
        lbl = Label(root, text=rows[count], bg='gray18', fg='white')
        lbl.grid(column=0, row=count+4)
        count +=1
    count = 0
    for x in pokemonOne:
        lbl = Label(root, text=pokemonOne[count], bg='gray18', fg='white')
        lbl.grid(column=1, row=count+4)
        count +=1
    count = 0
    for x in pokemonTwo:
        lbl = Label(root, text=pokemonTwo[count], bg='gray18', fg='white')
        lbl.grid(column=2, row=count+4)
        count +=1

    poke1_var.set("")
    poke2_var.set("")    

poke1_label = tk.Label(root, text = 'Pokemon 1', font=('calibre',10, 'bold'), bg='gray18', fg='white')
poke1_entry = tk.Entry(root,textvariable = poke1_var, font=('calibre',10,'normal'), bg='gray36', fg='white')
poke2_label = tk.Label(root, text = 'Pokemon 2', font = ('calibre',10,'bold'), bg='gray18', fg='white')
poke2_entry=tk.Entry(root, textvariable = poke2_var, font = ('calibre',10,'normal'), bg='gray36', fg='white')
sub_btn=tk.Button(root,text = 'Submit', command = submit, bg='gray36', fg='white')

poke1_label.grid(row=0,column=0)
poke1_entry.grid(row=0,column=1)
poke2_label.grid(row=1,column=0)
poke2_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)

root.mainloop()
