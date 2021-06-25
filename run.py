# This bot was developed by Chris Pham and Wesley Heath (TM).
# This bot was created for the Discord server UoA Esports.
# All enquiries please contact chrisphamdev@gmail.com
# All use of this bot must be approved by its authors.

# TO RUN THE BOT, RUN THIS FILE
import json

from main import bot

with open('token.json', 'r') as file_to_read:
   token = json.load(file_to_read)

bot.run()
