# 🤖 HealthBuddy - AI Health Chatbot

HealthBuddy is a simple, user-friendly chatbot that helps users get basic advice for common health issues like fever, cold, headache, stomach pain, and more. 
It simulates a natural doctor-like conversation using YAML-based logic.

## 🔍 Features

- Guides users through symptoms with follow-up questions
- Suggests basic medicines and precautions
- Uses easy language to explain health issues
- YAML-based conversation flow
- Helps users decide when to see a doctor

## 📁 Project Structure

HealthBuddy/
├── data/
├── saved_conversations/
├── static/ # CSS/JS/Images
├── templates/ # HTML Templates (signup.html, etc.)
├── users.yml # YAML-based user/condition flow
├── run.py # Flask app main entry
├── train.py # Chatbot training logic
├── speech.py # Voice input/output (TTS/STT)
└── README.md # This file

Each YAML file contains:
- Condition details
- Symptom-based questions
- Medicine suggestions
- Advice and warning signs

## 🚀 How to Use

1. Clone or download this repository.
2. Run the chatbot interface using your Python file (or load YAMLs into your chatbot framework).
3. Select or type the issue (e.g., "I have a headache").
4. Chatbot starts asking questions and gives advice.

## 🔧 Tech Used

- Python (for logic)
- YAML (for chatbot flow)
- web-based interface

## 📌 Example

"""yaml
condition: Fever
questions:
  - Do you have a high temperature?
  - Are you feeling chills or body pain?
advice:
  - Take rest and stay hydrated.
  - You can take paracetamol if the fever is above 100°F.
see_doctor_if:
  - Fever lasts more than 3 days
  - Severe body pain or rashes appear

💡 Future Improvement
1.Connect with a real doctor on escalation
2.Add a web or mobile UI

👤 Developed By
RAHULRAJU SANGARAJU
B.Tech CSE | Health-focused Tech Enthusiast
Email: rahulrajusangaraju@gmail.com
