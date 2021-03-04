import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = discord.Client()
client = commands.Bot(command_prefix=">")

# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
	# CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
	guild_count = 0

	# LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
	for guild in bot.guilds:
		# PRINT THE SERVER'S ID AND NAME.
		print(f"- {guild.id} (name: {guild.name})")

		# INCREMENTS THE GUILD COUNTER.
		guild_count += 1

	# PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
	print("Auto SCP is in " + str(guild_count) + " servers.")

# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(self, message):
	# CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
	if message.content == "hello":
		# SENDS BACK A MESSAGE TO THE CHANNEL.
		await message.channel.send("hi!")
	if self.user.mentioned_in(message) and message.mention_everyone is False:
		if 'help' in message.content.lower():
			await message.channel.send('Eine volle Liste aller Commands gibts hier: https://github.com/Der-Eddy/discord_bot#commands-list')
		else:
			await message.add_reaction('👀') # :eyes:
@client.event    
async def on_message(self, message):
    for x in message.mentions:
        if(x==client.user):
            await message.channel.send(f":sauropod: did someone mention me?")

    await client.process_commands(message)
# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run(TOKEN)