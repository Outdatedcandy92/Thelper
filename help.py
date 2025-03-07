import argparse
from google import genai
from google.genai import types
import json
import os
import pyperclip
import inquirer
import json
import sys


def validate_non_empty(answers, current):
    if not current:
        raise inquirer.errors.ValidationError('', reason='This field is required')
    return True

def get_user_input():
    questions = [
        inquirer.Text('api_key', message="Please enter your API key", validate=validate_non_empty),
        inquirer.List('model',
                      message="Please select the model you want",
                      choices=['gemini-1.5-flash', 'gemini-1.5-flash-8b', 'gemini-2.0-flash','gemini-2.0-flash-lite'],
                      carousel=True,
                      default='Gemini 1.5 Flash'),
        inquirer.Text('desktop_os', message="Please enter your OS (be specific eg- Debian 12, Windows 11, etc)", validate=validate_non_empty),
        inquirer.Text('max_token', message="Please enter the max output token value", default='100', validate=validate_non_empty),
        inquirer.Confirm('confirm', message="Confirm?")
    ]

    answers = inquirer.prompt(questions)
    return answers

#Check if settings.json exists
if not os.path.exists('settings.json'):
    print("Settings file not found, initializing setup...")
    user_input = get_user_input()
    settings = {
        "api_key": user_input['api_key'],
        "model": user_input['model'],
        "desktop_os": user_input['desktop_os'],
        "max_token": user_input['max_token'],
        "prompt": f"You are a helpful assistant that helps users with problems regarding {user_input['desktop_os']} terminal commands and {user_input['desktop_os']} commands in general. You should always aim to give the most accurate and helpful response to the user's query and to also always respond as short as possible. Aim to provide user with the relavant command that solves their problem. Format the response but never respond in markdown, you are a tool that prints in terminal where markdown is not supported."
    }
    with open('settings.json', 'w') as settings_file:
        json.dump(settings, settings_file, indent=4)
    print("User settings have been saved to settings.json")
    sys.exit()
    
    

#Load settings.json
with open('settings.json') as f:
    settings = json.load(f)

client = genai.Client(api_key=settings["api_key"])

#Model settings
chat = client.chats.create(
    model=settings["model"],
    config=types.GenerateContentConfig(
        max_output_tokens=settings["max_token"],
        system_instruction=settings["prompt"],
    )
)

#Query function for sending text to the model
def query(text):
    response = chat.send_message_stream(text)
    for chunk in response:
        print(chunk.text, end="")



def main():
    parser = argparse.ArgumentParser(description="A CLI tool that uses Google's Gemini API to help with terminal commands")
    parser.add_argument('text', type=str, nargs='*', help='Sends query to the model')
    parser.add_argument('-i','--init', action='store_true', help='Initialize setup')
    parser.add_argument('-s','--settings', action='store_true', help='Print settings information')
    parser.add_argument('-e','--error', action='store_true', help='Sends the error message to the model')
    args = parser.parse_args()

    if args.init:
        os.system('python setup.py')
        

    if args.settings:
        print(f"API Key: {settings['api_key']}")
        print(f"Model: {settings['model']}")
        print(f"Desktop OS: {settings['desktop_os']}")
        print(f"Max Token: {settings['max_token']}")
        print(f"Prompt: {settings['prompt']}")

    if args.error:
        clipboard_content = pyperclip.paste()
        query(f"Help i got this error: {clipboard_content}")


    input_text = ' '.join(args.text)
    query(input_text)


if __name__ == "__main__":
    main()