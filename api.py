from fastapi import FastAPI, HTTPException, Header, Depends
from pydantic import BaseModel
from gtts import gTTS
import os
from fastapi.responses import FileResponse
from datetime import datetime

API_KEY = "h830-5534-980-8639N"
API_KEY_NAME = "AI Dubbing Api Key"

app = FastAPI()

output_folder = "audio_outputs"
os.makedirs(output_folder, exist_ok=True)

class TTSRequest(BaseModel):
    text: str
    lang: str = "te"

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API Key")

@app.post("/generate_tts/")
def generate_tts(request: TTSRequest, _: str = Depends(verify_api_key)):
    try:
        tts = gTTS(text=request.text, lang=request.lang)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        filename = f"tts_{timestamp}.mp3"
        output_path = os.path.join(output_folder, filename)
        tts.save(output_path)
        return FileResponse(output_path, media_type="audio/mpeg", filename=filename)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
