class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.animal_sound = sound

    def make_sound(self):
        print(f'\nA {self.species} makes a {self.animal_sound}ing sound.\n')


class Dog(Animal):
    def __init__(self):
        super().__init__('dog', 'bark')


class Cat(Animal):
    def __init__(self):
        super().__init__('cat', 'meow')