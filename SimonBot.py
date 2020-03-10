#Importing;
import discord
from discord.ext import commands
import time
import random

#Common Settings;
Prefix = '?'
bot = commands.Bot(command_prefix=Prefix,help_command=None)
token = 'Njg2NTgyODMwODM4MzE3MDg4.XmZUWQ.qcZuOX1DLPJZr6iwhhgUrAjdwHk'
main_status = "Divine || ?help"
guild = bot.get_guild(686333272359436359)
Bad_Words = ['nigga','nigger','niggeran','Nigga','NIGGA','NIggA','niGaa','fuck','f*','f***','f*ck','shit','shitty','fucking','f*cking','fucky','sh*t','shite','ass','asshole','assh*le','bitch','b*tch','dick','d*ck','cunt','c*nt','pussy','p*ssy','c*ck','cock','fucker']

Color = 16774656
Version = 'V.1.0.1'
Build = 'Alpha'
Divine_Owners = [359038724161667072,527610923419172864]
welcome_channel = bot.get_channel(686338066327273493)
Topics = ['trees','gaming','gamer-girls','science','school','anime','relationships','programming','art','discord','music','depression','homeless-people','nudes','sexual-comments','youtubers','twitter','simonbot','divine','aliens']

#Classes

async def log(Type,User,OnUser,Command,Message):
    Channel = Message.channel
    logs = bot.get_channel(686339474661441537)
    if OnUser != None:
        embed = discord.Embed(
        title=None,
        description=f'{Type},\nTarget: {OnUser}\n`{Prefix}{Command},`\n{Channel.mention}.',
        color=Color
        )
    else:
        embed = discord.Embed(
        title=None,
        description=f'{Type},\n`{Prefix}{Command},`\n{Channel.mention}.',
        color=Color
        )
    embed.set_footer(text=f'{User.id}, {User}')
    await logs.send(embed=embed)

#Commands

@bot.command()
async def help(ctx):
    await ctx.message.delete(delay=None)
    embed = discord.Embed(title=None,
    description= 'Hello, I\'m Simon!~\nI\'m a bot developed for Divine, so no you can\'t have me in your own server, sorry!~\n\nMy commands are;\n*?help, brings up this help message!~\n?role <Role>, to toggle your <Role>!~ For a list of the roles just do `?roles list`, or anything instead of a Role!~\n?warn <User> <Warning>, Moderation command: warn <User> for <Warning>!~\n?kick <User> <Reason>, Moderation command: kick <User> for <Reason>!~\n?ban <User> <Reason>, Moderation command: warn <User> for <Reason>!~\n?clear <Amount>, Moderater command: Clears the <Amount> of messages for you!~\n?rtopics, Moderater command: Randomizes the topic channels for you!~\n?status <Status>, Moderater command: changes the bots status to `Watching <Status>` or the main status if <Status> is `main`, for you!~*',
    color=Color)
    embed.set_footer(text=ctx.author)
    await ctx.author.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_messages=True)
@commands.cooldown(rate=3, per=5)
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.author.send(f'Cleared {amount} messages for you!~')
    await log(Type='Moderater Action',User=ctx.author,OnUser=None,Command=f'clear {amount}',Message=ctx.message)

@bot.command()
@commands.has_permissions(manage_messages=True)
@commands.cooldown(rate=1, per=5)
async def warn(ctx, member : discord.Member, *, reason):
    await ctx.message.delete(delay=None)
    await log(Type='Moderater Action',User=ctx.author,OnUser=member,Command=f'kick {member} {reason}',Message=ctx.message)
    await ctx.author.send(f'{member} was warned.')
    await member.send(f'**You have been warned.\nModerator Note:** {reason}\n *- {ctx.author}*')

@bot.command()
@commands.cooldown(rate=2, per=30)
@commands.has_permissions(manage_messages=True)
async def kick(ctx, member : discord.Member, *, reason):
    await ctx.message.delete(delay=None)
    await member.kick(reason=reason)
    await log(Type='Moderater Action',User=ctx.author,OnUser=member,Command=f'kick {member} {reason}',Message=ctx.message)
    await ctx.author.send(f'{member} was kicked.')
    await member.send(f'**You have been kicked.\nModerator Note:** {reason}\n *- {ctx.author}*')

@bot.command()
@commands.cooldown(rate=2, per=60)
@commands.has_permissions(manage_messages=True)
async def ban(ctx, member : discord.Member, *, reason):
    await ctx.message.delete(delay=None)
    await member.ban(reason=reason)
    await log(Type='Moderater Action',User=ctx.author,OnUser=member,Command=f'kick {member} {reason}',Message=ctx.message)
    await ctx.author.send(f'{member} was banned.')
    await member.author.send(f'**You have been banned.\nModerator Note:** {reason}\n *- {ctx.author}*')

@bot.command()
@commands.cooldown(rate=1, per=60)
@commands.has_permissions(manage_messages=True)
async def announce(ctx, ping : bool,*,announcement):
    channel = bot.get_channel(686338128163766344)
    if ping == True:
        await channel.send('@everyone',delete_after=True)
    embed = discord.Embed(title=None,description= announcement,color=Color)
    await channel.send(embed=embed)
    await log(Type='Announcment sent',User=ctx.author,OnUser=ctx.author,Command=f'kick {member} {reason}',Message=ctx.message)

