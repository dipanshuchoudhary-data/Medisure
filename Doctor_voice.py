# print(">>> Doctor_voice.py is running...")

# import os
# import platform
# import subprocess
# from gtts import gTTS
# from elevenlabs import generate, save, Voice, VoiceSettings

# # Get ElevenLabs API Key from environment
# ELEVENLABS_KEY = os.environ.get("ELEVENLABS_KEY")

# # ===== gTTS: Save Only =====
# def text_to_speech_gtts_pre(input_text, output_filepath):
#     language = "en"
#     audio = gTTS(text=input_text, lang=language, slow=False)
#     audio.save(output_filepath)

# # ===== gTTS: Save and Auto-Play =====
# def text_to_speech_gtts_new(input_text, output_filepath):
#     language = "en"
#     audio = gTTS(text=input_text, lang=language, slow=False)
#     audio.save(output_filepath)

#     os_name = platform.system()
#     try:
#         if os_name == "Darwin":
#             subprocess.run(['afplay', output_filepath])
#         elif os_name == "Windows":
#             print("⚠️ Windows cannot autoplay MP3 directly from script. Use Streamlit's audio player instead.")
#         elif os_name == "Linux":
#             subprocess.run(['aplay', output_filepath])
#         else:
#             raise OSError("Unsupported OS")
#     except Exception as e:
#         print(f"Playback error: {e}")

# # ===== ElevenLabs: Save Only =====
# def text_to_speech_with_elevenlabs(input_text, output_filepath):
#     if not ELEVENLABS_KEY:
#         raise EnvironmentError("ELEVENLABS_KEY not set in environment variables.")

#     audio = generate(
#         text=input_text,
#         voice=Voice(
#             voice_id="EXAVITQu4vr4xnSDxMaL",  # Aria's default ID; replace if needed
#             settings=VoiceSettings(stability=0.75, similarity_boost=0.75)
#         ),
#         model="eleven_turbo_v2",
#         api_key=ELEVENLABS_KEY,
#         output_format="mp3_22050_32"
#     )
#     save(audio, output_filepath)

# # ===== ElevenLabs: Save and Auto-Play =====
# def text_to_speech_elevenlabs(input_text, output_filepath):
#     text_to_speech_with_elevenlabs(input_text, output_filepath)

#     os_name = platform.system()
#     try:
#         if os_name == "Darwin":
#             subprocess.run(["afplay", output_filepath])
#         elif os_name == "Windows":
#             print("⚠️ Windows cannot autoplay MP3 directly from script. Use Streamlit's audio player instead.")
#         elif os_name == "Linux":
#             subprocess.run(["aplay", output_filepath])
#         else:
#             raise OSError("Unsupported OS")
#     except Exception as e:
#         print(f"Playback error: {e}")


# # For manual script testing
# if __name__ == "__main__":
#     test_text = "This is a test message from ElevenLabs."
#     test_output = "test_elevenlabs.mp3"
#     text_to_speech_with_elevenlabs(test_text, test_output)
#     print(f"✅ ElevenLabs audio saved to: {test_output}")




# if you dont use pipenv uncomment the following:
# from dotenv import load_dotenv
# load_dotenv()




#Step1a: Setup Text to Speech–TTS–model with gTTS
# import os
# from gtts import gTTS

# def text_to_speech_gtts_pre(input_text, output_filepath):
#     language="en"

#     audioobj= gTTS(
#         text=input_text,
#         lang=language,
#         slow=False
#     )
#     audioobj.save(output_filepath)


# input_text="Hi this is Ai with Hassan!"
# text_to_speech_gtts_pre(input_text=input_text, output_filepath="gtts_testing.mp3")

# #Step1b: Setup Text to Speech–TTS–model with ElevenLabs
# import elevenlabs
# from elevenlabs.client import ElevenLabs

# ELEVENLABS_API_KEY=os.environ.get("ELEVEN_API_KEY")

# def text_to_speech_elevenlabs_pre(input_text, output_filepath):
#     client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
#     audio=client.generate(
#         text= input_text,
#         voice= "Aria",
#         output_format= "mp3_22050_32",
#         model= "eleven_turbo_v2"
#     )
#     elevenlabs.save(audio, output_filepath)

# #text_to_speech_with_elevenlabs_old(input_text, output_filepath="elevenlabs_testing.mp3") 

# #Step2: Use Model for Text output to Voice

# import subprocess
# import platform

# def text_to_speech_with_gtts(input_text, output_filepath):
#     language="en"

#     audioobj= gTTS(
#         text=input_text,
#         lang=language,
#         slow=False
#     )
#     audioobj.save(output_filepath)
#     os_name = platform.system()
#     try:
#         if os_name == "Darwin":  # macOS
#             subprocess.run(['afplay', output_filepath])
#         elif os_name == "Windows":  # Windows
#             subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
#         elif os_name == "Linux":  # Linux
#             subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
#         else:
#             raise OSError("Unsupported operating system")
#     except Exception as e:
#         print(f"An error occurred while trying to play the audio: {e}")


