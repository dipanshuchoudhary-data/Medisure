
import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO

AudioSegment.converter = r"C:\ffmpeg\ffmpeg-7.1.1-full_build\bin\ffmpeg.exe"


logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
def record_audio(file_path,timeout=10,phrase_time_limit=None):
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source,duration=1)
            logging.info("Start speaking now...")

            # Record audio

            audio_data = recognizer.listen(source,timeout=timeout,phrase_time_limit=phrase_time_limit)
            logging.info("Recording complete")

            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path,format="mp3",bitrate="128k")

            if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
                logging.info(f"Audio saved: {file_path}")
            else:
                logging.error("Exported file is empty or missing. Skipping transcription.")
                return


    except Exception as e:
        logging.error(f"An error occurred: {e}")


audio_filepath = "patient_voice_test_1.mp3"


import os
from groq import Groq

GROQ_API_KEY =os.environ.get("GROQ_API_KEY")
stt_model = "whisper-large-v3"

def transcribe_with_groq(stt_model,audio_filepath,GROQ_API_KEY):
    client=Groq(api_key=GROQ_API_KEY)

    with open(audio_filepath, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
          model=stt_model,
          file=audio_file,
          language='en'
    )


    return transcription.text


if __name__ == "__main__":
    record_audio(audio_filepath)
    if GROQ_API_KEY:
        transcript = transcribe_with_groq(stt_model, audio_filepath, GROQ_API_KEY)
        print("Transcription:", transcript)
    else:
        logging.error("GROQ_API_KEY is not set in environment variables.")
