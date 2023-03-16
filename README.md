# AI Chatbot with GPT-3.5 Turbo

This is a simple AI chatbot that uses OpenAI's GPT-3.5 Turbo language model to generate responses to user input. The chatbot uses Gradio for an interactive web interface.

## Installation

1. Clone the repository: `git clone https://github.com/yourusername/ai-chatbot-gpt-3.5-turbo.git`
2. Install the required packages: `pip install -r requirements.txt`
3. Set up an OpenAI API key by following the instructions [here](https://platform.openai.com/account/api-keys)
4. Add your API key to the `YOUR_API_KEY` field in `api.py`

## Usage

To start the chatbot, run `main.py` using Python 3:

    python main.py

The chatbot will launch a Gradio web interface where you can enter your input and view the conversation history. The chatbot will generate a response using the GPT-3.5 Turbo model.

To end the chatbot, close the web interface.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

* This chatbot was inspired by the [OpenAI GPT-3 Playground](https://beta.openai.com/playground/)
* The GPT-3.5 Turbo model is provided by [OpenAI](https://openai.com/)
* This chatbot was inspired by this project "https://github.com/kydycode/chatgpt-3.5-turbo" and iterated on using GPT-4 and Copilot 
