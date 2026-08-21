import requests
import pyperclip
from dotenv import load_dotenv
import os
import platform

# Load environment variables
load_dotenv()

# Get the DuckDuckGo Access Token from environment variable
ACCESS_TOKEN = os.getenv('DUCKDUCKGO_ACCESS_TOKEN')

USER_AGENTS = {
    "Darwin": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/27.0 "
        "Safari/605.1.15 Ddg/27.0"
    ),
    "Windows": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 "
        "Safari/537.36"
    ),
}


def generate_temp_email():
    if not ACCESS_TOKEN:
        raise RuntimeError(
            "DUCKDUCKGO_ACCESS_TOKEN is not set in the .env file"
        )

    user_agent = USER_AGENTS.get(platform.system())
    if not user_agent:
        raise RuntimeError("Only macOS and Windows are supported")

    url = "https://quack.duckduckgo.com/api/email/addresses"
    headers = {
        "Accept": "*/*",
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Origin": "https://duckduckgo.com",
        "Referer": "https://duckduckgo.com/",
        "User-Agent": user_agent,
    }
    response = requests.post(url, headers=headers, timeout=30)
    if response.status_code == 201:
        address = response.json()['address']
        email = address + "@duck.com"
        pyperclip.copy(email)  # Copy the email to clipboard
        print(f"Temporary email generated and copied to clipboard: {email}")
    else:
        print(f"Error: {response.status_code} - {response.text}")


if __name__ == "__main__":
    generate_temp_email()
