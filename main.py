import random

class Tool:
    def __init__(self, name, evidence_type, max_uses):
        self.name = name
        self.evidence_type = evidence_type
        self.max_uses = max_uses
        self.uses_left = max_uses
        self.reading = ""
        
    def trigger_evidence(self, player_distance, has_evidence_trait):
        # Values for EMF depends on sa distance ng ghost and if the ghost is may ganong evidence 
        if self.evidence_type == "EMF Level 5":
            if player_distance == 0:
                if has_evidence_trait:
                    self.reading = "EMF Level 5! (Max Danger)"
                else:
                    self.reading = "EMF Level 4 (Strong presence, but not max)"
            elif player_distance == 1:
                self.reading = "EMF Level 3 (Getting close)"
            elif player_distance == 2:
                self.reading = "EMF Level 2 (Faint signal)"
            else:
                self.reading = "EMF Level 1 (Normal)"

        elif self.evidence_type == "Freezing Temps":
            if player_distance == 0:
                if has_evidence_trait:
                    self.reading = f"{round(random.uniform(-5.0, -0.1), 1)} C (Freezing!)"
                else:
                    self.reading = f"{round(random.uniform(1.0, 10.0), 1)} C (Chilly, but not freezing)"
            else:
                self.reading = f"{round(random.uniform(15.0, 25.0), 1)} C (Normal)"

        elif self.evidence_type == "Spirit Box":
            # Spirit Box works from anywhere if the ghost has the trait
            if has_evidence_trait:
                self.reading = random.choice(["'Eeeh...'", "'D I E'"])
            else:
                self.reading = "*Static noise*"
                
        else:
            # Logic for Inscription, Prints, Wither
            if player_distance == 0 and has_evidence_trait:
                if self.evidence_type == "Inscription":
                    self.reading = "Scribbles and dark symbols appeared!"
                elif self.evidence_type == "Prints":
                    self.reading = "Glowing handprints detected!"
                elif self.evidence_type == "Wither":
                    self.reading = "The plant immediately withered and died!"
            else:
                if self.evidence_type == "Inscription": self.reading = "Pages remain blank."
                elif self.evidence_type == "Prints": self.reading = "No prints found."
                elif self.evidence_type == "Wither": self.reading = "Plant is healthy."

class Ghost:
    # Class Attribute: 3 unique combination of evidences per ghost
    GHOST_JOURNAL = {
        "Aswang": ["EMF Level 5", "Inscription", "Wither"],
        "Demon": ["EMF Level 5", "Freezing Temps", "Prints"],
        "Doppelganger": ["Freezing Temps", "Inscription", "Spirit Box"],
        "Ravager": ["EMF Level 5", "Inscription", "Spirit Box"],
        "Revenant": ["EMF Level 5", "Freezing Temps", "Inscription"],
        "Entity": ["Prints", "Spirit Box", "Freezing Temps"],
        "Ghoul": ["Freezing Temps", "Spirit Box", "Wither"],
        "Shadow": ["EMF Level 5", "Inscription", "Wither"], 
        "Vesper": ["Inscription", "Prints", "Wither"]
    }

    def __init__(self, ghost_type, haunt_room):
        # Method 1
        self.ghost_type = ghost_type
        self.evidences = Ghost.GHOST_JOURNAL[ghost_type]
        self.current_room = haunt_room

    def interact_with_tool(self, tool_object, player_room, floor_layout):
        # Method 2
        if tool_object.uses_left is not None and tool_object.uses_left <= 0:
            #Checks if the tool still has uses left
            print(f"\n> The {tool_object.name} has no uses left.")
            return

        player_index = floor_layout.index(player_room)
        ghost_index = floor_layout.index(self.current_room)
        distance = abs(player_index - ghost_index)

        has_trait = tool_object.evidence_type in self.evidences
        #Checks if the ghost has this attribute/trait
        
        print(f"\n> You observe the {tool_object.name} in the {player_room}...")
        
        if tool_object.uses_left is not None:
            tool_object.uses_left -= 1
        
        tool_object.trigger_evidence(player_distance=distance, has_evidence_trait=has_trait)
        
        print(f"> READING: {tool_object.reading}")

    @staticmethod
    def get_evidence_for(ghost_type):
        #return ung specific type
        #hindi nagamit
        return Ghost.GHOST_JOURNAL.get(ghost_type, "Ghost type not found in journal.")

    @staticmethod
    def get_all_types():
        #return lahat ng type
        #ginamit sa definition ng ghost names sa play_game()
        return list(Ghost.GHOST_JOURNAL.keys())

    @staticmethod
    def display_full_journal():
        #display full journal - lahat ng types saka evidences
        #sa play game ginamit for view journal move
        print("\n=== FULL GHOST JOURNAL ===")
        for ghost, evidences in Ghost.GHOST_JOURNAL.items():
            print(f"- {ghost:12}: {', '.join(evidences)}")


