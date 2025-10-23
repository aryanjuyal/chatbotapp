from google import genai
from PIL import Image
from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("GEMINI_API_KEy")




client = genai.Client(api_key=api_key)

def gemini(prompt,image=None):
   contents = [prompt]
   if image:
        img = Image.open(image)
        contents.append(img)
  


    
   response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=contents
        
       
    )
   return response.text


# NOTES FOR FUTURE


 # config=types.GenerateContentConfig(
        # thinking_config=types.ThinkingConfig(thinking_budget=0)
        #   config=types.GenerateContentConfig(
        # system_instruction="You are a cat. Your name is Neko."),
      
