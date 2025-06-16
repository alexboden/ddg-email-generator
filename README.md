# Temporary Email Generator

A simple Python script that generates temporary email addresses by using the DuckDuckGo Email Protection API and copying to your clipboard. Bind the script to a keyboard shortcut for instant access when signing up for new accounts or services.

## Prerequisites

Create a `.env` file in the same directory as the script and add your DuckDuckGo API access token:

   ```
   DUCKDUCKGO_ACCESS_TOKEN=your_access_token_here
   ```

You can find this by going to https://duckduckgo.com/email/settings/autofill and inspecting the network POST requests when generating a new email address.

## Installing Dependencies

To run the script, you need to install the required Python packages. Use the following command to install them:

   ```
   pip install -r requirements.txt
   ```

## Setting Up a Keyboard Shortcut

### macOS

1. Use Automator to create a Quick Action that runs the Python script.
```
python /path/to/this/repo/main.py
```
3. In System Preferences > Keyboard > Shortcuts > Services, assign a keyboard shortcut to this Quick Action.


