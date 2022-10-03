import disnake, random
from disnake.ext import commands, tasks


class Stone(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def stone(inter, member: disnake.Member):
        "Shame the user"
        await inter.response.send_message(f":rock: :rock: :rock: :rock: React to stone <@{member.id}> :rock: :rock: :rock: :rock:  ")
        msg = await inter.original_message()
        await msg.add_reaction('\U0001FAA8')

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        channel = reaction.message.channel
        original_string = reaction.message.content
        abc = original_string.find("<@")
        asd = original_string.find(">")
        ping_string = original_string[abc:asd]

        if(reaction.message.author.id == 1000178445013225512 and ':rock: :rock:' in reaction.message.content):
            if(reaction.emoji == '\U0001FAA8'):
                if(user.id == 1000178445013225512):
                    pass
                else:
                    file = disnake.File("stoned.gif", filename="image.gif")
                    await channel.send(f"{user.name} threw a rock at {ping_string}>", file=file)


def setup(bot: commands.Bot):
    bot.add_cog(Stone(bot))

