import random
from items import armors, weapons, skills

# Character data structure
class Character:
    def __init__(self, nametag, might, agility, toughness, comeliness, maxhp,
                 lifepoints, skill, weapon, armor1, armor2, tier, index):
        self.name = nametag
        self.might = might
        self.agility = agility
        self.toughness = toughness
        self.comeliness = comeliness
        self.maxhp = maxhp
        self.lifepoints = lifepoints
        self.skill = skill
        self.weapon = weapon
        self.armor1 = armor1
        self.armor2 = armor2
        self.tier = tier
        self.index = index

# Importing list of names
with open('names/lastnamelist.txt') as file:
    last_names = [line.strip() for line in file]

with open("names/firstnamelist.txt") as file:
    first_names = [line.strip() for line in file]

# Attribute dictionaries
attributeList = {0: 'Might', 1: 'Agility', 2: 'Toughness', 3: 'Comeliness', 4: 'Hit Points'}
attributeBonus = {1: -5, 2: -5, 3: -4, 4: -4, 5: -3, 6: -3, 7: -2, 8: -2, 9: -1,
                  10: -1, 11: 0, 14: 0, 15: 1, 16: 1, 17: 2, 18: 2, 19: 3, 20: 3,
                  21: 4, 22: 4, 23: 5, 24: 5}

# Initialize character index, generate character functions
char_index = 0
character_list = []

def generate_name() -> str:
    # Name generation
    first_index, last_index = (random.randint(0, len(first_names)),
                               random.randint(0, len(first_names)))
    first_name = first_names[first_index]
    last_name = last_names[last_index]
    name = f'{first_name} {last_name}'

    return name

def generate_attributes() -> list[int]:
    # Select specialty attribute
    specialty = random.randint(0, 4)
    attribute_list = []
    for i in range(5):
        score = random.choices(range(1, 5, ), k=5)
        attribute_list.append(score)

    # Adding 10 to Life Points
    attribute_list[4] += 10

    return attribute_list

def generate_weapon(tier) -> weapons.Weapon:
    weapon_list = weapons.weapon_list(tier)
    weapon_index = random.randint(0, len(weapon_list))
    weapon = weapon_list(weapon_index)
    return weapon

def generate_armor(tier) -> armors.Armor:
    1

def generate_new_character(tier):
    # Make character index a global variable and count up for new character
    global char_index
    char_index += 1

    # Call generation functions
    name = generate_name()
    attributes = generate_attributes
    weapon = generate_weapon