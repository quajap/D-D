# Define a class to represent a magic item
class MagicItem:
    def __init__(self, name, description, rarity, effects):
        self.name = name
        self.description = description
        self.rarity = rarity
        self.effects = effects

    # Define a method to apply the effects of the magic item to a character
    def apply_effects(self, character):
        for effect in self.effects:
            effect.apply(character)

# Define a class to represent a magic item effect
class MagicItemEffect:
    def __init__(self, attribute, modifier):
        self.attribute = attribute
        self.modifier = modifier

    # Define a method to apply the effect to a character
    def apply(self, character):
        setattr(character, self.attribute, getattr(character, self.attribute) + self.modifier)

# Example usage: create a magic item and apply its effects to a character
magic_item = MagicItem("Ring of Protection", "A gold ring with a small ruby in the center.", "Rare", [
    MagicItemEffect("armor_class", 1)
])
character = Character("Conan", "Human", "Fighter", 16, 14, 12, 10, 8, 6)
magic_item.apply_effects(character)
print(character.name, "has equipped the", magic_item.name)
print(character.name, "now has an armor class of", character.armor_class)
