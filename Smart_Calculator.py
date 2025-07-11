import streamlit as st
import math

st.set_page_config(page_title="Smart Calculator", page_icon="🧮", layout="centered")
st.title("🧮 Smart Calculator App")

# Session state to store history
if "history" not in st.session_state:
    st.session_state.history = []

# Operation selection
operation = st.selectbox(
    "Choose Operation",
    [
        "Add", "Subtract", "Multiply", "Divide", "Power", "Modulus",
        "Square Root", "Logarithm (base 10)", 
        "Sine", "Cosine", "Tangent"
    ]
)

# Determine number of inputs needed
single_input_ops = ["Square Root", "Logarithm (base 10)", "Sine", "Cosine", "Tangent"]
if operation in single_input_ops:
    num1 = st.number_input("Enter number", value=0.0, format="%.4f", key="num1")
    num2 = None
else:
    num1 = st.number_input("Enter first number", value=0.0, format="%.4f", key="num1")
    num2 = st.number_input("Enter second number", value=0.0, format="%.4f", key="num2")

# Calculate button
if st.button("Calculate"):
    result = None
    try:
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("❌ Cannot divide by zero!")
        elif operation == "Power":
            result = num1 ** num2
        elif operation == "Modulus":
            result = num1 % num2
        elif operation == "Square Root":
            if num1 >= 0:
                result = math.sqrt(num1)
            else:
                st.error("❌ Cannot take square root of negative number!")
        elif operation == "Logarithm (base 10)":
            if num1 > 0:
                result = math.log10(num1)
            else:
                st.error("❌ Logarithm is undefined for zero or negative numbers!")
        elif operation == "Sine":
            result = math.sin(math.radians(num1))
        elif operation == "Cosine":
            result = math.cos(math.radians(num1))
        elif operation == "Tangent":
            result = math.tan(math.radians(num1))

        if result is not None:
            st.success(f"✅ Result: {result:.4f}")
            st.session_state.history.append(f"{operation}: {result:.4f}")

    except Exception as e:
        st.error(f"❌ Error: {str(e)}")

# Clear button
if st.button("Clear History"):
    st.session_state.history = []
    st.info("🧹 History cleared!")

# Show history
if st.session_state.history:
    st.subheader("📜 Calculation History")
    for i, item in enumerate(reversed(st.session_state.history), 1):
        st.text(f"{i}. {item}")
