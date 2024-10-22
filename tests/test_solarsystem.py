import unittest
import json
from solarsystem import Planet
from unittest.mock import patch, mock_open
from main import construct_solar_system, planet_info, planet_mass, planet_existence, planet_moons, validated_input

# Sample data from planets.json file for mocking purposes
sample_planet_data = '''
[
  {
    "name": "Mercury",
    "mass": "3.3011 x 10²³",
    "distance_from_sun": 57.9,
    "moons_total": 0,
    "moons": []
  },
  {
    "name": "Earth",
    "mass": "5.972168 × 10²⁴",
    "distance_from_sun": 149.6,
    "moons_total": 1,
    "moons": ["Moon"]
  }
]
'''


# Unit test for Planet class
class TestPlanetClass(unittest.TestCase):

    def test_planet_creation(self):
        planet = Planet("Earth", "5.972168 × 10²⁴", 149.6, 1, ["Moon"])
        self.assertEqual(planet.name, "Earth")
        self.assertEqual(planet.mass, "5.972168 × 10²⁴")
        self.assertEqual(planet.distance_from_sun, 149.6)
        self.assertEqual(planet.moons_total, 1)
        self.assertEqual(planet.moons, ["Moon"])

    def test_string_representation(self):
        planet = Planet("Mars", "6.4171 × 10²³", 228, 2, ["Deimos", "Phobos"])
        expected_output = "Planet Mars:\n - Mass: 6.4171 × 10²³ kg\n - Average distance from the Sun: 228 million km\n - Total count of moons: 2\n - Moons: Deimos, Phobos"
        self.assertEqual(str(planet), expected_output)


# Unit test for SolarSystem class
class TestSolarSystem(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data=sample_planet_data)
    @patch('json.load')
    def test_construct_solar_system(self, mock_json_load, mock_file):
        # Mock the json.load function to load our sample data
        mock_json_load.return_value = json.loads(sample_planet_data)

        solar_system = construct_solar_system()

        # Assert that the planets were correctly loaded into the solar system
        mercury = solar_system.find_planet("Mercury")
        earth = solar_system.find_planet("Earth")

        self.assertIsNotNone(mercury)
        self.assertEqual(mercury.mass, "3.3011 x 10²³")
        self.assertEqual(mercury.moons_total, 0)

        self.assertIsNotNone(earth)
        self.assertEqual(earth.mass, "5.972168 × 10²⁴")
        self.assertEqual(earth.moons_total, 1)
        self.assertEqual(earth.moons, ["Moon"])

    @patch('builtins.input', side_effect=["", "Mercury1", "Mercury"])
    def test_validated_input(self, mock_input):
        with patch('builtins.print') as mock_print:
            result = validated_input("Enter planet name:")
            self.assertEqual(result, "Mercury")
            mock_print.assert_any_call("Input cannot be empty. Please try again.")
            mock_print.assert_any_call("Input must be a text without numbers. Please try again.")

    @patch('builtins.input', side_effect=["Earth"])
    @patch('builtins.print')
    def test_planet_info(self, mock_print, mock_input):
        # Mock the SolarSystem and add Earth
        solar_system = construct_solar_system()
        planet_info(solar_system)

        # Check if the information about Earth is printed
        earth = solar_system.find_planet("Earth")
        mock_print.assert_called_with(earth)

    @patch('builtins.input', side_effect=["Mercury"])
    @patch('builtins.print')
    def test_planet_mass(self, mock_print, mock_input):
        # Mock the SolarSystem and add Mercury
        solar_system = construct_solar_system()
        planet_mass(solar_system)

        mock_print.assert_called_with("The mass of Mercury is 3.3011 x 10²³ kg.")

    @patch('builtins.input', side_effect=["Jupiter"])
    @patch('builtins.print')
    def test_planet_mass_not_found(self, mock_print, mock_input):
        # Mock the SolarSystem without adding Jupiter
        solar_system = construct_solar_system()
        planet_mass(solar_system)

        mock_print.assert_called_with("Jupiter is not in the solar system.")

    @patch('builtins.input', side_effect=["Earth"])
    @patch('builtins.print')
    def test_planet_existence(self, mock_print, mock_input):
        # Mock the SolarSystem and add Earth
        solar_system = construct_solar_system()
        planet_existence(solar_system)

        mock_print.assert_called_with("Yes, Earth is in the solar system.")

    @patch('builtins.input', side_effect=["Jupiter"])
    @patch('builtins.print')
    def test_planet_existence_not_found(self, mock_print, mock_input):
        # Mock the SolarSystem without adding Jupiter
        solar_system = construct_solar_system()
        planet_existence(solar_system)

        mock_print.assert_called_with("No, Jupiter is not in the solar system.")

    @patch('builtins.input', side_effect=["Earth"])
    @patch('builtins.print')
    def test_planet_moons(self, mock_print, mock_input):
        # Mock the SolarSystem and add Earth
        solar_system = construct_solar_system()
        planet_moons(solar_system)

        expected_calls = [
            unittest.mock.call("Earth has 1 moon."),
            unittest.mock.call("Moons: Moon")
        ]
        mock_print.assert_has_calls(expected_calls)


if __name__ == "__main__":
    unittest.main()

# References
'''
Mariya (2023). Testing GUI Apps - What to test? How to test it? Mini Coding Course for Beginners. Python Simplified. https://www.youtube.com/watch?v=EqJWhlC1H6k
Mariya (2022). Python TDD Workflow - Unit Testing Code Example for Beginners. Python Simplified. https://www.youtube.com/@PythonSimplified/search
Silveira, O.S.(2022). A Beginner’s Guide to Unit Tests in Python (2023). Dataquest Labs Inc. https://www.dataquest.io/blog/unit-tests-python/
Python Tytorial. Python assertIsNone(). Retrieved October 21, 2024, from https://www.pythontutorial.net/python-unit-testing/python-assertisnone/
Python Software Foundation. unittest — Unit testing framework. Retrieved October 20, 2024, from https://docs.python.org/3/library/unittest.html
'''
