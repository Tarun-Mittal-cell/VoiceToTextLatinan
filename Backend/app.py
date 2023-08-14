from flask import Flask, request, jsonify
from flask_cors import CORS
from google.cloud import speech_v1 as speech

app = Flask(__name__)
CORS(app)


@app.route("/voice-to-text", methods=["POST"])
def voice_to_text():
    try:
        audio_file = request.files["file"]

        client = speech.SpeechClient()

        content = audio_file.read()
        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
            sample_rate_hertz=16000,
            language_code="en-US",
        )

        response = client.recognize(config=config, audio=audio)

        if not response.results:
            return jsonify({"error": "Could not understand audio"}), 400

        transcript = response.results[0].alternatives[0].transcript

        return jsonify({"transcript": transcript})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
