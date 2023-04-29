import random
from enum import Enum


class DnDStatusEffect(Enum):
    NORMAL = 'normal'
    BLINDED = 'blinded'
    CHARMED = 'charmed'
    DEAFENED = 'deafened'
    FATIGUED = 'fatigued'
    FRIGHTENED = 'frightened'
    GRAPPLED = 'grappled'
    INCAPACITATED = 'incapacitated'
    INVISIBLE = 'invisible'
    PARALYZED = 'paralyzed'
    PETRIFIED = 'petrified'
    POISONED = 'poisoned'
    PRONE = 'prone'
    RESTRAINED = 'restrained'
    STUNNED = 'stunned'
    UNCONSCIOUS = 'unconscious'


class Combatant:
    def __init__(self, name, initiative, status='normal'):
        self.name = name
        self.initiative = initiative
        self.status = status

    def player_initiative(self, initiative_player):
        self.initiative = initiative_player


class Monster:
    def __init__(self, name, size, monster_type, armor_class, hit_points, speed, strength=0, dexterity=0,
                 constitution=0, intelligence=0, wisdom=0, charisma=0, strength_save=0, dexterity_save=0,
                 constitution_save=0, intelligence_save=0, wisdom_save=0, charisma_save=0, skills='none',
                 damage_vulnerabilities='none', damage_resistances='none', damage_immunities='none',
                 condition_immunities='none', senses='', challenge_rating='', actions='', reactions='none',
                 legendary_desc='none', legendary_actions='none', special_abilities='none', spell_list='none',
                 pros='none', status='normal', initiative=0):
        self.name = name
        self.size = size
        self.type = monster_type
        self.armor_class = armor_class
        self.hit_points = hit_points
        self.speed = speed

        self.strength = 0 if strength == '' else int(strength)
        self.dexterity = 0 if dexterity == '' else int(dexterity)
        self.constitution = 0 if constitution == '' else int(constitution)
        self.intelligence = 0 if intelligence == '' else int(intelligence)
        self.wisdom = 0 if wisdom == '' else int(wisdom)
        self.charisma = 0 if charisma == '' else int(charisma)

        self.strength_save = 0 if strength_save == '' else int(strength_save)
        self.dexterity_save = 0 if dexterity_save == '' else int(dexterity_save)
        self.constitution_save = 0 if constitution_save == '' else int(constitution_save)
        self.intelligence_save = 0 if intelligence_save == '' else int(intelligence_save)
        self.wisdom_save = 0 if wisdom_save == '' else int(wisdom_save)
        self.charisma_save = 0 if charisma_save == '' else int(charisma_save)

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

        self.pros = pros
        self.status = status
        self.initiative = initiative

    def roll_initiative(self):
        self.initiative = random.randint(1, 20) + self.dexterity

    def cast_spell(self):
        pass


