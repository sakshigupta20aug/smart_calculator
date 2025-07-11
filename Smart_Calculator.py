import streamlit as st
import math

# Page settings
st.set_page_config(page_title="Smart Calculator by Sakshi", page_icon="🧮", layout="centered")
st.markdown("<h1 style='text-align: center;'>🧮 Smart Calculator</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>Created by Sakshi Gupta</h4>", unsafe_allow_html=True)
st.markdown("---")

# Store history
if "history" not in st.session_state:
    st.session_state.history = []

# === Section 1: Core Smart Calculator ===
st.subheader("🔢 Standard Calculator")

# Operation selection
operation = st.selectbox(
    "Choose Operation",
    [
        "Add", "Subtract", "Multiply", "Divide", "Power", "Modulus",
        "Square Root", "Logarithm (base 10)",
        "Sine", "Cosine", "Tangent"
    ]
)

# Input logic
single_input_ops = ["Square Root", "Logarithm (base 10)", "Sine", "Cosine", "Tangent"]
if operation in single_input_ops:
    num1 = st.number_input("Enter number", value=0.0, format="%.4f", key="num1_single")
    num2 = None
else:
    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("Enter first number", value=0.0, format="%.4f", key="num1_double")
    with col2:
        num2 = st.number_input("Enter second number", value=0.0, format="%.4f", key="num2_double")

# Calculate
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
            result = num1 / num2 if num2 != 0 else st.error("❌ Cannot divide by zero!")
        elif operation == "Power":
            result = num1 ** num2
        elif operation == "Modulus":
            result = num1 % num2
        elif operation == "Square Root":
            result = math.sqrt(num1) if num1 >= 0 else st.error("❌ Invalid input for square root!")
        elif operation == "Logarithm (base 10)":
            result = math.log10(num1) if num1 > 0 else st.error("❌ Log undefined for ≤ 0!")
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
    st.subheader("📜 Calculation History")
    for i, item in enumerate(reversed(st.session_state.history), 1):
        st.text(f"{i}. {item}")

if st.button("🧹 Clear History"):
    st.session_state.history = []
    st.info("🧼 History cleared!")

st.markdown("---")

# === Section 2: 📈 Financial & Math Tools ===
st.subheader("📈 Financial & Math Tools")

# Tool selection
tool = st.selectbox("Choose Tool", ["Simple Interest", "Compound Interest", "Fibonacci Series"])

# === Simple Interest ===
if tool == "Simple Interest":
    p = st.number_input("Principal (P)", value=0.0, format="%.2f")
    r = st.number_input("Rate of Interest (R%)", value=0.0, format="%.2f")
    t = st.number_input("Time Period (T in years)", value=0.0, format="%.2f")
    if st.button("Calculate Simple Interest"):
        si = (p * r * t) / 100
        st.success(f"💰 Simple Interest = ₹{si:.2f}")

# === Compound Interest ===
elif tool == "Compound Interest":
    p = st.number_input("Principal (P)", value=0.0, format="%.2f", key="ci_p")
    r = st.number_input("Annual Interest Rate (R%)", value=0.0, format="%.2f", key="ci_r")
    t = st.number_input("Time (T in years)", value=0.0, format="%.2f", key="ci_t")
    n = st.number_input("Compounded Times per Year (n)", value=1, step=1, min_value=1, key="ci_n")
    if st.button("Calculate Compound Interest"):
        amount = p * (1 + (r / (100 * n))) ** (n * t)
        ci = amount - p
        st.success(f"💰 Compound Interest = ₹{ci:.2f} | Total Amount = ₹{amount:.2f}")

# === Fibonacci Series ===
elif tool == "Fibonacci Series":
    terms = st.number_input("Number of terms", min_value=1, max_value=100, step=1)
    if st.button("Generate Fibonacci Series"):
        fib_series = [0, 1]
        for i in range(2, int(terms)):
            fib_series.append(fib_series[-1] + fib_series[-2])
        if terms == 1:
            st.success("🔢 Fibonacci Series: 0")
        else:
            st.success(f"🔢 Fibonacci Series: {', '.join(map(str, fib_series[:int(terms)]))}")

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Made with ❤️ by <strong>Sakshi Gupta</strong></p>", unsafe_allow_html=True)
