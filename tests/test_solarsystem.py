import unittest
from solarsystem import Planet, SolarSystem


class TestPlanet(unittest.TestCase):
    def setUp(self):
        self.earth = Planet("Earth", "5.972168 × 10²⁴", 149.6, ["Moon"], 1)

    def test_planet_creation(self):
        self.assertEqual(self.earth.name, "Earth")
        self.assertEqual(self.earth.mass, "5.972168 × 10²⁴")
        self.assertEqual(self.earth.distance_from_sun, 149.6)
        self.assertEqual(self.earth.moons, ["Moon"])
        self.assertEqual(self.earth.moons_total, 1)

    def test_planet_string_representation(self):
        expected_output = "Planet Earth:\n - Mass: 5.972168 × 10²⁴ kg\n - Average distance from the Sun: 149.6 million km\n - Total count of moons: 1\n - Moons: Moon"
        self.assertEqual(str(self.earth), expected_output)


class TestSolarSystem(unittest.TestCase):
    def setUp(self):
        self.solar_system = SolarSystem()
        self.earth = Planet("Earth", "5.972168 × 10²⁴", 149.6, ["Moon"], 1)
        self.mars = Planet("Mars", "6.4171 × 10²³", 228, ["Phobos", "Deimos"], 2)
        self.solar_system.add_planet(self.earth)
        self.solar_system.add_planet(self.mars)

    def test_add_planet(self):
        self.assertEqual(len(self.solar_system.planets), 2)

    def test_find_planet(self):
        found_planet = self.solar_system.find_planet("Earth")
        self.assertEqual(found_planet, self.earth)

    def test_planet_not_found(self):
        found_planet = self.solar_system.find_planet("Venus")
        self.assertIsNone(found_planet)

    def test_get_planet_mass(self):
        self.assertEqual(self.solar_system.get_planet_mass("Earth"), "5.972168 × 10²⁴")
        self.assertIsNone(self.solar_system.get_planet_mass("Pluto"))

    def test_get_planet_moon_count(self):
        self.assertEqual(self.solar_system.get_planet_moon_count("Mars"), 2)
        self.assertEqual(self.solar_system.get_planet_moon_count("Earth"), 1)
        self.assertIsNone(self.solar_system.get_planet_moon_count("Pluto"))


if __name__ == '__main__':
    unittest.main()
