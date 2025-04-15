import re
import streamlit as st

st.set_page_config(page_title="Password Strength Meter", layout="centered")

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
    margin: auto;
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
.main{
    text-align: center;
}
.stTextInput {
    width: 60%;
    margin: auto;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>Password Strength Meter using Python and Streamlit</h1>", unsafe_allow_html=True)
st.write("Enter your password below to check its strength.")

def check_password_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
        
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Password should include both uppercase and lowercase letters.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Password should include at least one number.") 
    
    if re.search(r"[~`!@#$%^&*)(_\-+=:;<>,./]", password):
        score += 1
    else:
        feedback.append("Password should include at least one special character.")
        
    # Show strength result
    if score >= 4:
        st.success("✅ Strong Password")
    elif score == 3:
        st.info("⚠️ Medium Password")
    else:
        st.warning("❌ Weak Password")
        
    # Show feedback
    if feedback:
        with st.expander("🔐 Tips for a Stronger Password"):
            for item in feedback:
                st.write(f"• {item}")

password = st.text_input("Enter your password:", type="password", help="Your password will not be shown")

if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("Please enter a password.")

st.markdown("<div class='footer'>Made with ❤️ using Streamlit</div>", unsafe_allow_html=True)
