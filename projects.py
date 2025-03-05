import streamlit as st
import random
import time
import requests

# Apply custom CSS for colorful design and animations
st.markdown(
    """
    <style>
        body {
            background-color: #1e1e1e;
            color: #ffffff;
            font-family: Arial, sans-serif;
        }
        .main-container {
            background: #222;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 4px 15px rgba(255, 255, 255, 0.2);
            width: 70%;
            margin: auto;
            text-align: center;
            animation: fadeIn 1s ease-in-out;
        }
        .stButton>button {
            background: linear-gradient(90deg, #ff8a00, #e52e71);
            color: white;
            border-radius: 8px;
            padding: 12px 24px;
            border: none;
            font-size: 16px;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background: linear-gradient(90deg, #e52e71, #ff8a00);
            transform: scale(1.05);
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="main-container">', unsafe_allow_html=True)

st.title("🎨 Multi-Project Python App 🚀")

# Project selection
project = st.selectbox("Choose a project:", [
    "BMI Calculator",
    "Mad Libs Generator",
    "Guess the Number",
    "Rock, Paper, Scissors",
    "Countdown Timer",
    "Password Generator",
    "To-Do List App",
    "Unit Converter",
    "Weather App",
    "Simple Calculator"
])

if project == "BMI Calculator":
    weight = st.number_input("Enter your weight (kg)", min_value=1.0, format="%.1f")
    height = st.number_input("Enter your height (m)", min_value=0.1, format="%.2f")
    if st.button("Calculate BMI"):
        if height > 0:
            bmi = weight / (height ** 2)
            st.success(f"Your BMI is: {bmi:.2f}")
        else:
            st.error("Height must be greater than zero!")

elif project == "Mad Libs Generator":
    st.subheader("📝 Fill in the blanks!")
    noun = st.text_input("Enter a noun:")
    adjective = st.text_input("Enter an adjective:")
    verb = st.text_input("Enter a verb:")
    place = st.text_input("Enter a place:")
    
    if st.button("Generate Story"):
        if noun and adjective and verb and place:
            story = f"One day, a {adjective} {noun} decided to {verb} at the {place}. It was an amazing experience!"
            st.success(story)
        else:
            st.warning("Please fill in all the blanks!")

elif project == "Guess the Number":
    st.subheader("🔢 Guess the Number!")
    number = random.randint(1, 100)
    guess = st.number_input("Enter a number (1-100):", min_value=1, max_value=100, step=1)
    if st.button("Submit Guess"):
        if guess == number:
            st.success("Congratulations! You guessed the correct number!")
        elif guess < number:
            st.warning("Try a higher number!")
        else:
            st.warning("Try a lower number!")

elif project == "Rock, Paper, Scissors":
    st.subheader("✊✋✌ Rock, Paper, Scissors!")
    choices = ["Rock", "Paper", "Scissors"]
    user_choice = st.selectbox("Choose one:", choices)
    if st.button("Play"):
        comp_choice = random.choice(choices)
        st.write(f"Computer chose: {comp_choice}")
        if user_choice == comp_choice:
            st.info("It's a tie!")
        elif (user_choice == "Rock" and comp_choice == "Scissors") or \
             (user_choice == "Scissors" and comp_choice == "Paper") or \
             (user_choice == "Paper" and comp_choice == "Rock"):
            st.success("You win!")
        else:
            st.error("You lose!")

elif project == "Countdown Timer":
    st.subheader("⏳ Countdown Timer")
    time_sec = st.number_input("Enter time in seconds:", min_value=1, step=1)
    if st.button("Start Countdown"):
        for i in range(time_sec, 0, -1):
            st.write(i)
            time.sleep(1)
        st.success("Time's up!")

elif project == "Password Generator":
    st.subheader("🔐 Password Generator")
    length = st.number_input("Enter password length:", min_value=4, max_value=32, step=1)
    if st.button("Generate Password"):
        password = ''.join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()", k=length))
        st.success(f"Generated Password: {password}")

elif project == "To-Do List App":
    st.subheader("✅ To-Do List App")
    task = st.text_input("Enter a task:")
    if st.button("Add Task"):
        st.write(f"✔ {task}")

elif project == "Unit Converter":
    st.subheader("🔄 Unit Converter")
    km = st.number_input("Enter kilometers:")
    if st.button("Convert to Miles"):
        miles = km * 0.621371
        st.success(f"{km} km is {miles:.2f} miles")

elif project == "Weather App":
    st.subheader("☁️ Weather App")
    city = st.text_input("Enter city name:")
    if st.button("Get Weather"):
        st.warning("Weather API integration needed")

elif project == "Simple Calculator":
    st.subheader("🧮 Simple Calculator")
    num1 = st.number_input("Enter first number:")
    num2 = st.number_input("Enter second number:")
    operation = st.selectbox("Choose operation:", ["Add", "Subtract", "Multiply", "Divide"])
    if st.button("Calculate"):
        if operation == "Add":
            st.success(f"Result: {num1 + num2}")
        elif operation == "Subtract":
            st.success(f"Result: {num1 - num2}")
        elif operation == "Multiply":
            st.success(f"Result: {num1 * num2}")
        elif operation == "Divide":
            st.success(f"Result: {num1 / num2}")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("**Development by @ Suhail Ahmed Aamro**")

