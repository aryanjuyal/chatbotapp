from fastapi import FastAPI, File, UploadFile, Form
from .bot import gemini

app = FastAPI()

@app.get("/")
def base():
    return {"message": "This is my bot api"}


@app.post("/chat")
async def chat(prompt: str = Form(...), image: UploadFile = File(None)):
    if image:
        response = gemini(prompt, image.file)
    else:
        response = gemini(prompt)
    return {"response": response}
