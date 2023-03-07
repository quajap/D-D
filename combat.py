# Define a function to simulate combat between two characters
def combat(attacker, defender):
    print(attacker.name, "attacks", defender.name)
    attack_roll = roll_die(20) + attacker.attack_bonus
    if attack_roll >= defender.armor_class:
        damage_roll = roll_die(attacker.damage_dice) + attacker.damage_bonus
        defender.hit_points -= damage_roll
        print(attacker.name, "hits for", damage_roll, "damage!")
        if defender.hit_points <= 0:
            print(defender.name, "has been defeated!")
    else:
        print(attacker.name, "misses!")

# Example usage: create two characters and simulate combat between them
character1 = Character("Drizzt", "Elf", "Ranger", 18, 16, 14, 10, 12, 8)
character2 = Character("Bruenor", "Dwarf", "Fighter", 16, 14, 16, 8, 10, 12)
print(character1.name, "has", character1.hit_points, "hit points")
print(character2.name, "has", character2.hit_points, "hit points")
while character1.hit_points > 0 and character2.hit_points > 0:
    combat(character1, character2)
    if character2.hit_points > 0:
        combat(character2, character1)
print("Combat is over!")
