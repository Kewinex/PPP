import pokebase as pb
from tkinter import *   
import tkinter as tk

rows = ["Name: ", "Type: ", "Height: ", "Weight: ", "Base experience: ", "HP: ","Attack: ", "Defense: ", "Special attack:", "Special defense: ", "Speed: ", "No damage to: ", "Half damage to: ", "Double damage to: ", "No damage from: ", "Half damage from: ", "Double damage from: "]

root = Tk()
root.geometry("600x400")
root.title("Pokemons comparer")

poke1_var=tk.StringVar()
poke2_var=tk.StringVar()

def submit():
 
    poke1=poke1_var.get()
    poke2=poke2_var.get()
     
    pokemon1 = pb.pokemon(poke1)
    type = pb.type_(pokemon1.types[0].type.name)
    pokemon1 = []
    pokemon1.extend((pokemon1.name.capitalize(), pokemon1.types[0].type.name, pokemon1.height, pokemon1.weight, pokemon1.base_experience, pokemon1.stats[0].base_stat, pokemon1.stats[1].base_stat, pokemon1.stats[2].base_stat, pokemon1.stats[3].base_stat, pokemon1.stats[4].base_stat, pokemon1.stats[5].base_stat))
    
    pokemon2 = pb.pokemon(poke2)
    type = pb.type_(pokemon2.types[0].type.name)
    pokemon2 = []
    pokemon2.extend((pokemon2.name.capitalize(), pokemon2.types[0].type.name, pokemon2.height, pokemon2.weight, pokemon2.base_experience, pokemon2.stats[0].base_stat, pokemon2.stats[1].base_stat, pokemon2.stats[2].base_stat, pokemon2.stats[3].base_stat, pokemon2.stats[4].base_stat, pokemon2.stats[5].base_stat))

    """
    , type.damage_relations.no_damage_to[0].name, type.damage_relations.half_damage_to[0].name, type.damage_relations.double_damage_to[0].name, type.damage_relations.no_damage_from[0].name, type.damage_relations.half_damage_from[0].name, type.damage_relations.double_damage_from[0].name
    """

    count = 0
    for x in rows:
        lbl = Label(root, text=rows[count])
        lbl.grid(column=0, row=count+4)
        count +=1
    count = 0
    for x in pokemon1:
        lbl = Label(root, text=pokemon1[count])
        lbl.grid(column=1, row=count+4)
        count +=1
    count = 0
    for x in pokemon2:
        lbl = Label(root, text=pokemon2[count])
        lbl.grid(column=2, row=count+4)
        count +=1

    poke1_var.set("")
    poke2_var.set("")    

poke1_label = tk.Label(root, text = 'Pokemon 1', font=('calibre',10, 'bold'))
poke1_entry = tk.Entry(root,textvariable = poke1_var, font=('calibre',10,'normal'))
poke2_label = tk.Label(root, text = 'Pokemon 2', font = ('calibre',10,'bold'))
poke2_entry=tk.Entry(root, textvariable = poke2_var, font = ('calibre',10,'normal'))
sub_btn=tk.Button(root,text = 'Submit', command = submit)

poke1_label.grid(row=0,column=0)
poke1_entry.grid(row=0,column=1)
poke2_label.grid(row=1,column=0)
poke2_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)

root.mainloop()




