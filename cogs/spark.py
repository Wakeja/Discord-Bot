import sqlite3
from typing import Optional
import disnake,random
import asyncio
from disnake import ApplicationCommandInteraction
from disnake.ext import commands, tasks

class Pulls(commands.Cog):

    def __init__(self, bot:  commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def total(self, inter: disnake.ApplicationCommandInteraction, hh: Optional[int] = 0, tenhh: Optional[int] = 0, orundum: Optional[int] = 0):
        "Set your total number of pulls"
        total_pulls = int(((hh * 600) + (tenhh * 6000) + orundum) / 600)
        if(total_pulls < 1):
            await inter.send("https://tenor.com/view/wallet-gif-24561995")
        else:
            name_without_id = str(inter.author)
            spark_left = 300 - total_pulls
            embed = disnake.Embed(title="Arknights Pulls", color=0xeb4034)
            embed.set_author(name=name_without_id, icon_url=inter.author.avatar.url)
            embed.set_thumbnail(url="https://static.wikia.nocookie.net/mrfz/images/5/5c/Orundum.png/revision/latest?cb=20200202224532")
            if(spark_left > 0):
                embed.add_field(name=f"{hh} headhunts + {tenhh} 10x headhunt(s) + {orundum} orundum", value=f"You have a total of {total_pulls} pulls!"                                                                                        f"\nYou have {spark_left} til you can spark.")
            else:
                embed.add_field(name=f"{hh} headhunts + {tenhh} 10x headhunt(s) + {orundum} orundum", value=f"You have a total of {total_pulls} pulls!"
                                                                                                            f"\nYou are ready to spark!")

            await inter.send(embed=embed)

    @commands.slash_command()
    async def add_total(inter, hh: Optional[int] = None, tenhh: Optional[int] = None, orundum: Optional[int] = None):
        "Add to AK balance"
        db = sqlite3.connect("arknights.sqlite")
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM arknights WHERE user_id = {inter.author.id}") #<-hmmmmmmmmmmmmmmmmmmmmmmmm
        data = cursor.fetchone()
        try:
            col1 = data[1]
            col2 = data[2]
            col3 = data[3]
            col4 = data[4]
        except:
            await inter.send("There is an error")

        if(hh != None):
            cursor.execute("UPDATE arknights SET hh = ? WHERE user_id = ?", (col2 + hh, inter.author.id))

        if(tenhh != None):
            cursor.execute("UPDATE arknights SET tenhh = ? WHERE user_id = ?", (col3 + tenhh, inter.author.id))

        if (orundum != None):
            cursor.execute("UPDATE arknights SET orundum = ? WHERE user_id = ?", (col4 + orundum, inter.author.id))

        await inter.send(f"Updated! Check your new balance using /balance.")

        db.commit()
        cursor.close()
        db.close()

    @commands.slash_command()
    async def sub_total(inter, hh: Optional[int] = None, tenhh: Optional[int] = None, orundum: Optional[int] = None):
        "Subtract from AK balance"
        db = sqlite3.connect("arknights.sqlite")
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM arknights WHERE user_id = {inter.author.id}")  # <-hmmmmmmmmmmmmmmmmmmmmmmmm
        data = cursor.fetchone()
        try:
            col2 = data[2]
            col3 = data[3]
            col4 = data[4]
        except:
            await inter.send("There is an error")

        if (hh != None):
            cursor.execute("UPDATE arknights SET hh = ? WHERE user_id = ?", (col2 - hh, inter.author.id))
        if (tenhh != None):
            cursor.execute("UPDATE arknights SET tenhh = ? WHERE user_id = ?", (col3 - tenhh, inter.author.id))
        if (orundum != None):
            cursor.execute("UPDATE arknights SET orundum = ? WHERE user_id = ?", (col4 - orundum, inter.author.id))

        await inter.send(f"Updated! Check your new balance using /balance.")

        db.commit()
        cursor.close()
        db.close()

    @commands.slash_command()
    async def balance(ctx, member:disnake.Member = None):
        "AK Balance"
        if member is None:
            member = ctx.author

        db = sqlite3.connect("arknights.sqlite")
        cursor = db.cursor()

        cursor.execute(f"SELECT wallet, hh, tenhh, orundum FROM arknights WHERE user_id = {member.id}")
        bal = cursor.fetchone()

        cooler_tuple = list(bal)
        cooler_tuple[0] = int(((bal[1] * 600) + (bal[2] * 6000) + bal[3]) / 600)
        spark_left = 300 - cooler_tuple[0]

        embed = disnake.Embed(title="Arknights Balance", color=0xf54242)
        embed.set_author(name=member.name, icon_url=member.avatar.url)
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/mrfz/images/5/5c/Orundum.png/revision/latest?cb=20200202224532")
        if(spark_left <= 0):
            embed.add_field(name="Total Pulls", value=f"{cooler_tuple[0]}    (Can spark!)", inline=False)
        else:
            embed.add_field(name="Total Pulls", value=f"{cooler_tuple[0]}    ({spark_left} until spark)", inline=False)
        embed.add_field(name="HH", value=f"{bal[1]}")
        embed.add_field(name="10xHH", value=f"{bal[2]}")
        embed.add_field(name="Orundum", value=f"{bal[3]}")
        if(cooler_tuple[0] == 0):
            await ctx.send(content="https://tenor.com/view/wallet-gif-24561995")
            await ctx.send(embed=embed)
        else:
            await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(Pulls(bot))