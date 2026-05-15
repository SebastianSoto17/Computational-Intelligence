from openai import OpenAI
import os
from dotenv import load_dotenv

SYSTEM_MESSAGE = "You are a chatbot. You will have a conversation with a user. Be friendly and concise"

if __name__ == "__main__":
    load_dotenv()
    URL = os.environ.get('OPENAI_BASE_URL')
    KEY = os.environ.get('OPENAI_KEY') or os.environ.get('OPENAI_API_KEY')
    MODEL = os.environ.get('MODEL', '').strip()

    if not KEY:
        raise RuntimeError('Missing OpenAI API key. Set OPENAI_KEY or OPENAI_API_KEY in your environment.')
    if not URL:
        raise RuntimeError('Missing OpenAI base URL. Set OPENAI_BASE_URL in your environment.')
    if not MODEL:
        raise RuntimeError('Missing model name. Set MODEL in your environment.')

    client = OpenAI(
        base_url=URL,
        api_key=KEY,
    )

    print(f"Chatting with {MODEL} model at {URL}\n")

    message_history = [
        {'role': 'system', 'content': SYSTEM_MESSAGE}
    ]

    while True:
        message = input("> ")
        message_history.append({'role': 'user', 'content': message})

        response = client.chat.completions.create(
            model=MODEL,
            messages=message_history
        )

        bot_message = response.choices[0].message.content
        print(bot_message)

        message_history.append({'role': 'assistant', 'content': bot_message})
