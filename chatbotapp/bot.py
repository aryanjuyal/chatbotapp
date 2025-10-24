from google import genai
from PIL import Image
from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")




client = genai.Client()

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


      
