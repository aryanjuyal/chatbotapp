from fastapi import FastAPI, File, UploadFile, Form
from .bot import gemini

app = FastAPI()
@app.post("/chat")
async def chat(prompt: str = Form(...), image: UploadFile = File(None)):
    if image:
        response = gemini(prompt, image.file)
    else:
        response = gemini(prompt)
    return {"response": response}
