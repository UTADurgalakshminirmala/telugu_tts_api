# Telugu TTS API

A simple API to generate Telugu text-to-speech audio using **Python** + **FastAPI**.

## Features

- Accepts input text and language code (default: `te` for Telugu)  
- Converts the text into an MP3 audio file  
- Returns the audio file as a response  
- Protects access via a custom API key header  

---

## Requirements

- **Python 3.11+**  
- Python packages: `fastapi`, `uvicorn`, `gtts`, `pydantic`  
- An environment variable `API_KEY` set to your secret key  

---

##  Setup & Run

1. **Clone the project**
   ```bash
   git clone https://github.com/UTADurgalakshminirmala/telugu_tts_api.git
   cd telugu_tts_api


2.Create and activate a virtual environment
python -m venv .venv
.\.venv\Scripts\activate   # Windows
# or
source .venv/bin/activate  # Linux / macOS

3.Install dependencies
pip install -r requirements.txt

4.Api key in terminal
# Windows PowerShell
$env:API_KEY = "h830-5534-980-8639N"
5.uvicorn api:app --reload

6.Open the docs interface:
http://127.0.0.1:8000/docs

Example Request

POST /generate_tts/

Headers:

Ai-Dubbing-API-Key: h830-5534-980-8639N


Body:

{
  "text": "నమస్కారం! మీరు ఎలా ఉన్నారు?",
  "lang": "te"
}


Response: MP3 file containing the spoken Telugu text.

Project Structure
.
├── api.py             # Main FastAPI app
├── requirements.txt   # Dependencies
├── audio_outputs/     # Generated MP3 files
└── README.md          # Project documentation
