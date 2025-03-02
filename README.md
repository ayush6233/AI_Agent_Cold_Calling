AI Agent for Cold Calling (Hinglish)
Project Description
This project implements an AI agent capable of conducting personalized, human-like cold calls in Hinglish for various scenarios:

Demo Scheduling: Scheduling ERP system demos.
Candidate Interviewing: Conducting initial screening interviews.
Payment/Order Follow-up: Reminding customers to release payments or place orders.
The agent leverages natural language processing, text-to-speech (TTS), and speech-to-text (STT) functionalities to simulate realistic conversations.

Features
Multi-Scenario Support:
Handles demo scheduling, candidate interviewing, and payment follow-up.
Integration with External Services:
Stub integrations for Calendar, CRM, and Payment systems.
Conversational AI:
Uses OpenAI's GPT-3.5-turbo for generating context-aware responses and questions.
Hinglish Communication:
Designed to interact in a mix of Hindi and English.
Voice Interaction:
Incorporates gTTS for TTS and SpeechRecognition for STT.
Project Structure
main.py: Entry point to run the AI agent across different scenarios.
agent.py: Contains the core AI agent logic including prompt generation and response handling.
config.py: Manages configuration and environment variables.
tts_stt.py: Implements text-to-speech and speech-to-text functionalities.
integration.py: Provides stub integrations for calendar, CRM, and payment systems.
conversation_manager.py: Manages conversation state and context.
Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/AI_Agent_Cold_Calling.git
cd AI_Agent_Cold_Calling
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
Note: Ensure that ffmpeg is installed on your system. In tts_stt.py, set the path to ffmpeg.exe and ffprobe.exe:

python
Copy
Edit
from pydub import AudioSegment
AudioSegment.converter = r"C:\path\to\ffmpeg.exe"
AudioSegment.ffprobe = r"C:\path\to\ffprobe.exe"
Replace the paths with the actual installation locations on your system.

3. Configure Environment Variables
Create a .env file in the project root based on the provided .env.example file.
Populate it with the necessary API keys and configuration settings, for example:
ini
Copy
Edit
OPENAI_API_KEY=your_openai_api_key_here
CALENDAR_API_KEY=your_calendar_api_key_here
CRM_API_KEY=your_crm_api_key_here
LLM_MODEL_NAME=microsoft/DialoGPT-medium
EMBEDDINGS_MODEL=sentence-transformers/all-MiniLM-L6-v2
Models & Data
Language Model:
Utilizes OpenAI's GPT-3.5-turbo for conversational responses. A fallback model (microsoft/DialoGPT-medium) is also integrated.
Embeddings:
Uses the model from sentence-transformers/all-MiniLM-L6-v2 for generating text embeddings.
Datasets:
Sample datasets for training or fine-tuning are included in the /data directory. If the fine-tuned model is too large to include, instructions for downloading or recreating it are provided here.
Architecture Overview
The project consists of several key components:

AIAgent:
Manages the generation of prompts, responses, and handles fallback mechanisms.
ConversationManager:
Keeps track of conversation context and state.
Integrations:
Contains stub implementations for external services like Calendar, CRM, and Payment systems.
TTS/STT Modules:
Implement voice input/output using gTTS and SpeechRecognition.
Demonstration Video
Watch the demonstration video on LOOM:
Demo Video Link

Feature Status
Demo Scheduling: Fully implemented (user provides slot details).
Candidate Interviewing: Fully implemented.
Payment Follow-up: Fully implemented.
Advanced Integrations (State Management, External APIs): Partially implemented (stubs provided).
Error Handling & Enhancements: Basic error handling is in place; additional features may be further refined.
Running the Project
To run the project, execute:

bash
Copy
Edit
python main.py
Follow the on-screen prompts to select a scenario and interact with the agent.

Loom video link -- https://www.loom.com/share/37d3b90f6ce3468186fdd0a35b71bcca?sid=e04548bb-ace9-4a35-b1e1-94c19d2cb5b9


