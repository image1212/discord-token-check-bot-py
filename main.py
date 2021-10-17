import discord.ext
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import requests

client=commands.Bot(command_prefix='!')

@client.command(aliases=["토큰"])
async def check(ctx, *, arg):
	headers = {'Content-Type': 'application/json', 'authorization': arg}
	url = 'https://discordapp.com/api/v6/users/@me/library'
	re = requests.get(url, headers=headers)
	if re.status_code == 200:
		await ctx.send("토큰이 살아있음")
	else:
		await ctx.send("토큰이 죽어있음")

client.run('')
