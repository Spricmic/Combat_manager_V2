import tkinter as tk
import csv
import textwrap
from combat_classes import Monster
from combat_classes import Combatant
from combat_manager import CombatManager

MONSTER_LISTBOX = 1
BATTLE_LISTBOX = 2


class SetupGUI:
    def __init__(self, master):
        self.master = master
        self.monster_list = []
        self.battle_participants = []
        master.title("DnD Combat Setup")

        # Create a label and entry widget to search for monsters
        search_frame = tk.Frame(master)
        search_frame.pack(side=tk.TOP, fill=tk.X)
        search_label = tk.Label(search_frame, text="Search for monster:")
        search_label.pack(side=tk.LEFT, padx=10, pady=10)
        self.search_entry = tk.Entry(search_frame, width=25)
        self.search_entry.pack(side=tk.LEFT, padx=5, pady=10)
        search_button = tk.Button(search_frame, text="Search", command=self.search_monster)
        search_button.pack(side=tk.LEFT, padx=5, pady=10)

        # Create a listbox to display the names of all monsters
        self.monster_listbox = tk.Listbox(master, width=25, height=25)
        self.monster_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a listbox to display the names of monsters in the battle
        self.battle_listbox = tk.Listbox(master, width=25, height=25)
        self.battle_listbox.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Create a listbox to display the stats of a preselected monster
        self.stats_listbox = tk.Listbox(master, width=200, height=25)
        self.stats_listbox.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        # Read the names of all monsters from monster.csv and add them to the listbox
        with open('monsters.csv', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=';')
            for row in csv_reader:
                monster = Monster(row['name'], row['size'], row['type'], row['armor_class'],
                                  row['hit_points'], row['speed'], row['strength'],
                                  row['dexterity'], row['constitution'], row['intelligence'],
                                  row['wisdom'], row['charisma'],
                                  strength_save=row['strength_save'], dexterity_save=row['dexterity_save'],
                                  constitution_save=row['constitution_save'],
                                  intelligence_save=row['intelligence_save'],
                                  wisdom_save=row['wisdom_save'], charisma_save=row['charisma_save'],
                                  skills=row['skills'],
                                  damage_vulnerabilities=row['damage_vulnerabilities'],
                                  damage_resistances=row['damage_resistances'],
                                  damage_immunities=row['damage_immunities'],
                                  condition_immunities=row['condition_immunities'],
                                  senses=row['senses'], challenge_rating=row['challenge_rating'],
                                  actions=row['actions'], reactions=row['reactions'],
                                  legendary_desc=row['legendary_desc'], legendary_actions=row['legendary_actions'],
                                  special_abilities=row['special_abilities'], spell_list=row['spell_list'],
                                  pros=row['pros'])

                self.monster_list.append(monster)
                self.monster_listbox.insert(tk.END, monster.name)

        # Create a button to add the selected monster to the battle list
        self.add_button = tk.Button(master, text="Add Monster", command=self.add_to_battle)
        self.add_button.pack(side="left", padx=10, pady=10)

        # create a button to add a player to the battle
        self.add_player_button = tk.Button(master, text="Add Player", command=self.add_player)
        self.add_player_button.pack(side="left", padx=10, pady=10)

        # Create a button to remove the selected monster from the battle list
        self.remove_button = tk.Button(master, text="Remove", command=self.remove_from_battle)
        self.remove_button.pack(side="right", padx=10, pady=10)

        # Create a button to start the battle
        self.start_button = tk.Button(master, text="Start", command=self.start_battle)
        self.start_button.pack(side="right", padx=10, pady=10)

        # Create a button to start the battle
        self.choose_setup_button = tk.Button(master, text="Choose from setup", command=self.choose_battle_setup)
        self.choose_setup_button.pack(side="left", padx=10, pady=10)

        # Create a button to safe the battle setup to a file
        self.safe_button = tk.Button(master, text="Safe", command=self.safe_battle_setup)
        self.safe_button.pack(side="left", padx=10, pady=10)

        self.check_monster_selection()
        self.check_battle_selection()

    def display_monster_stats(self, monster_index, source):
        """
        Find monster object with the given index.
        and display the stats of the monster at this index.
        :param monster_index: index of the monster in the .csv file
        :param source: the source is either MONSTER_LISTBOX or BATTLE_LISTBOX
        :return: None
        """
        # Find the Monster object with the given index
        if source == MONSTER_LISTBOX:
            monster = self.monster_list[monster_index]
        elif source == BATTLE_LISTBOX:
            monster = self.battle_participants[monster_index]
        else:
            print("ERROR: Monster not found!")
            pass

        # If the Monster object was found, display its stats
        if monster:
            self.stats_listbox.delete(0, tk.END)
            self.stats_listbox.insert(tk.END, "Name: {}".format(monster.name))
            self.stats_listbox.insert(tk.END, "Size: {}".format(monster.size))
            self.stats_listbox.insert(tk.END, "Type: {}".format(monster.type))
            self.stats_listbox.insert(tk.END, "Armor Class: {}".format(monster.armor_class))
            self.stats_listbox.insert(tk.END, "Hit Points: {}".format(monster.hit_points))
            self.stats_listbox.insert(tk.END, "Speed: {}".format(monster.speed))
            self.stats_listbox.insert(tk.END, "Challenge rating: {}".format(monster.challenge_rating))
            self.stats_listbox.insert(tk.END, "Strength: {}".format(monster.strength))
            self.stats_listbox.insert(tk.END, "Dexterity: {}".format(monster.dexterity))
            self.stats_listbox.insert(tk.END, "Constitution: {}".format(monster.constitution))
            self.stats_listbox.insert(tk.END, "Intelligence: {}".format(monster.intelligence))
            self.stats_listbox.insert(tk.END, "Wisdom: {}".format(monster.wisdom))
            self.stats_listbox.insert(tk.END, "Charisma: {}".format(monster.charisma))
            self.stats_listbox.insert(tk.END, "Strength Save: {}".format(monster.strength_save))
            self.stats_listbox.insert(tk.END, "Dexterity Save: {}".format(monster.dexterity_save))
            self.stats_listbox.insert(tk.END, "Constitution Save: {}".format(monster.constitution_save))
            self.stats_listbox.insert(tk.END, "Intelligence Save: {}".format(monster.intelligence_save))
            self.stats_listbox.insert(tk.END, "Wisdom Save: {}".format(monster.wisdom_save))
            self.stats_listbox.insert(tk.END, "Charisma Save: {}".format(monster.charisma_save))
            self.stats_listbox.insert(tk.END, "Strength Saving Throw: {}".format(monster.strength_save))
            self.stats_listbox.insert(tk.END, "Dexterity Saving Throw: {}".format(monster.dexterity_save))
            self.stats_listbox.insert(tk.END, "Constitution Saving Throw: {}".format(monster.constitution_save))
            self.stats_listbox.insert(tk.END, "Intelligence Saving Throw: {}".format(monster.intelligence_save))
            self.stats_listbox.insert(tk.END, "Wisdom Saving Throw: {}".format(monster.wisdom_save))
            self.stats_listbox.insert(tk.END, "Charisma Saving Throw: {}".format(monster.charisma_save))
            self.stats_listbox.insert(tk.END, "Skills: {}".format(monster.skills))
            self.stats_listbox.insert(tk.END, "Damage Vulnerabilities: {}".format(monster.damage_vulnerabilities))
            self.stats_listbox.insert(tk.END, "Damage Resistances: {}".format(monster.damage_resistances))
            self.stats_listbox.insert(tk.END, "Damage Immunities: {}".format(monster.damage_immunities))
            self.stats_listbox.insert(tk.END, "Condition Immunities: {}".format(monster.condition_immunities))
            self.stats_listbox.insert(tk.END, "Senses: {}".format(monster.senses))
            self.stats_listbox.insert(tk.END, "Actions: {}".format(monster.actions))
            self.stats_listbox.insert(tk.END, "Reactions: {}".format(monster.reactions))
            self.stats_listbox.insert(tk.END, "Legendary Description: {}".format(monster.legendary_desc))
            self.stats_listbox.insert(tk.END, "Legendary Actions: {}".format(monster.legendary_actions))
            self.stats_listbox.insert(tk.END, "Special Abilities: {}".format(monster.special_abilities))
            self.stats_listbox.insert(tk.END, "Spell List: {}".format(monster.spell_list))
            self.stats_listbox.insert(tk.END, "Pros: {}".format(monster.pros))
            self.stats_listbox.insert(tk.END, "Status: {}".format(monster.status))
            self.stats_listbox.insert(tk.END, "Initiative: {}".format(monster.initiative))

        else:
            # If the Monster object was not found, display an error message
            self.stats_listbox.delete(0, tk.END)
            self.stats_listbox.insert(tk.END, "Error: Monster not found")

    def check_monster_selection(self):
        """
        checks if a monster has been choosen in the monster.listbox (left side of gui)
        """
        selection = self.monster_listbox.curselection()
        if selection:
            monster_index = selection[0]
            self.display_monster_stats(monster_index, MONSTER_LISTBOX)
        self.master.after(500, self.check_monster_selection)

    def check_battle_selection(self):
        """
        checks if a monster has been choosen in the battle.listbox (right side of gui)
        """
        selection = self.battle_listbox.curselection()
        if selection:
            monster_index = selection[0]
            self.display_monster_stats(monster_index, BATTLE_LISTBOX)
        self.master.after(500, self.check_battle_selection)

    def add_to_battle(self):
        """
        inizalise the Monster class by the date of the selcted monster.
        Add the Monster to battle_participants list
        """
        selection = self.monster_listbox.curselection()
        if selection:
            index = selection[0]
            monster_class = self.monster_list[index]
            self.battle_participants.append(monster_class)

            # Add the monster name to the battle listbox
            self.battle_listbox.insert(tk.END, monster_class.name)

    def remove_from_battle(self):
        """
        remove the monster from battle_listbox and battle_participants
        """
        # Get the selected monster name from the battle listbox
        selection = self.battle_listbox.curselection()
        if selection:
            # Remove the monster name from the battle listbox
            self.battle_listbox.delete(selection)
            del self.battle_participants[selection[0]]

    def search_monster(self):
        search_term = self.search_entry.get().lower()
        if not search_term:
            return
        self.monster_listbox.selection_clear(0, tk.END)
        for i, monster in enumerate(self.monster_list):
            if search_term in monster.name.lower():
                self.monster_listbox.selection_set(i)
                self.monster_listbox.see(i)
                break

    def safe_battle_setup(self):
        pass

    def choose_battle_setup(self):
        pass

    def start_battle(self):
        """
        rolls initiative for all the monsters
        initalize the combat_manger
        :Arg passing_function: Function to execute with self.battle_participants as argument
        """
        for participant in self.battle_participants:
            if isinstance(participant, Monster):
                participant.roll_initiative()
            else:
                pass
        # Destroy the current window
        if self.master:
            self.master.after_cancel(self.check_monster_selection)
            self.master.after_cancel(self.check_battle_selection)
        self.master.destroy()
        # Create a new window for the combat manager
        root = tk.Tk()
        combat_gui = CombatManager(root, self.battle_participants)
        root.mainloop()

    def add_player(self):
        """
        add a new player to the player_list
        """
        # Create a new window for the player setup
        pass

root = tk.Tk()
setup_gui = SetupGUI(root)
root.mainloop()
