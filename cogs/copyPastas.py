import disnake
from disnake.ext import commands


class PingCommand(commands.Cog):
    """This will be for a ping command."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def ping(self, inter: disnake.ApplicationCommandInteraction):
        """Get the bot's current websocket latency."""
        await inter.response.send_message(f"Pong! {round(self.bot.latency * 1000)}ms")

    @commands.slash_command()
    async def walter(self, inter: disnake.ApplicationCommandInteraction):
        """Walter the funny"""
        await inter.response.send_message(f"Who are you ππ talking π£ to right β now? Who is it that you π think π­ you π see π? Do you ππ» know π΅π»ββοΈπ€ how much π₯ I π₯ make π a year π? I π mean π, even π if I π tell π£ you ππ», you ππ» wouldnβt believe π it. Do you π know π­ what happens π¦ππ if I π suddenly π± decide π― to stop π« going π into work πΌ? A business πΈ big ππ¦ enough π¦ it could be listed π¬ on π the NASDAQ πππ©πΏ goes π belly-up β. Gone π. It ceases β  to exist π without π« me. No π£, you π¦π clearly π donβt know π€ who youβre talking π£ to so let π me clue π you ππΌ in. I π am not in danger πͺ, Skylar π©π½. I π₯ am the danger πͺ. A guy π¦ opens π his π¦ front π door πͺ and gets π shot π«, and you ππΌ think π­ that of me? No π«. I π am the one 1οΈβ£ who knocks βπ.")

    @commands.slash_command()
    async def homelander(self, inter: disnake.ApplicationCommandInteraction):
        "Homelander speech"
        await inter.response.send_message(f"I don't make mistakes, I'm not like the rest of you, I'm stronger, I'm smarter, I'm better.\nI AM BETTER.\nI'm not some weak kneed fucking crybaby that goes around fucking apologizing all the time and why the fuck would you want me to be? All my life people have tried to control me, rich people, powerful people, tried to muzzle me, cancel me, keep me impotent and obedient, like I'm a fucking puppet. And you know what it worked, because I allowed it to work and guess what, if they can control me, they can control you. They already do you just realize it. I'm done. I am done apolgizing, I am done being persecuted for my strength. You people, should be thanking Christ that I am who I am, because you need me! You need me to save you, you do. I am the only one who possibly can. You're not the real heroes, I'M the real hero.\nI'm the real hero.")

    @commands.slash_command()
    async def joe(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, name=''):
        "Joe copypasta"
        nameWithoutID = str(inter.author)
        if name == '':
            await inter.response.send_message(f"<@{member.id}> hello new person! I am {nameWithoutID.split('#')[0]} one of the vets here in this server. Please feel free to ask me about anything related to gbf or even nsfw . I am pretty sure i can answer all of the raid questions and even if you want 6 digit recommendations if you know what i mean. Hahaha! We like to keep it casual here but we will ask you to go further if we see you having some potential to solo beel just like the rest of us but no pressure tho! We slacc and all. Hehe. Try looking at all the channels we even have other games channel but i dont really stay there since i am really dedicated to gbf just like how i am dedicated in life with my partner. (Yep sorry i am taken!) So try not have feelings when i show you how attentive i am to your question and needs. We can be good friends for sure and i hope i see you posting your own 6 digit recommendation hehehe. Let us keep our communications open such as vacation and rest days so we will know how active you are first. But if you are too shy with the other members you can pm me! (Not too often tho since i am taken sorry sorry!). I can coach you how to solo beel and do the other easier raids and how to progress your grid yep yep. Anyway have a great time here and dont forget to @ me every now and then as i have good reputation here. Everyone, let us welcome <@{member.id}>")
        else:
            await inter.response.send_message(f"<@{member.id}> hello new person! I am {name} one of the vets here in this server. Please feel free to ask me about anything related to gbf or even nsfw . I am pretty sure i can answer all of the raid questions and even if you want 6 digit recommendations if you know what i mean. Hahaha! We like to keep it casual here but we will ask you to go further if we see you having some potential to solo beel just like the rest of us but no pressure tho! We slacc and all. Hehe. Try looking at all the channels we even have other games channel but i dont really stay there since i am really dedicated to gbf just like how i am dedicated in life with my partner. (Yep sorry i am taken!) So try not have feelings when i show you how attentive i am to your question and needs. We can be good friends for sure and i hope i see you posting your own 6 digit recommendation hehehe. Let us keep our communications open such as vacation and rest days so we will know how active you are first. But if you are too shy with the other members you can pm me! (Not too often tho since i am taken sorry sorry!). I can coach you how to solo beel and do the other easier raids and how to progress your grid yep yep. Anyway have a great time here and dont forget to @ me every now and then as i have good reputation here. Everyone, let us welcome <@{member.id}>")

    @commands.slash_command()
    async def ff14(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message("Did you know that the critically acclaimed MMORPG Final Fantasy XIV has a free trial, and includes the entirety of A Realm Reborn AND the award-winning Heavensward expansion up to level 60 with no restrictions on playtime?")

def setup(bot: commands.Bot):
    bot.add_cog(PingCommand(bot))
