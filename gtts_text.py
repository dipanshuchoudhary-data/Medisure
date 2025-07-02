
from gtts import gTTS
import os
import platform
import subprocess

text = "Hello Dipanshu, your gTTS setup is working!"
language = "en"

speech = gTTS(text=text, lang=language, slow=False)
output_file = "gtts_test.mp3"
speech.save(output_file)

# Auto-play based on OS
os_name = platform.system()
if os_name == "Windows":
    subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_file}").PlaySync();'])
elif os_name == "Darwin":  # macOS
    subprocess.run(['afplay', output_file])
elif os_name == "Linux":
    subprocess.run(['aplay', output_file])
else:
    print("Unsupported OS for playback")

print("✅ gTTS audio generated and played successfully.")
