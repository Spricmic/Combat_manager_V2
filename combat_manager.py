import random


class Combatant:
    def __init__(self, name, initiative, status):
        self.name = name
        self.initiative = initiative
        self.status = status

    def roll_initiative(self, initiative_player):
        self.initiative = initiative_player


class Monster:
    def __init__(self, name, initiative, status, size, pros, monster_type, armor_class, hit_points, speed, strength,
                 dexterity,
                 constitution, intelligence, wisdom, charisma, strength_save, dexterity_save, constitution_save,
                 intelligence_save, wisdom_save, charisma_save, skills, damage_vulnerabilities, damage_resistances,
                 damage_immunities, condition_immunities, senses, challenge_rating, actions, reactions, legendary_desc,
                 legendary_actions, special_abilities, spell_list):
        self.name = name
        self.initiative = initiative
        self.status = status
        self.size = size
        self.pros = pros
        self.type = monster_type
        self.armor_class = armor_class
        self.hit_points = hit_points
        self.speed = speed
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.strength_save = strength_save
        self.dexterity_save = dexterity_save
        self.constitution_save = constitution_save
        self.intelligence_save = intelligence_save
        self.wisdom_save = wisdom_save
        self.charisma_save = charisma_save
        self.skills = skills
        self.damage_vulnerabilities = damage_vulnerabilities
        self.damage_resistances = damage_resistances
        self.damage_immunities = damage_immunities
        self.condition_immunities = condition_immunities
        self.senses = senses
        self.challenge_rating = challenge_rating
        self.actions = actions
        self.reactions = reactions
        self.legendary_desc = legendary_desc
        self.legendary_actions = legendary_actions
        self.special_abilities = special_abilities
        self.spell_list = spell_list

    def initiative(self):
        self.initiative = random.randint(1, 20) + self.dexterity
