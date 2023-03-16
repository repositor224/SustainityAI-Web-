import openai

class ChatbotAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def send_message(self, message_log):
        # Send a message to the GPT-3.5 Turbo model and receive a response.
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=message_log,
            max_tokens=100,
            temperature=0.7,
        )

        # Extract and return the AI assistant's response.
        return response.choices[0].message.content
