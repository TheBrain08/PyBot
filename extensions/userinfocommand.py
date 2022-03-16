from datetime import datetime

import discord
import pytz
from discord.ext import commands
from datetime import datetime


@commands.command(name='userinfo')
async def userinfo(ctx, member: discord.Member):
    de = pytz.timezone('Europe/Berlin')
    embed = discord.Embed(title=f'Userinfo für {member.display_name}',
                          description='', color=0x00eeff, timestamp=datetime.now().astimezone(tz=de))
    embed.add_field(name='Name', value=f'```{member.name}#{member.discriminator}```', inline=True)
    embed.add_field(name='Bot', value=f'```{("Ja" if member.bot else "Nein")}```', inline=True)
    embed.add_field(name='Nickname', value=f'```{(member.nick if member.nick else "Nicht gesetzt")}```', inline=True)

    embed.add_field(name='Server beigetreten', value=f'```{member.joined_at}```', inline=True)
    embed.add_field(name='Discord beigetreten', value=f'```{member.created_at}```', inline=True)
    embed.add_field(name='Rollen', value=f'```{len(member.roles) - 1}```', inline=True)

    embed.add_field(name='Höchste Rolle', value=f'```{member.top_role.name}```', inline=True)
    embed.add_field(name='Farbe', value=f'```{member.color}```', inline=True)
    embed.add_field(name='Booster', value=f'```{"ja" if member.premium_since else "Nein"}```', inline=True)

    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f'Angefordert von {ctx.author.name} • {ctx.author.id}', icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


def setup(bot):
    bot.add_command(userinfo)