# input_text="Hi this is Ai with Hassan, autoplay testing!"
# #text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing_autoplay.mp3")


# def text_to_speech_with_elevenlabs(input_text, output_filepath):
#     client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
#     audio=client.generate(
#         text= input_text,
#         voice= "Aria",
#         output_format= "mp3_22050_32",
#         model= "eleven_turbo_v2"
#     )
#     elevenlabs.save(audio, output_filepath)
#     os_name = platform.system()
#     try:
#         if os_name == "Darwin":  # macOS
#             subprocess.run(['afplay', output_filepath])
#         elif os_name == "Windows":  # Windows
#             subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
#         elif os_name == "Linux":  # Linux
#             subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
#         else:
#             raise OSError("Unsupported operating system")
#     except Exception as e:
#         print(f"An error occurred while trying to play the audio: {e}")

#text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_testing_autoplay.mp3")



# import os
# import platform
# import subprocess
# from gtts import gTTS

# from elevenlabs import generate, save, Voice, VoiceSettings, set_api_key

# # Set the API key
# ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
# set_api_key(ELEVENLABS_API_KEY)

# # gTTS basic TTS
# def text_to_speech_with_gtts(input_text, output_filepath):
#     tts = gTTS(text=input_text, lang='en', slow=False)
#     tts.save(output_filepath)

# # ElevenLabs TTS (corrected method)
# def text_to_speech_with_elevenlabs(input_text, output_filepath):
#     if not ELEVENLABS_API_KEY:
#         raise EnvironmentError("ELEVENLABS_API_KEY not set in environment variables.")
    
#     audio = generate(
#         text=input_text,
#         voice=Voice(
#             voice_id="EXAVITQu4vr4xnSDxMaL",  # "Aria" voice ID
#             settings=VoiceSettings(stability=0.75, similarity_boost=0.75)
#         ),
#         model="eleven_turbo_v2",
#         output_format="mp3_22050_32"
#     )
#     save(audio, output_filepath)

#     # Optional auto-play
#     os_name = platform.system()
#     try:
#         if os_name == "Darwin":
#             subprocess.run(["afplay", output_filepath])
#         elif os_name == "Windows":
#             subprocess.run(["powershell", "-c", f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
#         elif os_name == "Linux":
#             subprocess.run(["aplay", output_filepath])
#     except Exception as e:
#         print(f"Audio playback error: {e}")




print(">>> Doctor_voice.py is running...")

import os
import platform
import subprocess
from gtts import gTTS
from elevenlabs.client import ElevenLabs
from elevenlabs import save

# Get API Key from environment
ELEVEN_API_KEY = os.environ.get("ELEVEN_API_KEY")


# ========== gTTS - Save Only ==========
def text_to_speech_gtts_pre(input_text, output_filepath):
    language = "en"
    audio = gTTS(text=input_text, lang=language, slow=False)
    audio.save(output_filepath)


# ========== gTTS - Save and Auto-play ==========
def text_to_speech_gtts_new(input_text, output_filepath):
    language = "en"
    audio = gTTS(text=input_text, lang=language, slow=False)
    audio.save(output_filepath)

    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name == "Linux":
            subprocess.run(['aplay', output_filepath])
        else:
            raise OSError("Unsupported OS")
    except Exception as e:
        print(f"Playback error: {e}")


# ========== ElevenLabs - Save and Auto-play ==========
def text_to_speech_with_elevenlabs(input_text, output_filepath):
    if not ELEVEN_API_KEY:
        raise EnvironmentError("ELEVEN_API_KEY not found in environment variables.")

    # Initialize client
    client = ElevenLabs(api_key=ELEVEN_API_KEY)

    # Get Voice ID for "Aria"
    voices = client.voices.get_all()
    voice_id = next((v.voice_id for v in voices.voices if v.name.lower() == "aria"), None)

    if not voice_id:
        raise ValueError("Voice 'Aria' not found in ElevenLabs voice list.")

    # Generate speech
    audio = client.text_to_speech.convert(
        voice_id=voice_id,
        text=input_text,
        model_id="eleven_turbo_v2",
        output_format="mp3_22050_32"
    )

    # Save audio
    save(audio, output_filepath)

    # Auto-play audio
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(["afplay", output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(["aplay", output_filepath])
        else:
            raise OSError("Unsupported OS")
    except Exception as e:
        print(f"Playback error: {e}")


# ========== Test Block ==========
if __name__ == "__main__":
    test_text = "This is a test message from gTTS."
    output_path = "test_output.mp3"
    text_to_speech_gtts_pre(test_text, output_path)
    print(f"✅ gTTS audio saved to: {output_path}")
