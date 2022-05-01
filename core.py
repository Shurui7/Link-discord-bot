from discord.ext import commands
import discord

prefix = "!" #prefix for using commands
act = "watching" #acitvity 
act_desc = "links" 
token = "YOUR_TOKEN_HERE" #Your discord bot token here
bot = commands.Bot(command_prefix=prefix, activity=discord.Activity(type=discord.ActivityType[act].value, name=act_desc), status=discord.Status.online)


bot.remove_command("help")

@bot.command() # Twitch command
async def twitch(ctx, name):
    await ctx.send(f"https://twitch.tv/{name}")

@bot.command() # Youtube command
async def youtube(ctx, name):
    await ctx.send(f"https://youtube.com/c/{name}")

@bot.command() # Twitter command
async def twitter(ctx, name):
    await ctx.send(f"https://twitter.com/{name}")


@bot.command() # help command
async def help(ctx):
    embed=discord.Embed(title="Linky Help", description="This is the Linky Help Book", color=0x5866ef)
    embed.add_field(name="!twitch", value="sends u a link of twitch streamer", inline=False)
    embed.add_field(name="Usage:", value="!twitch (name)", inline=False)
    embed.add_field(name="!youtube", value="sends u a link of youtuber", inline=False)
    embed.add_field(name="Usage:", value="!youtube (name)", inline=False)
    embed.add_field(name="!twitter", value="!sends u a link of a twitter account", inline=False)
    embed.add_field(name="Usage:", value="!twitter (name)", inline=False)
    await ctx.send(embed=embed)

bot.run(token)
