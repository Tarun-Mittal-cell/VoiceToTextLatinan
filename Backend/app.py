from flask import Flask, request, jsonify
from google.cloud import speech
from google.cloud.speech import enums, types

app = Flask(__name__)

@app.route("/voice-to-text", methods=["POST"])
def voice_to_text():
    audio_file = request.files['file']
    
    client = speech.SpeechClient()

    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=16000,
        language_code='en-US',
    )

    response = client.recognize(config=config, audio=audio)

    if not response.results:
        return jsonify({"error": "Could not understand audio"}), 400

    transcript = response.results[0].alternatives[0].transcript

    return jsonify({"transcript": transcript})

if __name__ == "__main__":
    app.run(debug=True)
