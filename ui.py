import gradio as gr
from api import ChatbotAPI
import tkinter
from tkinter import *
from tkinter import messagebox
from plyer import notification
import schedule
import time
from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler
import random

# Input the API code here please
chatbot_api = ChatbotAPI(api_key="ENTER_YOUR_API_KEY_HERE") 

message_log = []

def notify(input_text):
    notification.notify(
    title = 'important message today!',
    message = input_text,
    )

def chatbot_ui(input_text, your_hobby, sus_event, hour_to_spend, num_act,character):
    if input_text != "" and your_hobby != "" and sus_event != "":
        global message_log
        global formatted_log
        prompt = "A kid has the hobby of" + your_hobby + "and his favourite event is" + sus_event + ". He can spend " + str(hour_to_spend) + " peer week, and has the characteristic of " + character + " . based on above, in 25 words or less, come up with an sustainable event for him."

        # Add the user's message to the message log.
        # Send the message_log to the ChatbotAPI and get a response.

    # try:
        message_log.append({"role": "user", "content": input_text})
        try:
            response = chatbot_api.send_message(message_log)
        except Exception as e:
            notification.notify(
            title = 'Logs and Personal Recommendation Event Cannot be generated!',
            message = str(e),
            )

        responsetwo = chatbot_api.send_message(prompt)
        responsethree = chatbot_api.send_message(prompt)
        responsefour = chatbot_api.send_message(prompt)

        scheduler = BackgroundScheduler()
        scheduler.add_job(notify, 'interval', args=[responsetwo], seconds = randrange(5,20))  
        scheduler.add_job(notify, 'interval', args=[responsethree], seconds = randrange(5,20))
        scheduler.add_job(notify, 'interval', args[responsefour], seconds = randrange(5,20))
        scheduler.start()
        # Add the AI assistant's response to the message log.
        message_log.append({"role": "assistant", "content": response})
        # Convert the message log to a readable format for display.
        formatted_log = '\n'.join([f"{msg['role'].title()}: {msg['content']}" for msg in message_log])
        # except Exception as e:
        #   notification.notify(
        #   title = 'I am sorry but an error occured',
        #   message = e,
        #   )
        return formatted_log
    else:
        window = Tk()
        window.wm_withdraw()
        window.geometry("1x1+500+500")#remember its .geometry("WidthxHeight(+or-)X(+or-)Y")
        tkinter.messagebox.showerror(title="error",message="Please fill all the boxes on the left!",parent=window)


def main():
    # Create the Gradio interface.
    iface = gr.Interface(
        fn=chatbot_ui,
        inputs=[gr.Textbox(label="Yourvalue", placeholder = "Prompts to ChatGPT"), 
        gr.Textbox(label = "Your hobby", placeholder = "What do you like?"), 
        gr.Textbox(label = "Favorite event", placeholder = "Describe an event that you like"),
        gr.Slider(label="Hours for Sustainable event per hour", value = 3, minimum = 1, maximum = 24, step = 1),
        gr.Slider(label="Number of Activities per month", value = 3, minimum = 1, maximum = 24),
        gr.Radio(["Outdoor", "Introvert"], label="Characteristic", info="What is your characteristics")],
        outputs=gr.components.Textbox(lines=10, label="Chat History"),
        title="Sustainity Chatbot",
        description="A simple program providing students with advice on creating a sustainable environment"
    )   
    # Launch the Gradio interface.
    iface.launch()

if __name__ == "__main__":
    main()
