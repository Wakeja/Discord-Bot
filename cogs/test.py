from disnake.ext import commands
import sqlite3
import random
import disnake


class Event(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        db = sqlite3.connect("arknights.sqlite")
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS arknights(
            user_id INTEGER, wallet INTEGER, hh INTEGER, tenhh INTEGER, orundum INTEGER
        )''')
        print("Bot is online")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        author = message.author
        db = sqlite3.connect("arknights.sqlite")
        cursor = db.cursor()
        cursor.execute(f"SELECT user_id FROM arknights WHERE user_id = {author.id}")
        result = cursor.fetchone()
        if result is None:
            sql = ("INSERT INTO arknights(user_id, wallet, hh, tenhh, orundum) VALUES (?,?,?,?,?)")
            val = (author.id, 0, 0, 0, 0)
            cursor.execute(sql, val)

        db.commit()
        cursor.close()
        db.close()


def setup(bot: commands.Bot):
    bot.add_cog(Event(bot))