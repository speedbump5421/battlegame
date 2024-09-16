""" Hello I added 2 more characters since i was unable to
finish this chalange during the work shop"""


wizard = "Wizard"
wizard_hp = 70
wizard_damage = 150

elf = "Elf"
elf_hp = 100
elf_damge = 100

human = "Human"
human_hp = 150
human_damage = 20

dwarf = "Dwarf"
dwarf_hp = 140
dwarf_damage = 30

orc = "Orc"
orc_hp = 200
orc_damage = 140

dragon_hp = 300
dragon_damage = 50

while True:
    print("1)   Wizard")
    print("2)   Elf")
    print("3)   Human")
    print("4)   Dwarf")
    print("5)   Orc")

    choice = int(input("Chose your character: "))

    if choice == 1:
        character = wizard
        my_damage = wizard_damage
        my_hp = wizard_hp
        break
    if choice == 2:
        character = elf
        my_damage = elf_damge
        my_hp = elf_hp
        break
    if choice == 3:
        character = human
        my_damage = human_damage
        my_hp = human_hp
        break
    if choice == 4:
        character = dwarf
        my_damage = dwarf_damage
        my_hp = dwarf_hp
        break
    if choice == 5:
        character = orc
        my_damage = orc_damage
        my_hp = orc_hp
        break
    print("")
    print("Unknown Character")
    print("Chose your character: ")

print("")
print("You have chosen the character:", character)
print("Health:", my_hp)
print("Damge:", my_damage)
print("")

while True:

    dragon_hp = dragon_hp - my_damage
    print("The", character, "damaged the Dragon!")
    print("The Dragon's hitpoints are now", dragon_hp)
    print("")
    if dragon_hp <= 0:
        print("The dragon has lost the battle.")
        break

    my_hp = my_hp - dragon_damage
    print("The Dragon strikes back at", character)
    print("The", character, "'s hitpoints are now:", my_hp)
    print("")
    if my_hp <= 0:
        print("The", character, "has lost the battle")
        break
