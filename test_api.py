import requests

url = "https://chatbotapp-1-49hu.onrender.com/chat"


data = {
    "prompt": "Hello Gemini! Tell me a joke."
}

response = requests.post(url, data=data)

print(response.json())