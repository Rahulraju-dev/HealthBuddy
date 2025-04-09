"""1st cde with out voice and correct output  
import speech_recognition as sr
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



english_bot = ChatBot('Bot',
             storage_adapter='chatterbot.storage.SQLStorageAdapter',
             logic_adapters=[
   {
       'import_path': 'chatterbot.logic.BestMatch'
   },
   
],
trainer='chatterbot.trainers.ListTrainer')
english_bot.set_trainer(ListTrainer)
r = sr.Recognizer()

speech = sr.Microphone(device_index=0)

while True:
    with speech as source:
        print("say something!...")
        audio = r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        recog = r.recognize_google(audio, language = 'en-US')
        print("You said: " + recog)
        response = str(english_bot.get_response(recog))
        print("Jarvis:"+response)
        appendfile=os.listdir('saved_conversations')[-1]
        appendfile= open('saved_conversations/'+str(filenumber),"a")
        appendfile.write('user : '+recog+'\n')
        appendfile.write('bot : '+response+'\n')
        appendfile.close()
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


"""
#2nd 
import speech_recognition as sr
import pyttsx3
import os
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Initialize Text-to-Speech
engine = pyttsx3.init()
engine.setProperty("rate", 150)  # Adjust speaking speed
engine.setProperty("volume", 1)  # Set volume level

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

# Create or fetch the latest conversation file
if not os.path.exists("saved_conversations"):
    os.makedirs("saved_conversations")

conversation_files = os.listdir("saved_conversations")
filenumber = int(conversation_files[-1]) + 1 if conversation_files else 1

with open(f"saved_conversations/{filenumber}", "w+") as file:
    file.write('bot : Hi There! I am a medical chatbot. You can begin conversation by speaking.\n')

# Initialize ChatBot
english_bot = ChatBot('Bot',
                      storage_adapter='chatterbot.storage.SQLStorageAdapter',
                      logic_adapters=[{'import_path': 'chatterbot.logic.BestMatch'}])

trainer = ListTrainer(english_bot)  # Fix ListTrainer initialization

# Initialize Speech Recognizer
recognizer = sr.Recognizer()
mic = sr.Microphone(device_index=0)

# Start Listening
while True:
    with mic as source:
        print("Say something!...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            print("Listening...")
            audio = recognizer.listen(source, timeout=5)
            recog_text = recognizer.recognize_google(audio, language='en-US')
            print("You said: " + recog_text)

            # Get ChatBot response
            response = str(english_bot.get_response(recog_text))
            print("Jarvis: " + response)

            # Speak the chatbot response
            speak(response)

            # Save conversation
            with open(f"saved_conversations/{filenumber}", "a") as appendfile:
                appendfile.write(f"user : {recog_text}\n")
                appendfile.write(f"bot : {response}\n")

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            speak("I didn't understand that. Please try again.")
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service")
            speak("There was an error connecting to Google Speech API. Please check your internet.")
        except sr.WaitTimeoutError:
            print("No speech detected. Try again.")
            speak("No speech detected. Please try again.")
