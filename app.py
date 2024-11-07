from fastapi import FastAPI
import uvicorn
import google.generativeai as ai

API_KEY = 'AIzaSyD7qu7lAPz-zeyvXBhcAL5E_Q6L3Ock4qs'

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