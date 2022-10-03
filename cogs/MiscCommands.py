import datetime
import os

import disnake, random
from disnake import ApplicationCommandInteraction
from disnake.ext import commands, tasks


class Misc(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(aliases=['8ball', '8b'])
    async def eightball(ctx, *, question):
        "RNG responses ftw"
        responses = [
            'Hell no.',
            'Prolly not.',
            'Idk bro.',
            'Prolly.',
            'Hell yeah my dude.',
            'It is certain.',
            'It is decidedly so.',
            'Without a Doubt.',
            'Yes - Definitaly.',
            'You may rely on it.',
            'As i see it, Yes.',
            'Most Likely.',
            'Outlook Good.',
            'Yes!',
            'No!',
            'Signs a point to Yes!',
            'Reply Hazy, Try again.',
            'IDK but u should subscribe to Exotix On Youtube and Follow Him On Insta mahad.ali.khan.',
            'Better not tell you know.',
            'Cannot predict now.',
            'Concentrate and ask again.',
            "Don't Count on it.",
            'My reply is No.',
            'My sources say No.',
            'Outlook not so good.',
            'Very Doubtful']
        await ctx.send(f':8ball: Question: {question}\n:8ball: Answer: {random.choice(responses)}')

    @commands.slash_command()
    async def clear(ctx, amount: int):
        "With great power, comes great responsibility"
        amount = min(amount, 100)
        if amount > 100:
            await ctx.send("Cannot delete more than 100 messages")
        else:
            await ctx.channel.purge(limit=amount)
            await ctx.send("snap")


def setup(bot: commands.Bot):
    bot.add_cog(Misc(bot))