def play_game():
    #multiplier ng sanity deduction ung floor_num
    #minus 2 sanity for moving, minus 5 for item use, minus 25 for wrong guess (nagaapply ung multiplier)

    floors = {
        1: {"name": "1st Floor", "rooms": ["VLC", "LC", "Lobby"]},
        2: {"name": "2nd Floor", "rooms": ["Lecture Room", "Lobby", "Server Room", "Admin Room"]},
        3: {"name": "3rd Floor", "rooms": ["ALab", "BeLab", "Wellness Room", "Inventory", "Smart iLab"]}
    }

    ghost_names = Ghost.get_all_types()

    print("=======================================")
    print("              DemonologEEE             ")
    print("=======================================")

    for current_floor_num in range(1, 4):
        floor_data = floors[current_floor_num]
        floor_name = floor_data["name"]
        floor_layout = floor_data["rooms"]

        actual_ghost_type = random.choice(ghost_names)
        ghost_haunt_room = random.choice(floor_layout)
        hidden_ghost = Ghost(actual_ghost_type, ghost_haunt_room)
        
        player_room = floor_layout[0] 
        sanity = 100

        inventory = [
            Tool("EMF Reader", "EMF Level 5", max_uses=None),
            Tool("Spirit Box", "Spirit Box", max_uses=1),
            Tool("Thermometer", "Freezing Temps", max_uses=None),
            Tool("Spirit Book", "Inscription", max_uses=2),
            Tool("Blacklight", "Prints", max_uses=1),
            Tool("Flower Pot", "Wither", max_uses=2)
        ]

        print(f"\n=======================================")
        print(f"         ENTERING: {floor_name.upper()}        ")
        print(f"=======================================")
    

        floor_cleared = False

        while not floor_cleared:
            print(f"\n--- LOCATION: {floor_name} - {player_room} | SANITY: {sanity}% ---")
            print("[1] Move Room  |  [2] Use Item  |  [3] Guess Entity  |  [4] View Journal  |  [5] Quit")
            
            choice = input("Enter choice (1-5): ")

            if choice == '1':
                print(f"\n--- {floor_name.upper()} MAP ---")
                for i in range(len(floor_layout)):
                    print(f"[{i+1}] {floor_layout[i]}")
                
                if True:
                    room_choice = int(input(f"Where do you want to go? (1-{len(floor_layout)}): "))
                    if 1 <= room_choice <= len(floor_layout):
                        player_room = floor_layout[room_choice - 1]
                        print(f"\nYou walked to the {player_room}.")
                        sanity -= 2 * current_floor_num
                        print(f"> Moving drained {2 * current_floor_num} sanity.")
                    else:
                        print("Invalid room choice. Please enter a valid number.")

            elif choice == '2':
                print("\n--- INVENTORY ---")
                for i in range(len(inventory)):
                    tool = inventory[i]
                    use_display = "Unli uses" if tool.uses_left is None else f"{tool.uses_left} uses left"
                    print(f"[{i+1}] {tool.name} ({use_display})")
                
                if True:
                    item_choice = int(input("Select an item to use (1-6): "))
                    if 1 <= item_choice <= 6:
                        selected_tool = inventory[item_choice - 1]
                        hidden_ghost.interact_with_tool(selected_tool, player_room, floor_layout)
                        sanity -= 5 * current_floor_num
                        print(f"> Using an item drained {5 * current_floor_num} sanity.")
                    else:
                        print("Invalid item choice. Please enter a valid number.")

            elif choice == '3':
                print("\n--- GHOST JOURNAL ---")
                for i in range(len(ghost_names)):
                    print(f"[{i + 1}] {ghost_names[i]}")

                guess_choice = int(input("Who is haunting this floor? (1-9): "))
                if 1 <= guess_choice <= 9:
                    guessed_ghost = ghost_names[guess_choice - 1]   #minus 1 para match sa list index
                    
                    if guessed_ghost == actual_ghost_type:
                        print(f"\nCORRECT! You successfully exorcised the {actual_ghost_type} from the {ghost_haunt_room}.")
                        floor_cleared = True 
                    else:
                        sanity -= 25 * current_floor_num
                        print(f"\nWRONG! The entity is angered by your false claim!")
                        print(f"> The attack drained {25 * current_floor_num} sanity.")
                else:
                    print("Invalid ghost choice. Please enter a valid number.")

            elif choice == '4':
                Ghost.display_full_journal() #print journal, eto ung nasa static method

            elif choice == '5':
                print("\nYou ran out of the EEE building in fear. GAME OVER.")
                return 

            if sanity <= 0:
                print("\nYour sanity reached 0. The darkness consumes you. GAME OVER.")
                return

    print("\n===========================================")
    print("                YOU SURVIVED!               ")
    print(" You cleared all floors of the EEE building.    ")
    print("           The ghosts are gone!        ")
    print("=============================================")


play_game()