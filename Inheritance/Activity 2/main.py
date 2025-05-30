# main.py
from weapons import Weapon, Sword, Bow, Longbow, Shortbow, list

inventory = []

def main():
    while True:
        action = input("\nThis is the weapon recording system. What would you like to do? \n- 1. Add weapon \n- 2. View inventory \n- 3. Search inventory \n- 4. Exit\n")

        if action == "1":
            name = input("Enter name of weapon (give it a nice name :D like Guoba, Mehrak, *Sinner's Final Notice* hehe): ")
            damage = int(input("Enter damage: "))

            weapon_choice = input("Choose type: \n- 1. Sword \n- 2. Bow \n- 3. Longbow \n- 4. Shortbow\n")
            
            if weapon_choice == "1":
                category = "Sword"
                damage_category = input("Enter damage type (e.g., slashing, piercing, etc.): ")
                new_weapon = Sword(name, category, damage, damage_category)
            elif weapon_choice == "2":
                category = "Bow"
                damage_category = "Piercing"
                new_weapon = Bow(name, category, damage, damage_category)
            elif weapon_choice == "3":
                category = "Longbow"
                damage_category = "Piercing"
                bow_range = 150
                new_weapon = Longbow(name, category, damage, damage_category, bow_range)
            elif weapon_choice == "4":
                category = "Shortbow"
                damage_category = "Piercing"
                bow_range = 80
                new_weapon = Shortbow(name, category, damage, damage_category, bow_range)
            else:
                print("\nInvalid input. Please try again.\n")
                continue

            inventory.append(new_weapon)
            print("\nWeapon added successfully!\n")

        elif action == "2":
            for weapon in inventory:
                weapon.get_stats()
                print("-" * 20)
        
        elif action == "3":
            search_term = input("Enter weapon name to search: ")
            found = [weapon for weapon in inventory if weapon.name.lower() == search_term.lower()]
            print()
            if found:
                for weapon in found:
                    weapon.get_stats()
            else:
                print("\nWeapon not found.\n")

        elif action == "4":
            print("\nThank you for using this program.\n")
            break
        else:
            print("\nInvalid input. Please try again.\n")

if __name__ == "__main__":
    main()