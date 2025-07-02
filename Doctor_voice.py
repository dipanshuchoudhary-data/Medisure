

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
