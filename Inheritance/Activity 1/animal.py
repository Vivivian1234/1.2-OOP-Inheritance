
class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.animal_sound = sound

    def make_sound(self):
        print(f'\nA {self.species} makes a {self.animal_sound}ing sound.\n')

    def __str__(self):
        return f"Species: {self.species}, Sound: {self.animal_sound}"
