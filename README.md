# VoiceToTextOutco 

VoiceToTextOutco is a tool that leverages speech recognition to convert audio speech into text transcripts. This README provides instructions on setting up and running the project.

## Description

This project utilizes the Google Speech-to-Text API to transcribe audio files into text. Some key features:

- Converts `.wav` audio files into text
- Easy to set up with Python dependencies
- Customizable for different audio sources

## Usage
- Send a POST request to /transcribe with a .wav audio file to get a text transcript back
- Customize app.py and transcribe.py as needed for different audio sources


### Prerequisites

Before running this project, you will need:

- Python 3.7+
- A Google Cloud Platform account with Speech-to-Text API enabled
- Google Cloud service account credentials JSON file

### Setup

1. Clone the repository

   ```bash
   git clone https://github.com/Tarun-Mittal-cell/VoiceToTextOutco.git
   cd VoiceToTextOutco

2. Create and activate a virtual environment

   ```bash
   python3 -m venv myenv  
   source myenv/bin/activate

3. Install dependencies

   ```bash
   pip install -r requirements.txt

4. Set up Google Cloud credentials

   ```bash
   Place your google_cloud_key.json file in the secrets directory
   Set GOOGLE_APPLICATION_CREDENTIALS environment variable to point to secrets/google_cloud_key.json

5. Run the app

   ```bash
   python app.py

### Contributing

Contributions are welcome! Please open an issue or pull request for any enhancements or bug fixes.









