from solarsystem import Planet, SolarSystem


def main_menu():
    solar_system = construct_solar_system()

    while True:
        print("\nSolar System Information Menu:")
        print("1. Tell me everything about a planet")
        print("2. How massive is a planet?")
        print("3. Is a certain planet in the list?")
        print("4. How many moons does a planet have?")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            planet_info(solar_system)
        elif choice == '2':
            planet_mass(solar_system)
        elif choice == '3':
            planet_existence(solar_system)
        elif choice == '4':
            planet_moons(solar_system)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid input, please enter a valid option.")


def construct_solar_system():
    solar_system = SolarSystem()

    solar_system.add_planet(Planet("Mercury", "3.3011 x 10\u00b2\u00b3 kg", "46 million to 70 million km", ["Mercury has no moons"]))
    solar_system.add_planet(Planet("Venus", "4.8675 × 10\u00b2\u2074 kg", "108 million km", ["Venus has no moons"]))
    solar_system.add_planet(Planet("Earth", "5.972168 × 10\u00b2\u2074 kg", "150 million km", ["Moon"]))
    solar_system.add_planet(Planet("Mars", "6.4171 × 10\u00b2\u00b3 kg", "230 million km", ["Deimos", "Phobos"]))
    solar_system.add_planet(Planet("Jupiter", "1.8982 × 10\u00b2\u2077 kg", "778 million km", ["Callisto", "Europa", "Ganymede", "Io"]))
    solar_system.add_planet(Planet("Saturn", "5.6834 × 10\u00b2\u2076 kg", "1,434 million km", ["Enceladus", "Rhea", "Titan"]))
    solar_system.add_planet(Planet("Uranus", "(8.6810 \u00b1 0.0013) × 10\u00b2\u2075 kg", "3 billion km", ["Ariel", "Miranda", "Oberon", "Titania", "Umbriel"]))
    solar_system.add_planet(Planet("Neptune", "1.02409 × 10\u00b2\u2076 kg", "4.5 billion km", ["Despina","Galatea", "Naiad", "Nereid", "Thalassa", "Triton"]))
    return solar_system


def planet_info(solar_system):
    name = input("Enter the name of the planet: ")
    planet = solar_system.find_planet(name)
    if planet:
        print(planet)
    else:
        print(f"{name} is not in the solar system.")


def planet_mass(solar_system):
    name = input("Enter the name of the planet: ")
    mass = solar_system.get_planet_mass(name)
    if mass:
        print(f"The mass of {name} is {mass}.")
    else:
        print(f"{name} is not in the solar system.")


def planet_existence(solar_system):
    name = input("Enter the name of the planet: ")
    if solar_system.is_planet_in_system(name):
        print(f"Yes, {name} is in the solar system.")
    else:
        print(f"No, {name} is not in the solar system.")


def planet_moons(solar_system):
    name = input("Enter the name of the planet: ")
    moons = solar_system.get_planet_moon_count(name)
    if moons is not None:
        print(f"{name} has {moons} moons.")
    else:
        print(f"{name} is not in the solar system.")


if __name__ == "__main__":
    main_menu()
