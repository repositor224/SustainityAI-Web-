import gradio as gr
from api import ChatbotAPI

# Initialize the ChatbotAPI with the API key.
chatbot_api = ChatbotAPI(api_key="your_openai_api_key_here")

message_log = []

def chatbot_ui(input_text):
    global message_log

    # Add the user's message to the message log.
    message_log.append({"role": "user", "content": input_text})

    # Send the message_log to the ChatbotAPI and get a response.
    response = chatbot_api.send_message(message_log)

    # Add the AI assistant's response to the message log.
    message_log.append({"role": "assistant", "content": response})

    # Convert the message log to a readable format for display.
    formatted_log = '\n'.join([f"{msg['role'].title()}: {msg['content']}" for msg in message_log])

    return formatted_log

def main():
    # Create the Gradio interface.
    iface = gr.Interface(
        fn=chatbot_ui,
        inputs=gr.components.Textbox(lines=5, label="Your message", placeholder="Type your message here..."),
        outputs=gr.components.Textbox(lines=10, label="Chat History"),
        title="AI Chatbot",
        description="A simple AI chatbot using GPT-3.5 Turbo.",
    )

    # Launch the Gradio interface.
    iface.launch()

if __name__ == "__main__":
    main()
