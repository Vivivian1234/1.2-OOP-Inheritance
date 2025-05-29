from weapons import Weapon, Sword, Bow, Longbow, Shortbow

weapon_list = Weapon


def main():
    while True:
        action = input("This is the weapon recording system. What would you like to do? \n- 1. Add weapon \n- 2. View inventory \n- 3. Search inventory \n- 4. Exit\n")

        if action == "1":
            weapon = input("What weapon woudl you like to add?\n- 1. Sword \n- 2. Bow \n- 3. Longbow \n- 4. Shortbow\n")
            if weapon == "1":
                damage = input("Enter damage: ")
                weapon_list.get_stats(Sword)
            elif weapon == "2":
                damage = input("Enter damage: ")
                weapon_list.get_stats(Bow)
            elif weapon == "3":
                damage = input("Enter damage: ")
                weapon_list.get_stats(Longbow)
            elif weapon == "4":
                damage = input("Enter damage: ")
                weapon_list.get_stats(Shortbow)
            else:
                print("\nInvalid input. Please try again.\n")
        elif action == "2":
            weapon_list.view_inventory()
        elif action == "3":
            weapon_list.search_inventory()
        elif action == "4":
            print("\nThank you for using this program.\n")
            break
        else:
            print("\nInvalid input. Please try again.\n")

main()

