import os

from flask import Flask, jsonify, request
from google.cloud import speech
from google.cloud.speech import RecognitionAudio, RecognitionConfig
from pydub import AudioSegment

app = Flask(__name__, static_url_path="", static_folder="../Frontend")
AudioSegment.converter = "/usr/local/bin/ffmpeg"

# Point to the Google Cloud Service Account Key file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../secrets/google_cloud_key.json"

client = speech.SpeechClient()


def convert_audio(audio_file):
    sound = AudioSegment.from_file(audio_file, format="webm")
    sound = sound.set_channels(1)

    # Convert the audio to 16 bits per sample
    sound = sound.set_sample_width(2)

    sound.export("temp.wav", format="wav")
    return "temp.wav"


@app.route("/voice-to-text", methods=["POST"])
def voice_to_text():
    try:
        audio_file = request.files["audio"]
        path = convert_audio(audio_file)

        with open(path, "rb") as audio_file:
            content = audio_file.read()

        audio = RecognitionAudio(content=content)
        config = RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=48000,
            language_code="en-US",
        )

        response = client.recognize(config=config, audio=audio)

        transcript = ""
        for result in response.results:
            transcript += result.alternatives[0].transcript

        if not transcript:
            return jsonify({"transcript": "No transcription found"}), 200

        return jsonify({"transcript": transcript}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/", methods=["GET"])
def index():
    return app.send_static_file("index.html")


if __name__ == "__main__":
    app.run(debug=True)
