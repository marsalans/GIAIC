import streamlit as st
import random
import json
import os
from datetime import datetime

USER_DATA_FILE = "growth_mindset_challenge.json"
CHALLENGES = [
    "Write down three things you're grateful for today.",
    "Step out of your comfort zone: Try something new today!",
    "Read a motivational article or book for 10 minutes.",
    "Reflect on a past failure and write down what you learned.",
    "Help someone without expecting anything in return.",
    "Practice mindfulness for at least 5 minutes.",
    "Take a small risk today and embrace uncertainty.",
    "Write a letter to your future self.",
    "Meditate for 10 minutes and note how you feel afterward.",
    "Identify a negative thought and reframe it positively."
]

def load_users():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USER_DATA_FILE, "w") as f:
        json.dump(users, f, indent=4)

def authenticate(username, password, users):
    return username in users and users[username]["password"] == password

def register_user(username, password, users):
    if username in users:
        return False
    users[username] = {"password": password, "journal": []}
    save_users(users)
    return True

def add_reflection(username, reflection, users):
    entry = {"date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "reflection": reflection}
    users[username]["journal"].append(entry)
    save_users(users)

def main():
    st.set_page_config(page_title="Growth Mindset Tracker", page_icon="🌱", layout="centered")
    
    users = load_users()
    
    if "user" not in st.session_state:
        st.title("🌱 Growth Mindset Challenge Tracker")
        menu = ["Login", "Register"]
        choice = st.sidebar.selectbox("Menu", menu)

        if choice == "Register":
            st.subheader("Create an Account")
            new_user = st.text_input("Username")
            new_pass = st.text_input("Password", type="password")
            if st.button("Register"):
                if register_user(new_user, new_pass, users):
                    st.success("Account created! You can now log in.")
                else:
                    st.error("Username already exists.")

        elif choice == "Login":
            st.subheader("Login to Your Account")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            
            if st.button("Login"):
                if authenticate(username, password, users):
                    st.session_state["user"] = username
                    st.rerun()
                else:
                    st.error("Invalid username or password.")
    
    if "user" in st.session_state:
        username = st.session_state["user"]
        st.title(f"Welcome, **{username}**!")
        st.write("Here's your challenge for today:")
        challenge = random.choice(CHALLENGES)
        st.info(f"📌 {challenge}")
        
        st.subheader("📝 Reflect on Your Challenge")
        reflection = st.text_area("Write your thoughts and experiences here:")
        if st.button("Submit Reflection"):
            if reflection.strip():
                add_reflection(username, reflection, users)
                st.success("Reflection saved! Keep up the great work.")
            else:
                st.warning("Please write something before submitting.")
        
        st.subheader("📖 Your Growth Journal")
        if users[username]["journal"]:
            for entry in reversed(users[username]["journal"]):
                st.markdown(f"**{entry['date']}** - {entry['reflection']}")
                st.markdown("---")
        else:
            st.write("No reflections yet. Start today!")
        
        if st.button("Logout"):
            del st.session_state["user"]
            st.rerun()

if __name__ == "__main__":
    main()
    st.markdown("""
    <style>
    .footer {
    text-align: center;
    margin-top: 50px;
    color: gray;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown("<div class='footer'>Made with ❤️ using Streamlit</div>", unsafe_allow_html=True)