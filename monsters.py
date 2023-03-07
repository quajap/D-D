# Define a class to represent a D&D character
class Character:
    def __init__(self, name, race, class_, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.name = name
        self.race = race
        self.class_ = class_
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

    # Define a method to calculate the character's hit points
    def calculate_hit_points(self):
        if self.class_ == "Fighter":
            return 10 + self.constitution
        elif self.class_ == "Wizard":
            return 6 + self.constitution
        else:
            return 8 + self.constitution

# Example usage: create a new character and display their hit points
new_character = Character("Gandalf", "Human", "Wizard", 10, 12, 8, 18, 16, 14)
hit_points = new_character.calculate_hit_points()
print(new_character.name, "has", hit_points, "hit points.")
