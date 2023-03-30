import pokebase as pb
from tkinter import *

rows = ["Name: ", "Type: ", "Height: ", "Weight: ", "Base experience: ", "HP: ","Attack: ", "Defense: ", "Special attack:", "Special defense: ", "Speed: ", "No damage to: ", "Half damage to: ", "Double damage to: ", "No damage from: ", "Half damage from: ", "Double damage from: "]

def tr(stat):
    try:
        pokemon1.extend(stat)
    except:
        pokemon1.extend("Undefined")

pokemon = pb.pokemon(input("Vložte jméno prvního pokemona:"))
type = pb.type_(pokemon.types[0].type.name)

pokemon1 = []
pokemon1.extend((pokemon.name.capitalize(), pokemon.types[0].type.name, pokemon.height, pokemon.weight, pokemon.base_experience, pokemon.stats[0].base_stat, pokemon.stats[1].base_stat, pokemon.stats[2].base_stat, pokemon.stats[3].base_stat, pokemon.stats[4].base_stat, pokemon.stats[5].base_stat))
try:
   pokemon1.extend([type.damage_relations.no_damage_to[0].name])
except:
    pokemon1.extend(["Undefined"])
try:
    pokemon1.extend([type.damage_relations.half_damage_to[0].name])
except:
    pokemon1.extend(["Undefined"])
try:
    pokemon1.extend([type.damage_relations.double_damage_to[0].name])
except:
    pokemon1.extend(["Undefined"])
try:
    pokemon1.extend([type.damage_relations.no_damage_from[0].name])
except:
    pokemon1.extend(["Undefined"])
try:
    pokemon1.extend([type.damage_relations.half_damage_from[0].name])
except:
    pokemon1.extend(["Undefined"])
try:
    pokemon1.extend([type.damage_relations.double_damage_from[0].name])
except:
    pokemon1.extend(["Undefined"])

"""
pokemon = pb.pokemon(input("Vložte jméno druhého pokemona:"))
pokemon2 = []
pokemon2.extend((pokemon.name.capitalize(), pokemon.types[0].type.name, pokemon.height, pokemon.weight, pokemon.base_experience, pokemon.stats[0].base_stat, pokemon.stats[1].base_stat, pokemon.stats[2].base_stat, pokemon.stats[3].base_stat, pokemon.stats[4].base_stat, pokemon.stats[5].base_stat, type.damage_relations.no_damage_to[0].name, type.damage_relations.half_damage_to[0].name, type.damage_relations.double_damage_to[0].name, type.damage_relations.no_damage_from[0].name, type.damage_relations.half_damage_from[0].name, type.damage_relations.double_damage_from[0].name))"""
count = 0

window = Tk()
window.title("Pokemons")
for x in rows:
    lbl = Label(window, text=rows[count])
    lbl.grid(column=0, row=count)
    count +=1
count = 0
for x in pokemon1:
    lbl = Label(window, text=pokemon1[count])
    lbl.grid(column=1, row=count)
    count +=1
count = 0
"""
for x in pokemon2:
    lbl = Label(window, text=pokemon2[count])
    lbl.grid(column=2, row=count)
    count +=1
"""
window.mainloop()

