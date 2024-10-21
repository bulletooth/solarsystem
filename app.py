from tkinter import *
from PIL import Image, ImageTk
from main import construct_solar_system


def input_validation():
    request = entry.get()
    if not request.strip():
        print_out.config(text="Input cannot be empty. Please try again.", fg="red")
    elif len(request.split()) != 1:
        print_out.config(text="Input must be a single word. Please try again.", fg="red")
    elif not request.isalpha():
        print_out.config(text="Input must be a text without numbers. Please try again.", fg="red")
    else:
        return request


def button_planet_info():
    name = input_validation()
    if name != None:
        planet = solar_system.find_planet(name)
        if planet:
            print_out.config(text=planet, fg="black")
        else:
            print_out.config(text="The planet is not in the solar system.", fg="black")


def button_planet_mass():
    name = input_validation()
    mass = solar_system.get_planet_mass(name)
    print_out.config(fg="black")
    if mass:
        print_out.config(text=f"The mass of {name.capitalize()} is {mass} kg.", fg="black")
    else:
        print_out.config(text="The planet is not in the solar system.", fg="black")


def button_planet_existence():
    name = input_validation()
    print_out.config(fg="black")
    if solar_system.is_planet_in_system(name):
        print_out.config(text=f"Yes, {name.capitalize()} is in the solar system.", fg="black")
    else:
        print_out.config(text=f"No, {name.capitalize()} is not in the solar system.", fg="black")


def button_planet_moons():
    name = input_validation()
    planet = solar_system.find_planet(name)
    print_out.config(fg="black")
    if planet.moons_total is not None:
        print_out.config(
            text=f"{planet.name} has {planet.moons_total} moon{"s" if planet.moons_total != 1 else ""}.\n{"Moons: " if planet.moons_total > 0 else ""}{', '.join(planet.moons)}{" ..." if planet.get_moon_count() < planet.moons_total else ""}",
            fg="black")
    else:
        print_out.config(text="The planet is not in the solar system.", fg="black")


solar_system = construct_solar_system()

root = Tk()

# Set window size and center it
width = 340
height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - width) // 2
y = (screen_height - height) // 2
root.geometry(f"{width}x{height}+{x}+{y}")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe = Frame(root)
mainframe.grid(rowspan=6, sticky=NSEW)

root.title("Solary System App")

logo = Image.open('solarsystemlogo.jpeg')
logo = ImageTk.PhotoImage(logo)
logo_label = Label(image=logo)
logo_label.image = logo
logo_label.grid(row=0, padx=0, pady=0, ipadx=0, ipady=0)

entry = Entry(root, width=30, background="black", foreground="white", justify="center")
entry.grid(row=1)
entry.insert(0, "Enter planet's name")

planet_info_button = Button(root, text="Tell me everything about this planet", command=button_planet_info, width=30)
planet_info_button.grid(row=2)
planet_mass_button = Button(root, text="How massive is this planet?", command=button_planet_mass, width=30)
planet_mass_button.grid(row=3)
planet_existence_button = Button(root, text="Is this planet in the Solar System?", command=button_planet_existence,
                                 width=30)
planet_existence_button.grid(row=4)
planet_moons_button = Button(root, text="How many moons does this planet have?", command=button_planet_moons,
                             width=30)
planet_moons_button.grid(row=5)

print_out = Label(root, height=10, wraplength=300, justify="left", anchor="n", font="Courier 14 bold",
                  foreground="black")
print_out.grid(row=6)
root.mainloop()
