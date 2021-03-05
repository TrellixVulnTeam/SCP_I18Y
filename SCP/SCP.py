import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import subprocess

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = discord.Client()
client = commands.Bot(command_prefix=">")

triggered = False

scpServer_Path = 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\SCP Secret Laboratory Dedicated Server'

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
async def on_message(ctx):
	global message
	if ctx.content == "hello":
		await ctx.channel.send("hi!")
	if discord.utils.get(ctx.guild.members) in ctx.mentions:
		message = await ctx.channel.send("Hey! Do you want to start the SCP Server? (React with 7 or more to start)")
		print(type(message))
		await message.add_reaction('🥵')


@bot.event
async def on_reaction_add(reaction, user):
	global triggered
	for re in reaction.message.reactions:
		if re.emoji != '🥵':
			print('Reaction rejected')
			await message.clear_reaction(re)
	if reaction.count >= 2 and triggered == False:
		await reaction.message.channel.send('Starting up!')
		triggered = True

def startServer():
	subprocess.call(scpServer_Path)
bot.run(TOKEN)