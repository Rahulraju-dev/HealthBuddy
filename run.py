from flask import Flask, render_template, request, redirect, url_for, session
import yaml
import os
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Flask(__name__)
app.secret_key = 'your_random_secret_key_12345'  # Make sure this is long & random

USERS_FILE = "users.yml"  # YAML file for storing user data

# Function to load users from users.yml
def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as file:
            return yaml.safe_load(file) or {}  # Return empty dict if file is empty
    return {}

# Function to save users to users.yml
def save_users(users):
    with open(USERS_FILE, "w") as file:
        yaml.safe_dump(users, file)

# Initialize ChatBot
english_bot = ChatBot('Bot',
                      storage_adapter='chatterbot.storage.SQLStorageAdapter',
                      logic_adapters=[{'import_path': 'chatterbot.logic.BestMatch'}])

trainer = ListTrainer(english_bot)  # Corrected ListTrainer initialization

# Conversation File Management
if not os.path.exists('saved_conversations'):
    os.makedirs('saved_conversations')

filenumber = len(os.listdir('saved_conversations')) + 1
file_path = f'saved_conversations/{filenumber}'
with open(file_path, "w+") as file:
    file.write('bot : Hi There! I am a medical chatbot. You can begin conversation by typing in a message and pressing enter.\n')

# Routes
@app.route("/")
def home():
    if "username" not in session:  # Ensure user must log in first
        return redirect(url_for("login"))
    return render_template("index.html", username=session["username"])


@app.route("/login", methods=["GET", "POST"])
def login():
    print("Login page accessed")  # Debugging

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        users = load_users()

        if username in users and users[username] == password:
            session["username"] = username
            print(f"User {username} logged in successfully")  # Debug log
            return redirect(url_for("home"))
        else:
            print("Login failed")  # Debug log
            return render_template("login.html", error="Invalid username or password")

    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        users = load_users()
        if username in users:
            return render_template("signup.html", error="Username already exists!")

        users[username] = password
        save_users(users)

        return redirect(url_for("login"))

    return render_template("signup.html")

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))

@app.route("/get")
def get_bot_response():
    if 'username' not in session:
        return "Unauthorized access"

    userText = request.args.get('msg')
    response = str(english_bot.get_response(userText))

    with open(file_path, "a") as appendfile:
        appendfile.write(f'user : {userText}\n')
        appendfile.write(f'bot : {response}\n')

    return response

if __name__ == "__main__":
    app.run(debug=True)