@bot.command()
@commands.cooldown(rate=1, per=5)
async def role(ctx,role : str):
    guild = ctx.guild
    if role == None:
        await ctx.send('Have a list of roles you can pick!~\n- weeb\n- single\n- taken\n- female\n- male\n- bi\n- e-girl\n- memer')
    elif role == 'weeb':
        role = guild.get_role(686344964871028801)
        if role in ctx.author.roles:
            await ctx.author.remove_roles(role)
        else:
            await ctx.author.add_roles(role)
        await ctx.send('Toggled the role, enjoy!~')
    elif role == 'single':
        role = guild.get_role(686345029819695126)
        if role in ctx.author.roles:
            await ctx.author.remove_roles(role)
        else:
            await ctx.author.add_roles(role)
        await ctx.send('Toggled the role, enjoy!~')
    elif role == 'female':
        role = guild.get_role(686345102230290479)
        if role in ctx.author.roles:
            await ctx.author.remove_roles(role)
        else:
            await ctx.author.add_roles(role)
        await ctx.send('Toggled the role, enjoy!~')
    elif role == 'male':
        role = guild.get_role(686345158383501337)
        if role in ctx.author.roles:
            await ctx.author.remove_roles(role)
        else:
            await ctx.author.add_roles(role)
        await ctx.send('Toggled the role, enjoy!~')
    elif role == 'bi':
        role = guild.get_role(686345205644918835)
        if role in ctx.author.roles:
            await ctx.author.remove_roles(role)
        else:
            await ctx.author.add_roles(role)
        await ctx.send('Toggled the role, enjoy!~')
    elif role == 'e-girl':
        role = guild.get_role(686345253938003993)
        if role in ctx.author.roles:
            await ctx.author.remove_roles(role)
        else:
            await ctx.author.add_roles(role)
        await ctx.send('Toggled the role, enjoy!~')
    elif role == 'memer':
        role = guild.get_role(686345308367487116)
        if role in ctx.author.roles:
            await ctx.author.remove_roles(role)
        else:
            await ctx.author.add_roles(role)
        await ctx.send('Toggled the role, enjoy!~')
    elif role == 'taken':
        role = guild.get_role(686684847732817952)
        if role in ctx.author.roles:
            await ctx.author.remove_roles(role)
        else:
            await ctx.author.add_roles(role)
        await ctx.send('Toggled the role, enjoy!~')
    else:
        await ctx.send('Have a list of roles you can pick!~\n- weeb\n- single\n- taken\n- female\n- male\n- bi\n- e-girl\n- memer')

@bot.command()
@commands.cooldown(rate=1, per=60)
@commands.has_permissions(manage_messages=True)
async def rtopics(ctx):
    await ctx.message.delete(delay=None)
    Channel1 = bot.get_channel(686338765920272543)
    Channel2 = bot.get_channel(686338885206147292)
    Channel3 = bot.get_channel(686338947638362289)
    await Channel1.edit(name=random.choice(Topics))
    await Channel2.edit(name=random.choice(Topics))
    await Channel3.edit(name=random.choice(Topics))
    await Channel1.purge(limit=None)
    await Channel2.purge(limit=None)
    await Channel3.purge(limit=None)
    await ctx.author.send(f'Changed topics to {Channel1.name}, {Channel2.name} and {Channel3.name}!~')
    await Channel1.send(f'Topic randomized to {Channel1.name} by {ctx.author}!~')
    await Channel2.send(f'Topic randomized to {Channel2.name} by {ctx.author}!~')
    await Channel3.send(f'Topic randomized to {Channel3.name} by {ctx.author}!~')
    await log(Type='Changed topics',User=ctx.author,OnUser=None,Command=f'rtopics',Message=ctx.message)

@bot.command()
async def status(ctx, *, status):
    await ctx.message.delete(delay=None)
    if ctx.author.id in Divine_Owners:
        if str(status) == 'main':
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=main_status))
            await ctx.author.send(f'Changed status to: `Watching {main_status}`!~')
        else:
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=str(status)))
            await ctx.author.send(f'Changed status to: `Watching {status}`!~')

#Events

@bot.event
async def on_ready():
    print('SimonBot\nSuccesfully loaded.')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=main_status))

@bot.event
async def on_raw_reaction_add(payload):
    if payload.channel_id == 686338066327273493:
        guild = bot.get_guild(686333272359436359)
        role = guild.get_role(686344645231640576)
        user = guild.get_member(payload.user_id)
        await user.add_roles(role)

@bot.event
async def on_command_error(ctx, error):
    await ctx.message.delete(delay=None)
    await ctx.author.send(error)

@bot.event
async def on_member_join(member):
    list = [f'{member}, aye.',f'Oh wow, {member} appeared.',f'{member} just flew in, wooshhh.',f'Teehee, {member} I was hoping you\'d join.',f'{member} came with some pizza, let him in.',f'{member} is here to love and hate.',f'Roses are red, violets are blue, {member} joined the server with you.',f'{member}, where\'s the pizza?',f'{member} :eyes:',f'{member} enjoys being {member}.',f'{member}, the council will decide your fate.']
    channel = bot.get_channel(686338279678803988)
    await channel.send(random.choice(list))

#Running
bot.run(token)
