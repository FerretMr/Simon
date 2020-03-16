#Importing;
import discord
from discord.ext import commands
import time
import random
import threading
from threading import Thread
#
#Common Settings;
Prefix = '?'
bot = commands.Bot(command_prefix=Prefix,help_command=None)
token = 'Njg5MTAxODM4MTIwNjQ4NzI0.Xm9-Jg.aPUG0ZLkR_BO-rYXM7SSdHBZmF8'
main_status = "Divine || ?help"
guild = bot.get_guild(686333272359436359)
Bad_Words = ['nigga','nigger','niggeran','Nigga','NIGGA','NIggA','niGaa','fuck','f*','f***','f*ck','shit','shitty','fucking','f*cking','fucky','sh*t','shite','ass','asshole','assh*le','bitch','b*tch','dick','d*ck','cunt','c*nt','pussy','p*ssy','c*ck','cock','fucker']

mute_list = []
Color = 15898955
Version = 'V.1.0.1'
Build = 'Alpha'
Divine_Owners = [359038724161667072,527610923419172864]
welcome_channel = bot.get_channel(686338066327273493)
Topics = ['women-rights','icons','logos','discord-bots','bussiness','trees','gaming','gamer-girls','science','school','anime','relationships','programming','art','discord','music','depression','homeless-people','nudes','sexual-comments','youtubers','twitter','simonbot','divine','aliens']

#Classes

locked_channels = []

@bot.command()
@commands.cooldown(rate=1, per=5)
@commands.has_role(686344052471234560)
async def lock(ctx):
    locked_channels.append(ctx.channel)

@bot.command()
@commands.cooldown(rate=1, per=5)
@commands.has_role(686344052471234560)
async def unlock(ctx):
    locked_channels.remove(ctx.channel)

def mmute(minutes,member):
    mute_list.append(member)
    time.sleep(minutes * 60)
    mute_list.remove(member)

def giveaway():
    channel = bot.get_channel(686338128163766344)
    channel.send()

import threading
def mute_user(minutes,member):
    download_thread = threading.Thread(target=mmute, args=(minutes,member))
    download_thread.start()

async def log(Type,User,OnUser,Command,Message):
    Channel = Message.channel
    logs = bot.get_channel(686339474661441537)
    if OnUser != None:
        embed = discord.Embed(title=Type,description=f'**Channel:** {Message.channel.mention}, `{Message.channel.id}`.\n**Victim:** {OnUser.mention}, `{OnUser.id}`.\n`{Prefix}{Command} || {Message.id}.`',color=Color)
        embed.set_footer(text=f'Divine || {Message.channel.mention}')
        embed.set_author(name=str(User), icon_url=User.avatar_url)
    else:
        embed = discord.Embed(title=Type,description=f'**Channel:** {Message.channel.mention}, `{Message.channel.id}`.\n`{Prefix}{Command} || {Message.id}.`',color=Color)
        embed.set_footer(text=f'Divine || {Message.channel.mention}')
        embed.set_author(name=str(User), icon_url=User.avatar_url)
    embed.set_footer(text=f'{User.id}, {User}')
    await logs.send(embed=embed)

#Commands


@bot.command()
async def help(ctx):
    await ctx.message.delete(delay=None)
    embed = discord.Embed(title=None,
    description= 'Hello, I\'m Simon!~\nI\'m a bot developed for Divine, so no you can\'t have me in your own server, sorry!~\n\nMy commands are;\n*?help, brings up this help message!~\n?role <Role>, to toggle your <Role>!~ For a list of the roles just do `?roles list`, or anything instead of a Role!~\n?warn <User> <Warning>, Moderation command: warn <User> for <Warning>!~\n?kick <User> <Reason>, Moderation command: kick <User> for <Reason>!~\n?ban <User> <Reason>, Moderation command: warn <User> for <Reason>!~\n?clear <Amount>, Moderater command: Clears the <Amount> of messages for you!~\n?rtopics, Moderater command: Randomizes the topic channels for you!~\n?status <Status>, Moderater command: changes the bots status to `Watching <Status>` or the main status if <Status> is `main`, for you!~\n?reward <Member> <Badge>, Moderater command: gives <Member> the <Badge> for you!~*\n?mute <Member> <Minutes> <Reason>, Moderater command: Mutes the <Member> for the amount of <Minutes>!~*\n?unmute <Member> <Reason>, Moderater command: Unmutes the <Member>!~*',
    color=Color)
    embed.set_footer(text=ctx.author)
    await ctx.author.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_messages=True)
