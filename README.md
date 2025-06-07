# Spyfall Discord Bot [(Rules)](https://www.spyfall.app/gamerules)

## Created by Nathan Carpenter and Nicholas Dillon

![image](https://github.com/Nathan-Carpenter-Git/Spyfall-Discord-Bot/assets/144058518/5acaedfe-1a82-4b51-afef-3b8ed5abbf33)

## About
Lightweight Spyfall Discord bot inspired from Spyfall web page designed by Alexandr Ushan and Hobby World. The Spyfall Discord bot currently has 27 new locations not covered by original Spyfall game with the ability to add your own!

## Running the bot
- This bot has been tested using Heroku, this means it will consume $0.01 per hour, or around $7.20 per month if left on constantly.
- You can turn off the bot when you're not using it to save your money.

## Setup
- Download the bot from release or from ZIP.
- Extract the bot into a folder. (IMPORTANT: Don't put it where other files are, make sure all bot files are alone in their own folder)
- Create a Discord bot of your own through the Discord Developer Portal. [link](https://discord.com/developers/applications)
- Get your client secret token from OAuth2 bot page on the portal.
- Input client secret token into Spyfall.py file via: "client.run('INPUT SECRET HERE')" at the last line.
- Invite your Discord bot into a server via OAuth2 bot page through the bot URL generator. (Bot -> Administrator -> Paste URL into browser)
- Create Heroku account. [link](https://dashboard.heroku.com/apps)
- Create new Heroku app. (New -> Create new app)
- Deploy the bot files to Heroku following the "Deploy using Heroku Git" tutorial on Heroku or follow this tutorial by PedroTech. [link](https://www.youtube.com/watch?v=DQk3zJlY-eE&t=252s)
- Go to resources tab in Heroku and enable the Python SpyFall.py file.
- At this point the bot should be online in Discord and ready to go.

## Adding more locations
- Go follow the setup to caption image(s) on this repository. [link](https://github.com/Nathan-Carpenter-Git/Image-Captioner/tree/main)
- Add captioned image(s) locations into images folder.
- Add location name(s) into location array in Python.py. (locations = ["Airport Terminal", "Avengers Movie", etc.]) Note: Make sure to add them in order according to image number. (index 0 = 0.png)
- Deploy or redeploy bot files onto Heroku.

## Commands
- !start_game (users) | Example: !start_game @Nathan @James @Sam | DMs everyone their role and starts timer.
- !end_game | Ends game and stops timer.

## Credits
Credits to the designer Alexandr Ushan and Hobby World for creating Spyfall. [Web App](https://spyfall.co/app) | [Game on Amazon](https://www.amazon.com/Cryptozoic-Entertainment-CZE01904-Spyfall-Card/dp/B00Y4TYRT8)
