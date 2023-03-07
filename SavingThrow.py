# Define a class to represent a character's saving throw
class SavingThrow:
    def __init__(self, ability, bonus):
        self.ability = ability
        self.bonus = bonus

    # Define a method to make a saving throw against a DC
    def make_save(self, dc):
        roll = roll_die(20)
        if roll + self.bonus >= dc:
            print("Success!")
            return True
        else:
            print("Failure!")
            return False

# Example usage: simulate a character making a saving throw against a spell
spell_dc = 15
save_bonus = character.wisdom - 2
save = SavingThrow("Wisdom", save_bonus)
if save.make_save(spell_dc):
    print("You resist the spell's effects.")
else:
    print("You are affected by the spell.")

