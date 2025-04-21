import requests
import pyperclip
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get the DuckDuckGo Access Token from environment variable
ACCESS_TOKEN = os.getenv('DUCKDUCKGO_ACCESS_TOKEN')


def generate_temp_email():
    url = "https://quack.duckduckgo.com/api/email/addresses"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    response = requests.post(url, headers=headers)
    if response.status_code == 201:
        address = response.json()['address']
        email = address + "@duck.com"
        pyperclip.copy(email)  # Copy the email to clipboard
        print(f"Temporary email generated and copied to clipboard: {email}")
    else:
        print(f"Error: {response.status_code} - {response.text}")


if __name__ == "__main__":
    generate_temp_email()