# SustainityAI Chatbot

SustainityAI Chatbot is a simple AI Chatbot with OpenAI's GPT-3.5 Turbo Language Model API utilized. It includes the function of generating
responses based on user's input about sustainbility questions, along with generating customized computer notifications on possible events that
users can organize based on user's responses about their personal preferences such as their favourite events.

The chatbot is built using Gradio and Python. It runs through web using a local host. A software version using Java and dependencies is also 
available. This project is submitted for the hackathon "AI for change", and is the winner of that hackathon with a 500+ participants.

## Download Pip
If you receive an error "Pip is not recognized..." in powershell or cmd, please do the following:

1. Input 'python --version' in cmd to check whether python is downloaded in the computer. 
2. Go to 'https://pip.pypa.io/en/stable/installation/' 
3. In (2), Download the script, from https://bootstrap.pypa.io/get-pip.py. Leave the name of the script as 'get-pip.py'
4. Record the directory of 'get-pip.py' 
5. Open CMD again. Use cd function until the CMD directory is equal to the get-pip's directory in (4)
6. Input the command 'python get-pip.py' in CMD

## Download git
If you receive an error "git is not recognized" in powershell or cmd, please download 'git' on your computer.

## Installation

1. Clone the repository: `git clone https://github.com/yourusername/ai-chatbot-gpt-3.5-turbo.git`
2. Install the required packages: `pip install -r requirements.txt`
3. Set up an OpenAI API key by following the instructions [here](https://platform.openai.com/account/api-keys)
4. Add your API key to the `YOUR_API_KEY` field (located at Line 13) in `ui.py`

## Usage

To start the chatbot, run `main.py` using Python 3:

    python main.py

CMD will then show a local host website (such as: 'Running on local URL:  http://127.0.0.1:7860')

To end the chatbot, close the web interface.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

* This chatbot was inspired by https://github.com/jacob-dietle/chatbot_template?tab=readme-ov-file, 
* The GPT-3.5 Turbo model is provided by [OpenAI](https://openai.com/)
* This chatbot was inspired by this project "https://github.com/kydycode/chatgpt-3.5-turbo" and iterated on using GPT-4 and Copilot 
