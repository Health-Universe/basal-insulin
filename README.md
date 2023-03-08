# Basal Insulin Calculator for Type 1 Diabetics

This is a simple streamlit app in Python that helps a physician calculate how much basal insulin to give to a type 1 diabetic based on their weight and current insulin regimen.

## Usage
To run the app, save the code as a Python file (e.g., basal_insulin_calculator.py) and run it using the command streamlit run basal_insulin_calculator.py in the terminal. The app will open in your web browser, and you can enter the patient's weight and insulin regimen to calculate their basal insulin dose.

## How it works
The app uses the following formulas to calculate the basal insulin dose and total daily insulin dose:

Basal insulin dose (for MDI): Start with 0.5 units/kg/day
Basal insulin dose (for CSII): Start with 0.4-0.6 units/kg/day
Total daily insulin dose: Basal insulin dose + 0.5 units/kg/day for mealtime insulin
The user inputs the patient's weight in kg and their current insulin regimen (MDI or CSII). The app then calculates the basal insulin dose and total daily insulin dose based on the input values and displays the results on the screen.

Note that this is a very simple calculator and should not be used as a substitute for professional medical advice. It's always important to consult with a physician before making any changes to a patient's insulin regimen.

## Dependencies
This app requires the following Python packages to be installed:

```streamlit```

You can install these packages using pip:
```
pip install streamlit
```

## License
This app is licensed under the MIT License.
