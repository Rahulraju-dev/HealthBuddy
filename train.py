from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

try:
	os.remove("db.sqlite3")
	print("Old database removed. Training new database")
except:
	print('No database found. Creating new database.')

english_bot = ChatBot('Bot')
english_bot.set_trainer(ListTrainer)
for file in os.listdir('data'):
        print('Training using '+file)
        convData = open('data/' + file).readlines()
        english_bot.train(convData)
        print("Training completed for "+file)
    
"""no db needed
import yaml
import os

DATA_FOLDER = "data/"
responses = {}

# Load YAML files and store responses
for file in os.listdir(DATA_FOLDER):
    if file.endswith(".yml"):
        filepath = os.path.join(DATA_FOLDER, file)
        with open(filepath, "r", encoding="utf-8") as yml_file:
            data = yaml.safe_load(yml_file)
            responses.update(data)  # Merge all responses into a dictionary

print("Training completed! Loaded responses from YAML files.")
"""
