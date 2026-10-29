import random

class Weapon:
    def __init__(self, nametag, tier, die_count, dice, bonus_dmg):
        self.nametag = nametag
        self.tier = tier
        self.die_count = die_count
        self.dice = dice
        self.bonus_dmg = bonus_dmg

    def roll_damage(self) -> int:
        damage = random.choices(range(1, self.dice), k = self.die_count)
        return damage


# List of all Tier I weapons
dagger = Weapon('Dagger', 1, 2, 4, 0)
small_sword = Weapon('Small Sword', 1, 3, 4, 0)
small_mace = Weapon('Small Mace', 1, 1, 8, 0)
small_hammer = Weapon('Small Hammer', 1, 1, 6, 0)
short_spear = Weapon('Short Spear', 1, 3, 4, 0)
mailed_fist = Weapon('Mailed Fist', 1, 1, 4, 0)
small_axe = Weapon('Small Axe', 1, 2, 4, 0)
club = Weapon('Club', 1, 1, 6, 0)
small_trident = Weapon('Small Trident', 1, 1, 8, 0)
cleaver = Weapon('Cleaver', 1, 1, 10, 0)

# Tier I weapons list
weapons_tier1 = [dagger, small_sword, small_mace, small_hammer, short_spear, mailed_fist,
                 small_axe, club, small_trident, cleaver]
weapons_tier2 = []
weapons_tier3 = []

weapons_dict = {1: weapons_tier1, 2: weapons_tier2, 3: weapons_tier3}

def weapon_list(tier):
    return weapons_dict[tier]