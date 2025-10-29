import logging
from fastapi import FastAPI, Response, HTTPException
from pydantic import BaseModel
from gtts import gTTS
import io

app = FastAPI()

# Enable logging
logging.basicConfig(level=logging.INFO)

# Request model
class TTSRequest(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Welcome to Telugu TTS API! POST text to /tts endpoint"}

@app.post("/tts")
def telugu_tts(request: TTSRequest):
    """
    Convert given text to Telugu TTS (MP3) using gTTS (Google Text-to-Speech).
    """
    text = request.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="Text cannot be empty.")

    try:
        logging.info(f"Generating TTS for text: {text}")

        # Generate the Telugu TTS audio
        tts = gTTS(text=text, lang='te')  # Telugu language
        mp3_fp = io.BytesIO()
        tts.save(mp3_fp)
        mp3_fp.seek(0)  # Reset pointer to the start of the file

        logging.info("TTS generation successful. Returning response.")

        # Return MP3 audio as response
        return Response(
            content=mp3_fp.read(),
            media_type="audio/mpeg",
            headers={"Content-Disposition": "inline; filename=telugu_tts.mp3"}
        )

    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
