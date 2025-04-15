import streamlit as st

st.set_page_config(page_title="Unit Converter", layout="centered")

st.markdown("""
<style>
h1 {
    text-align: center;
    color: #4B8BBE;
}
.stButton>button {
    background-color: #4B8BBE;
    color: white;
    padding: 10px 20px;
    border-radius: 8px;
}
.result-box {
    background-color: #f0f2f6;
    color: black;
    padding: 15px;
    margin-top: 20px;
    border-radius: 10px;
    font-size: 20px;
    text-align: center;
    font-weight: bold;
}
.footer {
    text-align: center;
    margin-top: 50px;
    color: gray;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>Unit Converter using Python and Streamlit</h1>", unsafe_allow_html=True)
st.write("Easily convert between different units of **Length**, **Weight**, and **Temperature**.")

conversion_type = st.sidebar.selectbox("Choose Conversion Type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter value", value=0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilometers", "Centimeters", "Milimeters", "Miles", "Yards", "Inches", "Feet"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilometers", "Centimeters", "Milimeters", "Miles", "Yards", "Inches", "Feet"])

elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilogram", "Gram", "Miligram", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilogram", "Gram", "Miligram", "Pounds", "Ounces"])

elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

# Conversion functions
def length_convert(value, from_unit, to_unit):
    length_units = {
        'Meters': 1, 'Kilometers': 0.001, 'Centimeters': 100, 'Milimeters': 1000,
        'Miles': 0.000621371, 'Yards': 1.09361, 'Feet': 3.28084, 'Inches': 39.3701
    }
    return value / length_units[from_unit] * length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        'Kilogram': 1, 'Gram': 1000, 'Miligram': 1e6, 'Pounds': 2.20462, 'Ounces': 35.274
    }
    return value / weight_units[from_unit] * weight_units[to_unit]

def temp_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else value + 273.15
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else ((value - 32) * 5/9) + 273.15
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else ((value - 273.15) * 9/5) + 32

# Conversion trigger
if st.button("Convert"):
    if conversion_type == "Length":
        result = length_convert(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temp_converter(value, from_unit, to_unit)

    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

st.markdown("<div class='footer'>Made with ❤️ using Streamlit</div>", unsafe_allow_html=True)
