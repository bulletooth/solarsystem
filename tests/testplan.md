### **Test Plan for Solar System App**

---

### **Objective:**

The test plan is designed to validate the following aspects of the Solar System Tkinter-based application:

1. Correct handling and loading of planetary data from the JSON file.
2. Proper validation of user input.
3. Functionality of the different user options (e.g., retrieving planet information, checking planet mass, verifying
   planet existence, counting moons).
4. Ensuring the Tkinter window does not block test execution.
5. Accurate display of information on the Tkinter interface (using `print_out` labels).
6. Preventing invalid inputs from breaking the app and handling errors gracefully.

---

### **Test Coverage**

1. **File Handling**
    - Test that the `planets.json` file is correctly loaded, and planetary data is correctly initialized into the
      `SolarSystem` object.
    - Ensure that missing files and JSON parsing errors are handled gracefully (i.e., `FileNotFoundError`,
      `JSONDecodeError`).

2. **User Input Validation**
    - Ensure that empty input is rejected, and an appropriate error message is shown.
    - Test multiple-word inputs, ensuring that only single-word inputs are accepted.
    - Test for numeric or mixed input (e.g., "Mars123") and ensure the system handles it appropriately.
    - Verify that only alphabetic characters are accepted.

3. **Functionality Testing**
    - **Planet Info**: Test that valid planets return the correct information (planet name, mass, distance from the Sun,
      and moons) and invalid planets return an error message.
    - **Planet Mass**: Ensure that the correct mass is returned for valid planets and that the error message is shown
      for invalid planet names.
    - **Planet Existence**: Test that the function correctly identifies whether a planet is in the solar system.
    - **Planet Moons**: Ensure the correct number of moons and the list of moon names are returned for valid planets.
      Invalid planets should return an error message.

4. **GUI (Tkinter) Testing**
    - Test that the Tkinter window can be initialized without blocking the test.
    - Ensure that buttons trigger the correct functions.
    - Mock the `Entry` widget to simulate user input and ensure the `print_out` label is updated with the correct
      information.
    - Ensure that the `mainloop()` does not block test execution by mocking or using `after()` for delayed closing of
      the window.

---

### **Test Scenarios**

#### **Scenario 1: Load Solar System Data from File**

- **Objective**: Verify that planetary data is correctly loaded from the `planets.json` file.
- **Test Steps**:
    1. Mock the file handling and JSON loading functions.
    2. Ensure that all planets are correctly added to the `SolarSystem` object.
    3. Ensure proper handling of missing or malformed files.
- **Expected Outcome**: Planets should load correctly, and errors should be handled gracefully.

#### **Scenario 2: Validate User Input**

- **Objective**: Ensure that invalid inputs are handled, and only valid inputs proceed.
- **Test Steps**:
    1. Simulate empty input, multi-word input, numeric input, and valid input using `mock_input`.
    2. Check if the proper error message is displayed for invalid input.
- **Expected Outcome**: The system should display appropriate error messages and reject invalid inputs.

#### **Scenario 3: Retrieve Planet Information**

- **Objective**: Verify that planet information is correctly retrieved for valid planets and handled correctly for
  invalid ones.
- **Test Steps**:
    1. Simulate valid and invalid planet names using `mock_input`.
    2. Call `planet_info()`.
    3. Ensure that the correct information is displayed for valid planets.
    4. Ensure an error message is displayed for invalid planets.
- **Expected Outcome**: Correct information for valid planets, appropriate error message for invalid inputs.

#### **Scenario 4: Retrieve Planet Mass**

- **Objective**: Ensure that planet mass is correctly retrieved and displayed for valid planets and handled properly for
  invalid ones.
- **Test Steps**:
    1. Simulate valid and invalid planet names using `mock_input`.
    2. Call `planet_mass()`.
    3. Ensure the correct mass is displayed for valid planets and that an error message is displayed for invalid
       planets.
- **Expected Outcome**: Correct mass for valid planets, appropriate error message for invalid inputs.

#### **Scenario 5: Verify Planet Existence**

- **Objective**: Verify that the system correctly identifies whether a planet is in the solar system.
- **Test Steps**:
    1. Simulate valid and invalid planet names using `mock_input`.
    2. Call `planet_existence()`.
    3. Ensure the correct message is displayed for valid planets and that an error message is displayed for invalid
       planets.
- **Expected Outcome**: Correct existence message for valid planets, appropriate error message for invalid inputs.

#### **Scenario 6: Retrieve Planet Moons**

- **Objective**: Ensure that the correct number of moons and moon names are retrieved for valid planets.
- **Test Steps**:
    1. Simulate valid and invalid planet names using `mock_input`.
    2. Call `planet_moons()`.
    3. Ensure the correct moon count and list of moons are displayed for valid planets.
    4. Ensure that an error message is displayed for invalid planets.
- **Expected Outcome**: Correct moon count and names for valid planets, appropriate error message for invalid inputs.

#### **Scenario 7: GUI Testing**

- **Objective**: Ensure the Tkinter interface works without blocking tests and displays correct output based on user
  interaction.
- **Test Steps**:
    1. Mock the `Entry` widget to simulate user input.
    2. Mock the `Label` widget (`print_out`) to check if it's updated correctly.
    3. Ensure buttons trigger the correct functions and display the correct output in the `print_out` label.
    4. Mock or use `after()` to prevent the `mainloop()` from blocking test execution.
- **Expected Outcome**: The window should initialize, user input should trigger the correct functions, and output should
  display in the label.

---

### **Pass/Fail Criteria**

| Test Scenario                     | Description                                                             | Pass/Fail Criteria                                                                              |
|-----------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| **File Handling**                 | Ensure that `planets.json` is loaded correctly.                         | Planets are correctly added to the solar system.                                                |
| **User Input Validation**         | Test input validation for empty, multi-word, numeric, and valid inputs. | Invalid inputs are rejected, valid inputs proceed.                                              |
| **Planet Info Retrieval**         | Test planet information retrieval for valid/invalid planets.            | Correct information for valid planets, error for invalid inputs.                                |
| **Planet Mass Retrieval**         | Ensure planet mass is retrieved for valid/invalid planets.              | Correct mass for valid planets, error for invalid inputs.                                       |
| **Planet Existence Verification** | Test whether the planet exists in the solar system.                     | Correct existence message for valid planets, error for invalid ones.                            |
| **Planet Moons Retrieval**        | Test moon count and moon name retrieval for planets.                    | Correct moon count and names for valid planets, error for invalid ones.                         |
| **Tkinter GUI Testing**           | Test Tkinter interaction without blocking tests.                        | Tkinter window initializes, buttons trigger correct functions, `print_out` is updated properly. |

---

### **Risks & Assumptions**

- **Risks**: Tkinter's `mainloop()` may block tests if not properly mocked or handled using `after()`. Incorrect mocking
  of user inputs or the GUI components may lead to false failures.
- **Assumptions**: The `planets.json` file is properly formatted. Tkinter components are testable through mock
  functions.

---