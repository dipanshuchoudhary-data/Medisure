import os
import gradio as gr

from main import encode_image, analyze_image
from patient_voice import record_audio, transcribe_with_groq
from Doctor_voice import text_to_speech_gtts_pre, text_to_speech_gtts_new, text_to_speech_with_elevenlabs


# System prompt for AI
system_prompt = """You have to act as a professional doctor, i know you are not but this is for learning purpose. 
What's in this image?. Do you find anything wrong with it medically? 
If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in 
your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
Donot say 'In the image I see' but say 'With what I see, I think you have ....'
Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
Keep your answer concise (max 2 sentences). No preamble, start your answer right away please."""

# Core function
def process_inputs(audio_filepath, image_filepath):
    # Transcribe voice input
    transcription = transcribe_with_groq(
        stt_model="whisper-large-v3",
        audio_filepath=audio_filepath,
        GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
    )

    # Analyze image + transcription
    if image_filepath:
        encoded_img = encode_image(image_filepath)
        response = analyze_image(
            query=system_prompt + transcription,
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            encoded_image=encoded_img
        )
    else:
        response = "No image provided for me to analyze"

    # Convert response to speech
    text_to_speech_with_elevenlabs(input_text=response, output_filepath="final.mp3")

    return transcription, response, "final.mp3"

# Gradio interface
iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath", label="🎙️ Your Voice Input"),
        gr.Image(type="filepath", label="🖼️ Facial Image")
    ],
    outputs=[
        gr.Textbox(label="📝 Transcribed Text"),
        gr.Textbox(label="🧠 AI Doctor's Response"),
        gr.Audio(label="🔊 Doctor's Voice")
    ],
    title="🤖 AI Doctor (Voice + Vision)",
    description="Speak your symptoms and upload your  image. Get a response from a virtual doctor."
)

iface.launch(debug=True)


#http://127.0.0.1:7860