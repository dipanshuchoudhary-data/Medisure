# Medisure
 # 🩺 AI Doctor - Text-to-Speech Voice Module

This module provides text-to-speech (TTS) functionality using both **gTTS (Google Text-to-Speech)** and **ElevenLabs** APIs, supporting **audio generation** and **cross-platform playback**. It is part of the larger **AI Doctor** project, designed to simulate interactive AI-powered medical consultation.

---

## 🎯 Features

- 🔊 Convert text to audio using:
  - 🗣️ gTTS (Google)
  - 🧠 ElevenLabs (Realistic voice synthesis)
- 🎧 Cross-platform audio playback:
  - Windows
  - macOS
  - Linux
- 🔐 Secure use of API keys via `.env` or environment variables
- 🔄 Modular and reusable TTS interface

---

## 🧪 Dependencies

Install required libraries:

```bash
pip install gtts elevenlabs python-dotenv
