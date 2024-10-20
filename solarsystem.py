class Planet:
    def __init__(self, name, mass, distance_from_sun, moons, moons_total):
        self.name = name
        self.mass = mass
        self.distance_from_sun = distance_from_sun
        self.moons = moons
        self.moons_total = moons_total

    def __str__(self):
        return f"Planet {self.name}:\n - Mass: {self.mass} kg\n - Average distance from the Sun: {self.distance_from_sun} million km\n - Total count of moons: {self.moons_total}\n - Moons: {', '.join(self.moons)}"

    def get_mass(self):
        return self.mass

    def get_distance(self):
        return self.distance_from_sun

    def get_moon_count(self):
        return len(self.moons)


class SolarSystem:
    def __init__(self):
        self.planets = []

    def add_planet(self, planet):
        self.planets.append(planet)

    def find_planet(self, name):
        for planet in self.planets:
            if planet.name.lower() == name.lower():
                return planet
        return None

    def is_planet_in_system(self, name):
        return self.find_planet(name) is not None

    def get_planet_mass(self, name):
        planet = self.find_planet(name)
        return planet.get_mass() if planet else None

    def get_planet_moon_count(self, name):
        planet = self.find_planet(name)
        return planet.get_moon_count() if planet else None
