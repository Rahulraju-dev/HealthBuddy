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
"""
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

filenumber=int(os.listdir('saved_conversations')[-1])
filenumber=filenumber+1
file= open('saved_conversations/'+str(filenumber),"w+")
file.write('bot : Hi There! I am a medical chatbot. You can begin conversation by typing in a message and pressing enter.\n')
file.close()

app = Flask(__name__)


english_bot = ChatBot('Bot',
             storage_adapter='chatterbot.storage.SQLStorageAdapter',
             logic_adapters=[
   {
       'import_path': 'chatterbot.logic.BestMatch'
   },
   
],
trainer='chatterbot.trainers.ListTrainer')
english_bot.set_trainer(ListTrainer)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    response = str(english_bot.get_response(userText))

    appendfile=os.listdir('saved_conversations')[-1]
    appendfile= open('saved_conversations/'+str(filenumber),"a")
    appendfile.write('user : '+userText+'\n')
    appendfile.write('bot : '+response+'\n')
    appendfile.close()

    return response


if __name__ == "__main__":
    app.run()
2222222222222222222222222222222222222222222222222222222222222222222222222222222222222

main() file
#added login page ans sign up route
from flask import Flask, render_template, request, redirect, url_for, session
import yaml
import os
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Flask(__name__)
app.secret_key = 'your_random_secret_key_12345'
  # Change this if needed

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
english_bot.set_trainer(ListTrainer)

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
    if 'username' in session:
        return render_template("index.html", username=session["username"])
    return redirect(url_for('login'))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        users = load_users()

        if username in users and users[username] == password:
            session["username"] = username
            return redirect(url_for("home"))
        else:
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
3.33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333"
"
#now adding besst match logic
from flask import Flask, render_template, request, redirect, url_for, session
import yaml
import os
from difflib import get_close_matches  # For best match selection

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this if needed

USERS_FILE = "users.yml"  # YAML file for storing user credentials
DATA_FOLDER = "data/"  # Folder containing YAML response files

# Load users from users.yml
def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as file:
            return yaml.safe_load(file) or {}  # Return empty dict if file is empty
    return {}

# Save users to users.yml
def save_users(users):
    with open(USERS_FILE, "w") as file:
        yaml.safe_dump(users, file)

# Load all responses from YAML files
def load_all_responses():
    responses = {}
    for filename in os.listdir(DATA_FOLDER):
        if filename.endswith(".yml"):
            file_path = os.path.join(DATA_FOLDER, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                yaml_data = yaml.safe_load(file)
                responses.update(yaml_data)  # Merge YAML responses
    return responses

# Ensure 'saved_conversations' folder exists
if not os.path.exists('saved_conversations'):
    os.makedirs('saved_conversations')

filenumber = len(os.listdir('saved_conversations')) + 1
file_path = f'saved_conversations/{filenumber}'
with open(file_path, "w+") as file:
    file.write('bot : Hi There! I am a medical chatbot. Start your conversation now.\n')

# Routes
@app.route("/")
def home():
    if 'username' in session:
        return render_template("index.html", username=session["username"])
    return redirect(url_for('login'))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        users = load_users()

        if username in users and users[username] == password:
            session["username"] = username
            return redirect(url_for("home"))
        else:
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

    userText = request.args.get('msg').lower()  # Convert to lowercase for better matching
    responses = load_all_responses()  # Load all YAML responses

    # Find the best match
    matches = get_close_matches(userText, responses.keys(), n=1, cutoff=0.6)

    if matches:
        bot_response = responses[matches[0]]  # Get response for the best match
    else:
        bot_response = "I'm sorry, I don't have an answer for that."

    # Save conversation to a file
    with open(file_path, "a") as appendfile:
        appendfile.write(f'user : {userText}\n')
        appendfile.write(f'bot : {bot_response}\n')

    return bot_response

if __name__ == "__main__":
    app.run(debug=True)
"""