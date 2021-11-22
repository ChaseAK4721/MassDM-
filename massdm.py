import discord

token = "OTEyMjI1NTU4MTc4NDU5Njc5.YZs2QQ.gisCeEuvDqb7iJmMkQCQGMaBCME
"
message = "This is What you get for being asscociated with OTR FUCKING RETARD"

client = discord.Client()

@client.event
async def on_connect():
    for friend in client.user.friends:
        try:
            await friend.send(message)
            print(f"Messaged {friend.name}")
        except:
            pass

    for channel in client.private_channels:
        try:
            await channel.send(message)
            print(f"Messaged {friend.name}")
        except:
            pass
            
client.run(token, bot=False)
