# Test Plan for Solar System Program

## Objective

Objective: Validate the functionality of your SolarSystem and Planet classes, ensuring that the code accurately handles
planetary data from the planets.json file, and that the user input/output functionality in main.py works as expected.

## Tests

### 1. Loading and Storing Planetary Data

- Verify that data from planets.json is correctly parsed into Planet objects.
- Ensure the data attributes such as mass, distance, and moon counts are accurate.

### 2. Querying Planet Information

- Test adding planets and retrieving them by name.
- Test the ability to query a planet’s information (name, mass, distance, moons, etc.).
- Validate handling of edge cases (e.g., querying a planet that doesn't exist).

### 3. Input Validation

- Validate user inputs for various menu options (non-empty strings, numeric inputs when required).
- Verify the program does not crash with invalid inputs.

### 4. Error Handling

- Ensure appropriate error messages are shown when invalid data or operations are encountered.

### 5. Manual Testing

- Run the program and use all menu options to ensure accurate information retrieval and correct user interface behavior.


