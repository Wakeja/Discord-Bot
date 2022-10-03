import disnake
from disnake.ext import commands

class Key(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg):

        #Prequel Quotes
        if 'hello there' in msg.content.lower():
            channel = msg.channel
            await channel.send('GENERAL KENOBI! YOU ARE A BOLD ONE.')

        if 'senate' in msg.content.lower():
            file = disnake.File("palpatine1.gif", filename="image.gif")
            channel = msg.channel
            await channel.send(file=file)

        if 'democracy' in msg.content.lower():
            file = disnake.File("palpatine2.gif", filename="image.gif")
            channel = msg.channel
            await channel.send(file=file)

        if 'aaa' in msg.content.lower():
            file = disnake.File("palpatine3.gif", filename="image.gif")
            channel = msg.channel
            await channel.send(file=file)

        if 'treason' in msg.content.lower():
            file = disnake.File("palpatine4.gif", filename="image.gif")
            channel = msg.channel
            await channel.send(file=file)


def setup(bot: commands.Bot):
    bot.add_cog(Key(bot))