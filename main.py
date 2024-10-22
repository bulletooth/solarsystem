from solarsystem import Planet, SolarSystem
import json

FILE_PATH = 'planets.json'


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


def construct_solar_system(file=FILE_PATH):
    solar_system = SolarSystem()

    try:
        with open(file, 'r') as file:
            data = json.load(file)

            for planet_data in data:
                name = planet_data["name"]
                mass = planet_data["mass"]
                distance_from_sun = planet_data["distance_from_sun"]
                moons_total = planet_data["moons_total"]
                moons = planet_data["moons"]

                planet = Planet(name, mass, distance_from_sun, moons_total, moons)
                solar_system.add_planet(planet)

    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
    except json.JSONDecodeError:
        print("Error: The file is not a valid JSON file.")

    return solar_system


def validated_input(prompt):
    i = 0
    while i < 3:
        request = input(prompt)
        if not request.strip():
            print("Input cannot be empty. Please try again.")
        elif len(request.split()) != 1:
            print("Input must be a single word. Please try again.")
        elif not request.isalpha():
            print("Input must be a text without numbers. Please try again.")
        else:
            return request
        i += 1
    print("Returning back to main menu.")
    main_menu()


def planet_info(solar_system):
    name = validated_input("Enter the name of the planet: ")
    planet = solar_system.find_planet(name)
    if planet:
        print(planet)
    else:
        print(f"{name.capitalize()} is not in the solar system.")


def planet_mass(solar_system):
    name = validated_input("Enter the name of the planet: ")
    mass = solar_system.get_planet_mass(name)
    if mass:
        print(f"The mass of {name.capitalize()} is {mass} kg.")
    else:
        print(f"{name.capitalize()} is not in the solar system.")


def planet_existence(solar_system):
    name = validated_input("Enter the name of the planet: ")
    if solar_system.is_planet_in_system(name):
        print(f"Yes, {name.capitalize()} is in the solar system.")
    else:
        print(f"No, {name.capitalize()} is not in the solar system.")


def planet_moons(solar_system):
    name = validated_input("Enter the name of the planet: ")
    # moons = solar_system.get_planet_moon_count(name)
    planet = solar_system.find_planet(name)
    if planet.moons_total is not None:
        print(f"{planet.name} has {planet.moons_total} moon{"s" if planet.moons_total != 1 else ""}.")
        if planet.moons_total > 0:
            print(f"Moons: {', '.join(planet.moons)}{" ..." if planet.get_moon_count() < planet.moons_total else ""}")
    else:
        print(f"{name.capitalize()} is not in the solar system.")


if __name__ == "__main__":
    main_menu()

# References
'''

Acsany, P. (2024). Working With JSON Data in Python. Real Python. https://realpython.com/python-json/
Compart AG. Unicode. Retrieved October 14, 2024, from https://www.compart.com/en/unicode/
Downey, A. (2012), Think Python: How to Think Like a Computer Scientist: Learning with Python 3, Greentea Press. http://www.thinkpython.com
Gray, D (2023), Python Tutorial for Beginners (with mini-projects), free CodeCamp. https://youtu.be/qwAFL1597eM?si=1DQAWVE6F4FlF4zc 
Mertz, J. Reading and Writing Files in Python (Guide). Real Python. Retrieved October 15, 2024, from https://realpython.com/read-write-files-python/
Spronk, P. (2023), The Coder's Apprentice. https://www.spronck.net/pythonbook/
Stack Overflow. Python Ternary Operator Without else. Retrieved October 16, 2024, from https://stackoverflow.com/questions/12199757/python-ternary-operator-without-else
Stack Overflow. How do you print superscript?. Retrieved October 14, 2024, from https://stackoverflow.com/questions/8651361/how-do-you-print-superscript
Wikipedia. Unicode subscripts and superscripts. Retrieved October 14, 2024, from https://en.wikipedia.org/wiki/Unicode_subscripts_and_superscripts
Wikipedia. Solar System. Retrieved October 14, 2024, from https://en.wikipedia.org/wiki/Solar_System
Zaczynski, B. (2023). Serialize Your Data With Python. Real Python. https://realpython.com/python-serialize-data/
'''
