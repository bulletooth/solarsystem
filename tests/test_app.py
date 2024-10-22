import unittest
from unittest.mock import patch, MagicMock
from app import input_validation, button_planet_info, button_planet_mass, button_planet_existence, button_planet_moons


# Unit test for Solar System App
class TestSolarSystemApp(unittest.TestCase):

    def setUp(self):
        # Mock the Entry widget and Label widget from Tkinter
        self.entry_patcher = patch('app.entry')
        self.mock_entry = self.entry_patcher.start()

        self.print_out_patcher = patch('app.print_out')
        self.mock_print_out = self.print_out_patcher.start()

        # Mock the solar system object
        self.solar_system_patcher = patch('app.solar_system')
        self.mock_solar_system = self.solar_system_patcher.start()

    def tearDown(self):
        self.entry_patcher.stop()
        self.print_out_patcher.stop()
        self.solar_system_patcher.stop()

    def test_input_validation_empty(self):
        # Simulate empty input
        self.mock_entry.get.return_value = "   "
        result = input_validation()
        self.mock_print_out.config.assert_called_with(text="Input cannot be empty. Please try again.", fg="red")
        self.assertIsNone(result)

    def test_input_validation_multiple_words(self):
        # Simulate input with multiple words
        self.mock_entry.get.return_value = "Mars is great"
        result = input_validation()
        self.mock_print_out.config.assert_called_with(text="Input must be a single word. Please try again.", fg="red")
        self.assertIsNone(result)

    def test_input_validation_invalid_characters(self):
        # Simulate input with numbers
        self.mock_entry.get.return_value = "Earth123"
        result = input_validation()
        self.mock_print_out.config.assert_called_with(text="Input must be a text without numbers. Please try again.",
                                                      fg="red")
        self.assertIsNone(result)

    def test_input_validation_valid(self):
        # Simulate valid input
        self.mock_entry.get.return_value = "Mars"
        result = input_validation()
        self.assertEqual(result, "Mars")

    def test_button_planet_info_valid(self):
        # Mock the behavior of solar_system.find_planet
        self.mock_entry.get.return_value = "Mars"
        self.mock_solar_system.find_planet.return_value = MagicMock(name="Planet Mars", mass="6.4171 × 10²³",
                                                                    distance_from_sun=228, moons=["Phobos", "Deimos"])

        button_planet_info()

        self.mock_solar_system.find_planet.assert_called_with("Mars")
        self.mock_print_out.config.assert_called_with(text=self.mock_solar_system.find_planet.return_value, fg="black")

    def test_button_planet_info_invalid(self):
        # Simulate invalid planet input
        self.mock_entry.get.return_value = "Pluto"
        self.mock_solar_system.find_planet.return_value = None

        button_planet_info()

        self.mock_solar_system.find_planet.assert_called_with("Pluto")
        self.mock_print_out.config.assert_called_with(text="The planet is not in the solar system.", fg="black")

    def test_button_planet_mass_valid(self):
        # Mock valid input and mass
        self.mock_entry.get.return_value = "Earth"
        self.mock_solar_system.get_planet_mass.return_value = "5.972168 × 10²⁴"

        button_planet_mass()

        self.mock_solar_system.get_planet_mass.assert_called_with("Earth")
        self.mock_print_out.config.assert_called_with(text="The mass of Earth is 5.972168 × 10²⁴ kg.", fg="black")

    def test_button_planet_mass_invalid(self):
        # Simulate invalid planet input
        self.mock_entry.get.return_value = "Pluto"
        self.mock_solar_system.get_planet_mass.return_value = None

        button_planet_mass()

        self.mock_solar_system.get_planet_mass.assert_called_with("Pluto")
        self.mock_print_out.config.assert_called_with(text="The planet is not in the solar system.", fg="black")

    def test_button_planet_existence_valid(self):
        # Mock valid planet input for existence check
        self.mock_entry.get.return_value = "Mars"
        self.mock_solar_system.is_planet_in_system.return_value = True

        button_planet_existence()

        self.mock_solar_system.is_planet_in_system.assert_called_with("Mars")
        self.mock_print_out.config.assert_called_with(text="Yes, Mars is in the solar system.", fg="black")

    def test_button_planet_existence_invalid(self):
        # Simulate invalid planet input for existence check
        self.mock_entry.get.return_value = "Pluto"
        self.mock_solar_system.is_planet_in_system.return_value = False

        button_planet_existence()

        self.mock_solar_system.is_planet_in_system.assert_called_with("Pluto")
        self.mock_print_out.config.assert_called_with(text="No, Pluto is not in the solar system.", fg="black")

    def test_button_planet_moons_valid(self):
        # Mock valid planet input for moons
        self.mock_entry.get.return_value = "Jupiter"
        mock_planet = MagicMock()
        mock_planet.name = "Jupiter"
        mock_planet.moons_total = 79
        mock_planet.moons = ["Io", "Europa", "Ganymede", "Callisto"]
        mock_planet.get_moon_count.return_value = 4
        self.mock_solar_system.find_planet.return_value = mock_planet

        button_planet_moons()

        self.mock_solar_system.find_planet.assert_called_with("Jupiter")
        expected_output = "Jupiter has 79 moons.\nMoons: Io, Europa, Ganymede, Callisto ..."
        self.mock_print_out.config.assert_called_with(text=expected_output, fg="black")

    def test_button_planet_moons_invalid(self):
        # Simulate invalid planet input (planet doesn't exist)
        self.mock_entry.get.return_value = "Pluto"
        self.mock_solar_system.find_planet.return_value = None  # Simulate find_planet returning None

        button_planet_moons()

        # Assert that the error message for a non-existent planet is shown
        self.mock_print_out.config.assert_called_with(text="The planet is not in the solar system.", fg="black")


if __name__ == "__main__":
    unittest.main()
