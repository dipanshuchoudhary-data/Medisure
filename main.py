
import os
GROQ_API_KEY =os.environ.get("GROQ_API_KEY")

import base64
image_path = r"C:\\Users\\DIPANSHU\\OneDrive\\Desktop\\AI_DOCTOR\\AI-Doctor\\acne.png"

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


from groq import Groq

query = "Is there something wrong with my face? And how to cure it"

model = "meta-llama/llama-4-scout-17b-16e-instruct"

def analyze_image(query,model,encoded_image):
    client=Groq()
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }]
    chat_completion=client.chat.completions.create(
        messages=messages,
        model=model
    )

    return chat_completion.choices[0].message.content


from dotenv import load_dotenv
load_dotenv()


# encoded_image = encode_image(image_path)
# response = analyze_image(query,model,encoded_image)
# print("AI Diagnosis : ",response)