import discord
import os
import subprocess
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = discord.Client()

triggered = False

# TODO: Could change this reaction to a custom one
emoji = '🥵'
scpServer_Path = 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\SCP Secret Laboratory Dedicated Server\\LocalAdmin.exe'
os.chdir('C:\\Program Files (x86)\\Steam\\steamapps\\common\\SCP Secret Laboratory Dedicated Server\\')

# this is just seeing what servers the bot is in, may remove later.
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


@bot.event
async def on_message(ctx):
	global prompt
	if ctx.content == "hello":
		await ctx.channel.send("hi!")

	# TODO: Make this message also appear if the Class D role is mentioned
	#       maybe make the role editable :eyes:
	if discord.utils.get(ctx.guild.members) in ctx.mentions:
		prompt = await ctx.channel.send("Hey! Do you want to start the SCP Server? (React with 7 or more to start)")
		await prompt.add_reaction(emoji)

@bot.event
async def on_reaction_add(reaction, user):
	global prompt
	if prompt == reaction.message:
		for re in reaction.message.reactions:
			if re.emoji != emoji:
				print('Reaction rejected')
				await prompt.clear_reaction(re)
		if reaction.count >= 8 and triggered == False:
			await reaction.message.channel.send('Starting up!')
			startServer()

def startServer():
	global triggered
	triggered = True
	subprocess.call(scpServer_Path + ' 7777')
	triggered = False

bot.run(TOKEN)
