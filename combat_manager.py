import csv
import tkinter as tk

class CombatManager:
    def __init__(self, master, combatants):
        self.master = master
        self.combatants_list = combatants
        
        self.initalize_gui(master)
        
    def initalize_gui(self, master):
        master.title("DnD Combat Manager")

        # Create a listbox to display the names of all monsters
        self.participant_listbox = tk.Listbox(master, width=25, height=25)
        self.participant_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        for participant in self.combatants_list:
            self.participant_listbox.insert(tk.END, participant.name)
