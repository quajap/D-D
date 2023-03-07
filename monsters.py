# Define a class to represent a monster
class Monster:
    def __init__(self, name, hit_points, armor_class, attack_bonus, damage_dice):
        self.name = name
        self.hit_points = hit_points
        self.armor_class = armor_class
        self.attack_bonus = attack_bonus
        self.damage_dice = damage_dice

    # Define a method for the monster to make an attack against a character
    def attack(self, character):
        roll = roll_die(20)
        if roll + self.attack_bonus >= character.armor_class:
            damage = roll_dice(*self.damage_dice)
            character.hit_points -= damage
            print(self.name, "hits", character.name, "for", damage, "points of damage!")
        else:
            print(self.name, "misses", character.name)

# Example usage: simulate a combat encounter between a character and a monster
character = Character("Conan", "Human", "Fighter", 16, 14, 12, 10, 8, 6)
monster = Monster("Goblin", 7, 13, 2, (1, 6))

while character.hit_points > 0 and monster.hit_points > 0:
    monster.attack(character)
    if character.hit_points <= 0:
        print("The", monster.name, "has defeated", character.name)
        break
    character.attack(monster)
    if monster.hit_points <= 0:
        print(character.name, "has defeated the", monster.name)
        break
