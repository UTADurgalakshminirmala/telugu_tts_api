from gtts import gTTS
import os

# Create a folder to save all output files
output_folder = "audio_outputs"
os.makedirs(output_folder, exist_ok=True)  # Creates folder if it doesn't exist

# Sample Telugu text
text = """గ లోకం మీద ఒక చీకటి సమయం అలుముకుంది. దేవలోకాలను కాపాడడానికి సృష్టించిన పవిత్ర ఆయుధం కట్వాంగ ఇప్పుడు ప్రమాదంలో ఉంది.
తాంత్రిక రుషి వక్రాంత దానిపై తన నీడను వేశాడు, దాని శక్తిని నాశనం కోసం వాడుకోవాలని చూశాడు. 
కట్వాంగాను తిరిగి పొందడానికి మరియు తమ భూమిని కాపాడడానికి, ఒక గొప్ప త్యాగం అవసరం అయ్యింది. అది ఎవరో కాదు, రాణి రేవతి మాత్రమే చేయాలి. 
ఆమె రక్తం ఒక్కటే వక్రాంత తాంత్రిక బంధాన్ని విచ్ఛిన్నం చేయగల శక్తిని కలిగి ఉంది."""

# Generate the TTS
tts = gTTS(text=text, lang='te')

# Save the generated speech to the folder
output_path = os.path.join(output_folder, "output.mp3")
tts.save(output_path)

print(f"Audio saved to {output_path}")
