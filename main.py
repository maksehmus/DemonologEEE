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