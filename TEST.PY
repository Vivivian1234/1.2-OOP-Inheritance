# main.py
from OTHERTEST import Weapon, Sword, Bow, Longbow, Shortbow

# Predefined instances
basic_weapon = Weapon("Basic Axe", "Axe", 15)
sword = Sword("Iron Sword", "Sword", 10, "Slashing")
bow = Bow("Wooden Bow", "Bow", 8, "Piercing")
longbow = Longbow("Elven Longbow", "Bow", 12, "Piercing", 150)
shortbow = Shortbow("Scout Shortbow", "Bow", 7, "Piercing", 80)

inventory = {
    basic_weapon.name: basic_weapon,
    sword.name: sword,
    bow.name: bow,
    longbow.name: longbow,
    shortbow.name: shortbow,
}

# Add custom weapon
def create_custom_weapon():
    name = input("Enter weapon name: ")
    category = input("Enter category (Weapon/Sword/Bow/Longbow/Shortbow): ")
    damage = int(input("Enter damage value: "))

    if category.lower() == "sword":
        dmg_cat = input("Enter damage type (e.g. Slashing): ")
        w = Sword(name, "Sword", damage, dmg_cat)
    elif category.lower() == "bow":
        dmg_cat = input("Enter damage type (e.g. Piercing): ")
        w = Bow(name, "Bow", damage, dmg_cat)
    elif category.lower() == "longbow":
        dmg_cat = input("Enter damage type (e.g. Piercing): ")
        rng = int(input("Enter range in ft: "))
        w = Longbow(name, "Bow", damage, dmg_cat, rng)
    elif category.lower() == "shortbow":
        dmg_cat = input("Enter damage type (e.g. Piercing): ")
        rng = int(input("Enter range in ft: "))
        w = Shortbow(name, "Bow", damage, dmg_cat, rng)
    else:
        w = Weapon(name, category, damage)

    inventory[name] = w
    print(f"\n{name} added to inventory!\n")
    w.get_stats()

# Search for a weapon
def search_weapon():
    name = input("Enter weapon name to search: ")
    weapon = inventory.get(name)
    if weapon:
        weapon.get_stats()
    else:
        print("Weapon not found in inventory.")

# Menu
while True:
    print("\n--- Weapon Inventory System ---")
    print("1. View all weapons")
    print("2. Add custom weapon")
    print("3. Search for a weapon")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        for w in inventory.values():
            print("\n---")
            w.get_stats()
    elif choice == "2":
        create_custom_weapon()
    elif choice == "3":
        search_weapon()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
