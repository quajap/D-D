# Define a function to cast a spell
def cast_spell(caster, spell, target):
    print(caster.name, "casts", spell.name, "on", target.name)
    spell_level = caster.spell_slots[spell.level] - 1
    if spell_level >= 0:
        caster.spell_slots[spell.level] = spell_level
        if spell.target_type == "self":
            spell.effect(caster)
            print(caster.name, "is affected by", spell.name)
        elif spell.target_type == "enemy":
            spell.effect(caster, target)
            print(target.name, "is affected by", spell.name)
        elif spell.target_type == "ally":
            spell.effect(caster, target)
            print(target.name, "is affected by", spell.name)
        else:
            print("Invalid target type for spell!")
    else:
        print("Insufficient spell slots to cast spell!")

# Define a class to represent a spell
class Spell:
    def __init__(self, name, level, target_type, effect):
        self.name = name
        self.level = level
        self.target_type = target_type
        self.effect = effect

# Example usage: create a character, some spells, and cast a spell
character = Character("Gandalf", "Human", "Wizard", 16, 14, 12, 18, 10, 8)
fireball = Spell("Fireball", 3, "enemy", lambda caster, target: target.take_damage(roll_die(6) + 5))
heal = Spell("Heal", 1, "ally", lambda caster, target: target.heal(roll_die(8) + 2))
print(character.name, "has", character.spell_slots, "spell slots")
enemy = Character("Goblin", "Goblin", "Fighter", 10, 14, 8, 6, 10, 8)
cast_spell(character, fireball, enemy)
cast_spell(character, heal, character)
