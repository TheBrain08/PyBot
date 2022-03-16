import discord
from discord.ext import commands


@commands.command(name='help')
async def help(ctx):
    embed = discord.Embed(title="Command Liste", url="https://iili.io/EZWDKl.md.jpg",
                          description="In dieser Liste findest du alle Befehle vor diesen Bot", color=0x00ccff)
    embed.add_field(name="+help", value="Zeigt dir diese liste an", inline=False)
    embed.add_field(name="+userinfo", value="Zeigt dir die Informationen für einen bestimmten User an", inline=False)
    embed.set_thumbnail(url='https://iili.io/EZWDKl.md.jpg')
    await ctx.send(embed=embed)


def setup(bot):
    bot.add_command(help)
