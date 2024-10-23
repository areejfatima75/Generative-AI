import streamlit as st

# Define functions for the calculator operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Streamlit app layout
st.title("Simple Calculator")

# User inputs for numbers
num1 = st.number_input("Enter first number", value=0.0, step=1.0)
num2 = st.number_input("Enter second number", value=0.0, step=1.0)

# Dropdown to select the operation
operation = st.selectbox("Select operation", ("Add", "Subtract", "Multiply", "Divide"))

# Perform calculation based on user selection
if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
        st.write(f"{num1} + {num2} = {result}")
    elif operation == "Subtract":
        result = subtract(num1, num2)
        st.write(f"{num1} - {num2} = {result}")
    elif operation == "Multiply":
        result = multiply(num1, num2)
        st.write(f"{num1} * {num2} = {result}")
    elif operation == "Divide":
        result = divide(num1, num2)
        st.write(f"{num1} / {num2} = {result}")

# Display the result
if st.button("Clear"):
    st.write("Calculator cleared.")
