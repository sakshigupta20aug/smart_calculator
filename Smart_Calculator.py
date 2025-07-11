import streamlit as st
import math

# Page config
st.set_page_config(page_title="Smart Calculator by Sakshi", page_icon="🧮", layout="centered")

# Title
st.markdown("<h1 style='text-align: center;'>🧮 Smart Calculator</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>Created by Sakshi Gupta</h4>", unsafe_allow_html=True)
st.markdown("---")

# Store history in session
if "history" not in st.session_state:
    st.session_state.history = []

# Operation selection
st.subheader("🔧 Select Operation")
operation = st.selectbox(
    "",
    [
        "Add", "Subtract", "Multiply", "Divide", "Power", "Modulus",
        "Square Root", "Logarithm (base 10)", 
        "Sine", "Cosine", "Tangent"
    ]
)

# Input area
st.subheader("🔢 Enter Numbers")
single_input_ops = ["Square Root", "Logarithm (base 10)", "Sine", "Cosine", "Tangent"]

if operation in single_input_ops:
    num1 = st.number_input("Enter number", value=0.0, format="%.4f", key="num1")
    num2 = None
else:
    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("First number", value=0.0, format="%.4f", key="num1")
    with col2:
        num2 = st.number_input("Second number", value=0.0, format="%.4f", key="num2")

# Calculate button
st.markdown("### 📤 Result")
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
                st.error("❌ Logarithm undefined for ≤ 0!")
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

# History
if st.session_state.history:
    st.markdown("---")
    st.subheader("📜 Calculation History")
    for i, item in enumerate(reversed(st.session_state.history), 1):
        st.text(f"{i}. {item}")

# Clear history
if st.button("🧹 Clear History"):
    st.session_state.history = []
    st.info("🧼 History cleared!")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Made with ❤️ using Streamlit by <strong>Sakshi Gupta</strong></p>", unsafe_allow_html=True)
