from animal import Animal, Dog, Cat

def main():
    animal_type = input("Enter an animal (dog or cat): ").strip().lower()

    if animal_type == 'dog':
        animal = Dog()
    elif animal_type == 'cat':
        animal = Cat()
    else:
        print("\nSorry, that animal is not recognized.")
        return

    animal.make_sound()


if __name__ == "__main__":
    main()