@commands.cooldown(rate=3, per=5)
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.author.send(f'Cleared {amount} messages for you!~')
    await log(Type='Bulk Message Delete',User=ctx.author,OnUser=None,Command=f'clear {amount}',Message=ctx.message)

@bot.command()
@commands.has_permissions(manage_messages=True)
@commands.cooldown(rate=1, per=5)
async def mute(ctx, member : discord.Member, minutes : int,*,reason):
    await ctx.message.delete(delay=None)
    mute_user(member=member,minutes=minutes)
    await log(Type='Member muted',User=ctx.author,OnUser=None,Command=f'mute {member} {minutes} {reason}',Message=ctx.message)

@bot.command()
@commands.has_permissions(manage_messages=True)
@commands.cooldown(rate=1, per=5)
async def unmute(ctx, member : discord.Member,*,reason):
    await ctx.message.delete(delay=None)
    mute_list.remove(member)
    await log(Type='Member unmuted',User=ctx.author,OnUser=None,Command=f'mute {member} {reason}',Message=ctx.message)

@bot.command()
@commands.has_permissions(manage_messages=True)
@commands.cooldown(rate=1, per=5)
async def warn(ctx, member : discord.Member, *, warning):
    await ctx.message.delete(delay=None)
    await log(Type='Member warned',User=ctx.author,OnUser=member,Command=f'warn {member} {warning}',Message=ctx.message)
    embed = discord.Embed(title='Warning',description=warning,color=Color)
    embed.set_footer(text=f'Divine || {member.id}')
    embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)
    await member.send(embed=embed)
    await ctx.author.send(embed=embed)

@bot.command()
@commands.cooldown(rate=2, per=30)
@commands.has_permissions(manage_messages=True)
async def kick(ctx, member : discord.Member, *, reason):
    await ctx.message.delete(delay=None)
    await member.kick(reason=reason)
    await log(Type='Member kicked',User=ctx.author,OnUser=member,Command=f'kick {member} {reason}',Message=ctx.message)
    embed = discord.Embed(title='Kick',description=warning,color=Color)
    embed.set_footer(text=f'Divine || {member.id}')
    embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)
    await member.send(embed=embed)
    await ctx.author.send(embed=embed)

@bot.command()
@commands.cooldown(rate=2, per=60)
@commands.has_permissions(manage_messages=True)
async def ban(ctx, member : discord.Member, *, reason):
    await ctx.message.delete(delay=None)
    await member.ban(reason=reason)
    await log(Type='Member banned',User=ctx.author,OnUser=member,Command=f'ban {member} {reason}',Message=ctx.message)
    embed = discord.Embed(title='Ban',description=warning,color=Color)
    embed.set_footer(text=f'Divine || {member.id}')
    embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)
    await member.send(embed=embed)
    await ctx.author.send(embed=embed)

@bot.command()
@commands.cooldown(rate=1, per=60)
@commands.has_permissions(manage_messages=True)
async def announce(ctx, ping : bool,*,announcement):
    await ctx.message.delete(delay=None)
    channel = bot.get_channel(686338128163766344)
    if ping == True:
        await channel.send('@everyone',delete_after=True)
    embed = discord.Embed(title=None,description= announcement,color=Color)
    embed.set_footer(text=f'Divine || {ctx.author.id}')
    embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)
    await channel.send(embed=embed)
    await log(Type='Announcment sent',User=ctx.author,OnUser=None,Command=f'announce {ping} {announcement}',Message=ctx.message)

