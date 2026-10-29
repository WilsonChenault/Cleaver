import random

class Armor:
    def __init__(self, nametag, tier, acbonus, reduction_dice):
        self.nametag = nametag
        self.tier = tier
        self.acbonus = acbonus
        self.reduction_dice = reduction_dice

    def damage_reduction(self):
        dmg_reduc = random.randint(1, self.reduction_dice)

# Defining all Tier I armors
small_shield = Armor('Small Shield', 1, 1, 2)
left_greave = Armor('Left Greave', 1, 0, 2)
right_greave = Armor('Right Greave', 1, 0, 2)
small_helm = Armor('Small Helm', 1, 0, 3)
left_armguard = Armor('Left Armguard', 1, 0, 3)
right_armguard = Armor('Right Armguard', 1, 0, 3)
broad_belt = Armor('Broadbelt', 1, 0, 2)
left_shoulderguard = Armor('Left Shoulderguard', 1, 0, 2)
right_shoulderguard = Armor('Right Shoulderguard', 1, 0, 2)

armors_tier1 = [small_shield, left_greave, right_greave, small_helm, left_armguard, right_armguard,
                broad_belt, left_shoulderguard, right_shoulderguard]