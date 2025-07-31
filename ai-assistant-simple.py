#ai assistant simple
#install openai

import openai
import pyttsx3

openai.api_key = "" #add your openai API

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
question = input(" Ask the ai something: ")

response = openai.ChatCompletition.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": question}]
)

reply = response['choices'][0][message]['content']
print(f"AI: {reply}")
speak(reply)
