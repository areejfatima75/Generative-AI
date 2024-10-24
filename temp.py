import streamlit as st

# Conversion functions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Streamlit app layout
st.title("Temperature Converter")

# User input for the type of conversion
conversion_type = st.radio(
    "Choose the conversion type:",
    ('Celsius to Fahrenheit', 'Fahrenheit to Celsius')
)

if conversion_type == 'Celsius to Fahrenheit':
    celsius = st.number_input("Enter temperature in Celsius:", value=0.0)
    if st.button('Convert'):
        fahrenheit = celsius_to_fahrenheit(celsius)
        st.write(f"{celsius}°C is equal to {fahrenheit}°F")
elif conversion_type == 'Fahrenheit to Celsius':
    fahrenheit = st.number_input("Enter temperature in Fahrenheit:", value=0.0)
    if st.button('Convert'):
        celsius = fahrenheit_to_celsius(fahrenheit)
        st.write(f"{fahrenheit}°F is equal to {celsius}°C")
