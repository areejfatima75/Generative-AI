import streamlit as st

# Conversion functions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Streamlit app layout
st.title("🌡️ Temperature Converter")

# Sidebar for input
st.sidebar.header("Conversion Settings")

# User input for the type of conversion in the sidebar
conversion_type = st.sidebar.radio(
    "Choose the conversion type:",
    ('Celsius to Fahrenheit', 'Fahrenheit to Celsius')
)

# Use a slider for more interactive temperature input
if conversion_type == 'Celsius to Fahrenheit':
    celsius = st.slider("Select temperature in Celsius:", min_value=-100.0, max_value=100.0, value=0.0)
    fahrenheit = celsius_to_fahrenheit(celsius)
    
    # Dynamic output with a colored metric display
    st.metric(label="Temperature in Fahrenheit", value=f"{fahrenheit:.2f}°F", delta=f"{fahrenheit - 32:.2f}°F")
    
    # Adding an image for better user experience
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/4e/Thermometer_image.png", width=150)
    
elif conversion_type == 'Fahrenheit to Celsius':
    fahrenheit = st.slider("Select temperature in Fahrenheit:", min_value=-200.0, max_value=200.0, value=32.0)
    celsius = fahrenheit_to_celsius(fahrenheit)
    
    # Dynamic output with a colored metric display
    st.metric(label="Temperature in Celsius", value=f"{celsius:.2f}°C", delta=f"{celsius - 0:.2f}°C")
    
    # Adding an image for better user experience
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/4e/Thermometer_image.png", width=150)

# Add an expander for additional information
with st.expander("ℹ️ About this app"):
    st.write("""
        This app allows you to convert temperatures between Celsius and Fahrenheit.
        - Use the **slider** to select a temperature.
        - The result will be shown dynamically.
        - Conversion formulas:
            - °F = (°C * 9/5) + 32
            - °C = (°F - 32) * 5/9
    """)

# Footer
st.sidebar.markdown("Created with ❤️ using Streamlit")
