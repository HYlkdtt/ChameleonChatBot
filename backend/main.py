from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import groq
import os
import json
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# CORS middleware to allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

client = groq.Client(api_key=os.environ.get("GROQ_API_KEY"))

chat_history_data = []
style_profile = ""

class ChatRequest(BaseModel):
    message: str

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    global chat_history_data, style_profile
    if not file.filename or not file.filename.endswith('.json'):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a JSON file.")
    
    contents = await file.read()
    try:
        chat_history_data = json.loads(contents)
        # Simple style analysis (can be improved)
        # For now, let's just find the first message from a person and use it.
        # A more complex implementation would analyze multiple messages.
        if chat_history_data and len(chat_history_data) > 0:
             # This is a placeholder for selecting a person and analyzing their style.
             # For now, we'll just take the text of the first message as a "style".
            first_message = chat_history_data[0].get("text", "")
            style_profile = f"Respond in the style of someone who would say: '{first_message}'"

        return {"filename": file.filename, "style_profile_created": bool(style_profile)}
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON file.")

@app.post("/chat/")
async def chat(request: ChatRequest):
    if not style_profile:
        raise HTTPException(status_code=400, detail="No style profile loaded. Please upload a chat history file first.")

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": style_profile
                },
                {
                    "role": "user",
                    "content": request.message,
                }
            ],
            model="llama3-8b-8192",
            max_tokens=150,
            temperature=0.7
        )
        return {"response": chat_completion.choices[0].message.content}
    except Exception as e:
        print(f"Error calling Groq API: {str(e)}")
        raise HTTPException(status_code=500, detail=f"API Error: {str(e)}")

@app.get("/")
def read_root():
    return {"message": "ChameleonChatBot backend is running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
