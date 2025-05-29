from animal import Animal

def main():

    species = input("Enter animal species: \n")
    sound = input("What sound does this animal make? E.g bark, meow, squeak. \n")

    animal_info = Animal(species, sound)

    animal_info.make_sound()


if __name__ == "__main__":
    main()