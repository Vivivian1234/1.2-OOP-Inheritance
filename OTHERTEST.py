# weapons.py

class Weapon:
    def __init__(self, name, category, damage):
        self.name = name
        self.category = category
        self.damage = damage

    def get_stats(self):
        print(f"Name: {self.name}\nCategory: {self.category}\nDamage: {self.damage}")

    def set_name(self, name):
        self.name = name

    def set_category(self, category):
        self.category = category

    def set_damage(self, damage):
        self.damage = damage


class Sword(Weapon):
    def __init__(self, name, category, damage, damage_category):
        super().__init__(name, category, damage)
        self.damage_category = damage_category

    def get_stats(self):
        print(f"Name: {self.name}\nCategory: {self.category}\nDamage: {self.damage}\nDamage Type: {self.damage_category}\nCrit Damage: {self.damage * 3}")

    def set_damage_category(self, damage_category):
        self.damage_category = damage_category


class Bow(Weapon):
    def __init__(self, name, category, damage, damage_category):
        super().__init__(name, category, damage)
        self.damage_category = damage_category

    def get_stats(self):
        print(f"Name: {self.name}\nCategory: {self.category}\nDamage: {self.damage}\nDamage Type: {self.damage_category}\nCrit Damage: {self.damage * 2}")

    def set_damage_category(self, damage_category):
        self.damage_category = damage_category


class Longbow(Bow):
    def __init__(self, name, category, damage, damage_category, bow_range):
        super().__init__(name, category, damage, damage_category)
        self.bow_range = bow_range

    def get_stats(self):
        print(f"Name: {self.name}\nCategory: {self.category}\nDamage: {self.damage}\nDamage Type: {self.damage_category}\nRange: {self.bow_range} ft\nCrit Damage: {self.damage * 2}")

    def set_bow_range(self, bow_range):
        self.bow_range = bow_range


class Shortbow(Bow):
    def __init__(self, name, category, damage, damage_category, bow_range):
        super().__init__(name, category, damage, damage_category)
        self.bow_range = bow_range

    def get_stats(self):
        print(f"Name: {self.name}\nCategory: {self.category}\nDamage: {self.damage}\nDamage Type: {self.damage_category}\nRange: {self.bow_range} ft\nCrit Damage: {self.damage * 2}")

    def set_bow_range(self, bow_range):
        self.bow_range = bow_range
