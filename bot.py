# Work with Python 3.6
import discord

TOKEN = ''

client = discord.Client()

@client.event
async def on_message(message):
	userMassage = ''
	if message.author == client.user:
		return

	username = str(message.author)
	
	userMassage += username[0:int(len(username)-5)] + ' said: ' + message.content
	await message.channel.send(userMassage, tts = True, delete_after = 5.0);

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)