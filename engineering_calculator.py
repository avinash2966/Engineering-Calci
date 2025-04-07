
import streamlit as st
import math

# Function for addition
def add(x, y):
    return x + y

# Function for subtraction
def subtract(x, y):
    return x - y

# Function for multiplication
def multiply(x, y):
    return x * y

# Function for division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Function for trigonometric functions
def trig_function(func, x):
    if func == "sin":
        return math.sin(math.radians(x))
    elif func == "cos":
        return math.cos(math.radians(x))
    elif func == "tan":
        return math.tan(math.radians(x))
    else:
        return "Invalid trigonometric function."

# Function for exponential function
def exponential(x):
    return math.exp(x)

# Function for decimal function
def decimal(x):
    return float(x)

# Function for square root function
def square_root(x):
    if x < 0:
        return "Error! Square root of negative number."
    else:
        return math.sqrt(x)

# Streamlit app
st.title("Engineering Calculator")

st.header("Basic Operations")
x = st.number_input("Enter first number", value=0.0)
y = st.number_input("Enter second number", value=0.0)
operation = st.selectbox("Select operation", ["Addition", "Subtraction", "Multiplication", "Division"])

if operation == "Addition":
    result = add(x, y)
elif operation == "Subtraction":
    result = subtract(x, y)
elif operation == "Multiplication":
    result = multiply(x, y)
elif operation == "Division":
    result = divide(x, y)

st.write(f"Result: {result}")

st.header("Trigonometric Functions")
angle = st.number_input("Enter angle in degrees", value=0.0)
trig_func = st.selectbox("Select trigonometric function", ["sin", "cos", "tan"])
trig_result = trig_function(trig_func, angle)
st.write(f"Result: {trig_result}")

st.header("Exponential Function")
exp_input = st.number_input("Enter number for exponential function", value=0.0)
exp_result = exponential(exp_input)
st.write(f"Result: {exp_result}")

st.header("Decimal Function")
dec_input = st.number_input("Enter number to convert to decimal", value=0.0)
dec_result = decimal(dec_input)
st.write(f"Result: {dec_result}")

st.header("Square Root Function")
sqrt_input = st.number_input("Enter number for square root", value=0.0)
sqrt_result = square_root(sqrt_input)
st.write(f"Result: {sqrt_result}")
