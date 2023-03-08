import streamlit as st

# Function to calculate basal insulin dose
def calculate_basal_insulin_weight(weight):
    basal_dose = weight * 0.5 # Start with 0.5 units/kg/day
    return basal_dose

# Function to calculate total daily insulin dose
def calculate_total_daily_dose(basal_dose, weight):
    total_daily_dose = basal_dose + 0.5 * weight # Add 0.5 units/kg/day for mealtime insulin
    return total_daily_dose

# Set up the app
st.title("Basal Insulin Calculator for Type 1 Diabetics")

st.write("Enter the patient's weight in kg and their current insulin regimen to calculate their basal insulin dose.")

weight = st.number_input("Weight (kg)", min_value=1.0, max_value=300.0, value=70.0, step=0.1)

insulin_regimen = st.selectbox("Insulin Regimen", ("Multiple Daily Injections (MDI)", "Continuous Subcutaneous Insulin Infusion (CSII)"))

if insulin_regimen == "MDI":
    basal_dose = calculate_basal_insulin_weight(weight)
    total_daily_dose = calculate_total_daily_dose(basal_dose, weight)

    st.write(f"Basal insulin dose: {round(basal_dose, 1)} units/day")
    st.write(f"Total daily insulin dose: {round(total_daily_dose, 1)} units/day")

elif insulin_regimen == "CSII":
    basal_dose = weight * 0.4 # Start with 0.4-0.6 units/kg/day for CSII
    total_daily_dose = calculate_total_daily_dose(basal_dose, weight)

    st.write(f"Basal insulin dose: {round(basal_dose, 1)} units/day")
    st.write(f"Total daily insulin dose: {round(total_daily_dose, 1)} units/day")
