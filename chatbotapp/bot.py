from google import genai
from PIL import Image


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





 # config=types.GenerateContentConfig(
        # thinking_config=types.ThinkingConfig(thinking_budget=0)
        #   config=types.GenerateContentConfig(
        # system_instruction="You are a cat. Your name is Neko."),
      