

```markdown
# 🤖 Automated Pinging Bot
```
## Description
This Discord bot is your ultimate pinging companion! It tirelessly sends out notifications to specified channels, mentioning everyone (@everyone) at regular intervals. With its customizable features, you can fine-tune the target channel and adjust the ping frequency to suit your needs.

## Features
- **Customizable Channel Selection:** Choose the channels where the bot will work its magic.
- **Adjustable Ping Rate:** Set the frequency of pings according to your preferences.
- **Simple Setup:** Get up and running in no time with a straightforward installation process.

## Installation
1. **Clone this Repository:** Bring the bot to life by cloning this repository to your local machine.
2. **Install Dependencies:** Use the following command to install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. **Configure Settings:** Create a `config.json` file with the following structure:
   ```json
   {
       "spam_guild_id": "your_guild_id",
       "ping_role_id": "your_role_id",
       "bot_token": "your_bot_token"
   }
   ```
   Make sure to replace the placeholders with actual values from your Discord server and bot.

**To find your Guild ID:
	•	Open Discord in your browser or desktop app.
	•	Right-click on your server’s icon in the sidebar.
	•	Select “Copy ID” from the menu.
	•	Paste this ID as the value for "spam_guild_id".
**To find your Role ID:
	•	Open Discord in your browser or desktop app.
	•	Go to Server Settings > Roles.
	•	Right-click on the role you want to use and select “Copy ID”.
	•	Paste this ID as the value for "ping_role_id".
**To obtain your Bot Token:
	•	Go to the Discord Developer Portal (https://discord.com/developers/applications).
	•	Create a new application and navigate to the “Bot” tab.
	•	Click “Add Bot” and confirm.
	•	Under the bot’s username, click “Copy” to copy the token.
	•	Paste this token as the value for "bot_token".
Note: Keep your bot token secure and never share it publicly.
Make sure to replace the placeholders with the actual values from your Discord server and bot.


## Usage
1. **Run the Bot:** Fire up the bot using the command:
   ```bash
   python bot.py
   ```
2. **Invite to Your Server:** Extend an invitation to the bot to join your Discord server.
3. **No Need for Commands:** Sit back and relax—no commands needed to trigger the pinging process!

## Contributing
🎉 Contributions are more than welcome! Feel free to fork this repository, make your improvements, and create a pull request.

Feel the urge to modify and enhance this README even further? Go ahead, let your creativity flow! Best of luck with your Discord bot adventures! 🚀
```
~topoos