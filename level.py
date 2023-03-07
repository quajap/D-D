# Define a class to represent a character's level
class Level:
    def __init__(self, level):
        self.level = level
        self.max_hit_points = roll_die(10) + 8 + ((level - 1) * 5)

    # Define a method to level up the character
    def level_up(self, character):
        character.level += 1
        character.max_hit_points += roll_die(10) + 8
        print(character.name, "has leveled up to level", character.level)

# Example usage: create a character and level them up
character = Character("Elric", "Elf", "Wizard", 12, 14, 10, 16, 8, 6)
level = Level(character.level)
print(character.name, "is currently level", character.level)
print(character.name, "has a max hit points of", character.max_hit_points)
level.level_up(character)
print(character.name, "is now level", character.level)
print(character.name, "has a new max hit points of", character.max_hit_points)
