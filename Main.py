import asyncio
import sys
import traceback
from os import listdir
from os.path import isfile, join

import discord
from discord.ext import commands
import pytz
from datetime import datetime
from random import randint

solist = ["so", "soo", "sooo", "soooooooo!"]


class PythonBot(commands.Bot):

    def __init__(self, command_prefix, **options):
        super().__init__(command_prefix, **options)

    async def on_ready(self):
        print(f'Ich bin als {bot.user.name} eingeloggt • Meine ID ist {bot.user.id}')
        bot.loop.create_task(self.status_task())
        guild: discord.Guild = bot.get_guild(953381552539189319)

        channel: discord.TextChannel = guild.get_channel(953682295385120819)
        await channel.send('Bot ist gestartet')

    async def status_task(self):
        while True:
            await bot.change_presence(activity=discord.Game('Coded by WasteDevelopment'), status=discord.Status.online)
            await asyncio.sleep(5)
            await bot.change_presence(activity=discord.Game('Ich bin cool'), status=discord.Status.online)
            await asyncio.sleep(5)

    async def on_member_join(member):
        guild: discord.Guild = bot.get_guild(953381552539189319)
        channel = bot.get_channel(953690624865996841)
        de = pytz.timezone('Europe/Berlin')
        embed = discord.Embed(title=f'Willkommen **{member.display_name}**',
                              description=f'Wir wünschen dir viel spaß auf {guild.name}.', color=0x00eeff, timestamp=
                              datetime.now().astimezone(tz=de))
        embed.set_thumbnail(url=member.avatar_url)
        await channel.send(embed=embed)

    async def on_raw_reaction_add(self, payload):
        if payload.member.bot:
            return
        if payload.channel_id == 953656913151791165:
            if payload.message_id == 953656968734707812:
                if payload.emoji.name == '🦷':
                    guild: discord.Guild = bot.get_guild(953381552539189319)
                    role: discord.Role = guild.get_role(953652306337996820)
                    await payload.member.add_roles(role, reason="Zuweisung")

                    channel: discord.TextChannel = guild.get_channel(953656913151791165)
                    message = await channel.send('Du hast den Zahn gezogen.')
                    await message.add_reaction('🦷')


bot = PythonBot(intents=discord.Intents.all(), command_prefix='+', help_command=None)


@bot.command(name='sick')
async def sick(ctx):
    await ctx.send('https://discord.gg/tiktokzone')


@bot.command(name='so')
async def so(ctx):
    zufall = randint(0, len(solist) - 1)
    await ctx.send(solist[zufall])


@bot.command(name='kiwi')
async def kiwi(ctx):
    await ctx.send('https://iili.io/GHkiAX.gif')


if __name__ == '__main__':
    path = 'extensions'
    extensions = [file for file in listdir(path) if isfile(join(path, file))]
    for extension in extensions:
        try:
            bot.load_extension(f'{path}.{extension[:-3]}')
        except Exception as e:
            print(f'Faile to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

bot.run('Token')
