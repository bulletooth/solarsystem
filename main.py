from solarsystem import Planet, SolarSystem
import json


def main_menu():
    solar_system = construct_solar_system('planets.json')

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


def construct_solar_system(filename):
    solar_system = SolarSystem()

    try:
        with open(filename, 'r') as file:
            data = json.load(file)

            for planet_data in data:
                name = planet_data["name"]
                mass = planet_data["mass"]
                distance_from_sun = planet_data["distance_from_sun"]
                moons = planet_data["moons"]

                planet = Planet(name, mass, distance_from_sun, moons)
                solar_system.add_planet(planet)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except json.JSONDecodeError:
        print("Error: The file is not a valid JSON file.")

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