@bot.command()
@commands.cooldown(rate=1, per=5)
async def role(ctx,role : str):
    guild = ctx.guild
    if role == None:
        await ctx.send('Have a list of roles you can pick!~\n- Gender\n    male\n    female\n    trans\n- Sexualtiy\n    straight\n    gay\n    bi\n- Extra\n     gamer\n    memer\n    e-girl\n    weeb')
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
    elif role == 'trans':
        role = guild.get_role(687773911588274178)
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
    elif role == 'gamer':
        role = guild.get_role(687764393009610752)
        if role in ctx.author.roles:
            await ctx.author.remove_roles(role)
        else:
            await ctx.author.add_roles(role)
        await ctx.send('Toggled the role, enjoy!~')
    elif role == 'straight':
        role = guild.get_role(687764522643095662)
        if role in ctx.author.roles:
            await ctx.author.remove_roles(role)
        else:
            await ctx.author.add_roles(role)
            await ctx.send('Toggled the role, enjoy!~')
    elif role == 'gay':
        role = guild.get_role(687764552951005207)
        if role in ctx.author.roles:
            await ctx.author.remove_roles(role)
        else:
            await ctx.author.add_roles(role)
            await ctx.send('Toggled the role, enjoy!~')
    else:
        await ctx.send('Have a list of roles you can pick!~\n- Gender\n    male\n    female\n    trans\n- Sexualtiy\n    straight\n    gay\n    bi\n- Extra\n     gamer\n    memer\n    e-girl\n    weeb')

@bot.command()
@commands.cooldown(rate=1, per=5)
@commands.has_permissions(manage_messages=True)
async def reward(ctx,member : discord.Member,*,badge):
    guild = ctx.guild
    if badge == 'list':
        await ctx.send('There\'s are our badges!~\n-Competition Winner\n-Early Supporter\n-Chatter\n-Founder\n-Partner')
    elif badge == 'Competition Winner':
        role = guild.get_role(687764619745427615)
        if role in member.roles:
            await member.remove_roles(role)
        else:
            await member.add_roles(role)
        await ctx.send('Toggled the role, enjoy!~')
    elif badge == 'Early Supporter':
        role = guild.get_role(687764390598279174)
        if role in member.roles:
            await member.remove_roles(role)
        else:
            await member.add_roles(role)
        await ctx.send('Toggled the role, enjoy!~')
    elif badge == 'Chatter':
        role = guild.get_role(687765632300875787)
        if role in member.roles:
            await member.remove_roles(role)
        else:
            await member.add_roles(role)
        await ctx.send('Toggled the role, enjoy!~')
    elif badge == 'Founder':
        role = guild.get_role(687775096844451846)
        if role in member.roles:
            await member.remove_roles(role)
        else:
            await member.add_roles(role)
        await ctx.send('Toggled the role, enjoy!~')
    elif badge == 'Partner':
        role = guild.get_role(687775094436528195)
        if role in member.roles:
            await member.remove_roles(role)
        else:
            await member.add_roles(role)
        await ctx.send('Toggled the role, enjoy!~')
    else:
        await ctx.send('There\'s are our badges!~\n-Competition Winner\n-Early Supporter\n-Chatter\n-Founder\n-Partner')

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
        role = guild.get_role(687765696913997864)
        await user.add_roles(role)
        role = guild.get_role(687765773137084500)
        await user.add_roles(role)

@bot.event
async def on_command_error(ctx, error):
    await ctx.author.send(error)

@bot.event
async def on_member_join(member):
    list = [f'Who\'s in the server? {member} is!~',f'Welcome {member}, where\'s your papperwork?',f'Welcome to Divine, {member}. Enjoy your stay!~',f'{member}, aye.',f'Oh wow, {member} appeared.',f'{member} just flew in, wooshhh.',f'Teehee, {member} I was hoping you\'d join.',f'{member} came with some pizza, let him in.',f'{member} is here to love and hate.',f'Roses are red, violets are blue, {member} joined the server with you.',f'{member}, where\'s the pizza?',f'{member} :eyes:',f'{member} enjoys being {member}.',f'{member}, the council will decide your fate.']
    channel = bot.get_channel(686338279678803988)
    await channel.send(random.choice(list))

@bot.event
async def on_message(message):
    staff_role = message.guild.get_role(686344052471234560)
    if channel in locked_channels:
        if not staff_role in message.author.roles:
            await message.delete(delay=None)
    if message.author in mute_list:
        await message.delete(delay=None)

    await bot.process_commands(message)

#Running
bot.run(token)
