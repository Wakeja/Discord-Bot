import disnake
from disnake.ext import commands
import random


class MOCK(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def mock(self, ctx, phrase):
        new_sentence = ''
        for x in phrase:
            rando = random.randint(0,1)
            if(rando == 0):
                new_sentence += x.upper()
            else:
                new_sentence += x.lower()
        await ctx.send(new_sentence)


def setup(bot: commands.Bot):
    bot.add_cog(MOCK(bot))
