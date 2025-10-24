from fastapi import FastAPI, File, UploadFile, Form

from .bot import gemini

app = FastAPI()



@app.get("/")
def home():
    return {"message": "hello this is a gemini api"}

@app.post("/chat")
async def chat(prompt: str = Form(...), image: UploadFile = File(None)):
    
    if image:
        response = gemini(prompt, image.file)
    else:
        response = gemini(prompt)
    return {"response": response}