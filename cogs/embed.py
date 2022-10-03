import datetime

import disnake,random
from disnake.ext import commands, tasks


class EmbedStuff(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def test(ctx):  # Embed outline
        timestamp = datetime.datetime.now().strftime("%H:%M")
        embed = disnake.Embed(title="Our first embed", description="This is a description", color=0x34ebba)
        embed.set_thumbnail(url="https://i.pinimg.com/736x/d5/fb/52/d5fb524efb039ae77c06c09b8a7d85b5.jpg")
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        embed.set_footer(text=f"Time: {timestamp}")
        embed.add_field(name="Field", value="This is the value for field")

        await ctx.send(embed=embed)

    @commands.slash_command()
    async def test2(ctx):  # Send images
        file2 = disnake.File("dumborine.png", filename="image.jpg")
        await ctx.send(file=file2)

    @commands.slash_command()
    async def help(ctx):
        "Help lmao"
        embed = disnake.Embed(title="Help Commands", color=0x34ebba)
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/803949115738030131.webp?size=240&quality=lossless")
        embed.add_field(name="Commands", value="`clear` `eightball` `mock` `ping` `stone` `user`", inline=False)
        embed.add_field(name="Keywords the Bot will react to", value="`aaa` `hello there` `senate` `treason`", inline=False)
        embed.add_field(name="Copypastas", value="`ff14` `homelander` `joe` `walter`", inline=False)
        embed.add_field(name="AK Stuff", value="`add_total` `balance` `sub_total`")
        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(EmbedStuff(bot))