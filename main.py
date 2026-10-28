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

    def init(self, ghost_type, haunt_room):
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
        #Calculate the distance between the player and the ghost's room

        has_trait = tool_object.evidence_type in self.evidences
        #Checks if the ghost has this attribute/trait

        print(f"\n> You observe the {tool_object.name} in the {player_room}...")

        if tool_object.uses_left is not None:
            tool_object.uses_left -= 1

        tool_object.trigger_evidence(player_distance=distance, has_evidence_trait=has_trait)

        print(f"> READING: {tool_object.reading}")
