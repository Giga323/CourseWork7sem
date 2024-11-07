from fastapi import FastAPI
import uvicorn
import google.generativeai as ai
from config import API_KEY

ai.configure(api_key=API_KEY)
model = ai.GenerativeModel("gemini-pro")

chat = model.start_chat()

app = FastAPI()

@app.post('/chat-bot/send-message')
def sendMessage(message: str = None):
    print(message)
    response = str(chat.send_message(message).text)
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)