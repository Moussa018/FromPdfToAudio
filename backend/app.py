from flask import Flask, jsonify
from flask_cors import CORS
from pypdf import PdfReader
from gtts import gTTS

app = Flask(__name__)
CORS(app)  # Allow React frontend to access backend

@app.route('/api/hello')
def hello():
    return jsonify({'message': 'Hello from Flask!'})

@app.route('/api/read_pdf/<path:file_path>')
def read_pdf(file_path):
    try:
        reader = PdfReader(file_path)
    except Exception as e:
        return str(e)

@app.route('/api/extract_text/<path:file_path>')
def extract_text_from_pdf(reader):
    text=''
    for page in reader.pages:
        text += page.extract_text() + '\n'

@app.route('/api/transform_into_audio/<path:text>')
def transform_into_audio(text):
    try:
        tts = gTTS(text=text, lang='en',slow=False)
        audio_file = 'output.mp3'
        tts.save(audio_file)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
