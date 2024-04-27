Discord Bot: Automated Pinging Bot
!Bot Logo

Description
This Discord bot performs automated pinging in specified channels. The bot sends messages mentioning everyone (@everyone) at regular intervals. It’s designed to be customizable, allowing you to choose the target channel and adjust the ping frequency.

Features
Customizable channel selection
Adjustable ping rate
Simple and straightforward setup
Installation
Clone this repository to your local machine.
Install the required dependencies using the following command:
pip install -r requirements.txt

Create a config.json file with the following structure:
JSON

{
    "spam_guild_id": "your_guild_id",
    "ping_role_id": "your_role_id",
    "bot_token": "your_bot_token"
}
AI-generated code. Review and use carefully. More info on FAQ.
Replace the placeholders with actual values from your Discord server and bot.
Usage
Run the bot using the command:
python bot.py

Invite the bot to your Discord server.
Use the !ping command to trigger the pinging process.
Contributing
Contributions are welcome! Please fork this repository and create a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Feel free to modify and enhance this README according to your project’s needs. Good luck with your Discord bot! 🚀
