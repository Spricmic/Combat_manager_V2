import tkinter as tk
import csv
from combat_classes import Monster
from combat_classes import Combatant

MONSTER_LISTBOX = 1
BATTLE_LISTBOX = 2

class CombatGUI:
    def __init__(self, master):
        self.master = master
        self.monster_list = []
        self.battle_participants = []
        master.title("DnD Combat Manager")

        # Create a listbox to display the names of all monsters
        self.monster_listbox = tk.Listbox(master, width=25, height=25)
        self.monster_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a listbox to display the names of monsters in the battle
        self.battle_listbox = tk.Listbox(master, width=25, height=25)
        self.battle_listbox.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Create a listbox to display the stats of a preselected monster
        self.stats_listbox = tk.Listbox(master, width=100, height=25)
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
        self.add_button = tk.Button(master, text="Add", command=self.add_to_battle)
        self.add_button.pack()

        # Create a button to remove the selected monster from the battle list
        self.remove_button = tk.Button(master, text="Remove", command=self.remove_from_battle)
        self.remove_button.pack()

        # Create a button to safe the battle setup to a file
        self.safe_button = tk.Button(master, text="Safe", command=self.safe_battle_setup)
        self.safe_button.pack()

        # Create a button to start the battle
        self.start_button = tk.Button(master, text="Start", command=self.start_battle)
        self.start_button.pack()

        self.master.after(500, self.check_monster_selection)
        self.master.after(500, self.check_battle_selection)

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
            self.stats_listbox.insert(tk.END, "Strength: {}".format(monster.strength))
            self.stats_listbox.insert(tk.END, "Dexterity: {}".format(monster.dexterity))
            self.stats_listbox.insert(tk.END, "Constitution: {}".format(monster.constitution))
            self.stats_listbox.insert(tk.END, "Intelligence: {}".format(monster.intelligence))
            self.stats_listbox.insert(tk.END, "Wisdom: {}".format(monster.wisdom))
            self.stats_listbox.insert(tk.END, "Charisma: {}".format(monster.charisma))
            self.stats_listbox.insert(tk.END, "Challenge Rating: {}".format(monster.challenge_rating))
        else:
            # If the Monster object was not found, display an error message
            self.stats_listbox.delete(0, tk.END)
            self.stats_listbox.insert(tk.END, "Error: Monster not found")

    def check_monster_selection(self):
        selection = self.monster_listbox.curselection()
        if selection:
            monster_index = selection[0]
            self.display_monster_stats(monster_index, MONSTER_LISTBOX)
        self.master.after(500, self.check_monster_selection)

    def check_battle_selection(self):
        selection = self.battle_listbox.curselection()
        if selection:
            monster_index = selection[0]
            self.display_monster_stats(monster_index, BATTLE_LISTBOX)
        self.master.after(500, self.check_battle_selection)

    def add_to_battle(self):
        # Get the selected monster name from the monster listbox
        selection = self.monster_listbox.curselection()
        if selection:
            index = selection[0]
            monster_class = self.monster_list[index]
            self.battle_participants.append(monster_class)

            # Add the monster name to the battle listbox
            self.battle_listbox.insert(tk.END, monster_class.name)


    def remove_from_battle(self):
        # Get the selected monster name from the battle listbox
        selection = self.battle_listbox.curselection()
        if selection:
            # Remove the monster name from the battle listbox
            self.battle_listbox.delete(selection)

    def safe_battle_setup(self):
        pass

    def start_battle(self):
        # Get the names of all monsters in the battle
        monster_names = [self.battle_listbox.get(idx) for idx in range(self.battle_listbox.size())]

        # TODO: add code to get the stats of the selected monsters and start the battle


root = tk.Tk()
gui = CombatGUI(root)
root.mainloop()
