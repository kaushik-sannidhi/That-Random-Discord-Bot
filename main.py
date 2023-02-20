import os
import random
import discord
from keep_alive import keep_alive
from discord.ext import commands
import requests

client = commands.Bot(command_prefix = "trdb ")
client.remove_command('help')
TOKEN = "" ## input your bot token here
@client.event
async def on_ready():
    print('We have logged in ')
    print("------------------------")

@client.group(invoke_without_command = True)
async def help(ctx):
        em = discord.Embed(title="Help Menu", description="Use: trdb help to get the help menu")
        em.add_field(name="joke", value = "trdb help joke")
        em.add_field(name="fact", value = "trdb help fact")
        em.add_field(name="mag8ball", value = "trdb help mag8ball")
        em.add_field(name="bucketlist", value = "trdb help bucketlist")
        em.add_field(name="name", value = "trdb help name")
        em.add_field(name="riddle", value = "trdb help riddle")
        em.add_field(name="meter", value = "trdb help meter")
        em.add_field(name="chucknorris", value = "trdb help chucknorris")
        em.add_field(name="dadjoke", value = "trdb help dadjoke")
        em.add_field(name="hobbies", value = "trdb help hobbies")
        em.add_field(name="trivia", value = "trdb help trivia")
        await ctx.send(embed = em)

##help commands
@help.command()
async def joke(ctx):
    em = discord.Embed(title="Joke", description="Displays a joke", inline=False)
    em.add_field(name = "**SYNTAX**", value = "trdb joke")
    await ctx.send(embed = em)

@help.command()
async def fact(ctx):
    em = discord.Embed(title="Fact", description="Displays a fun fact", inline=False)
    em.add_field(name = "**SYNTAX**", value = "trdb fact")
    await ctx.send(embed=em)

@help.command()
async def name(ctx):
    em = discord.Embed(title="Name", description="Displays a name", inline=False)
    em.add_field(name = "**SYNTAX**", value = "trdb name")
    await ctx.send(embed=em)

@help.command()
async def mag8ball(ctx):
    em = discord.Embed(title="Mag8ball", description="A magic 8 ball", inline=False)
    em.add_field(name = "**SYNTAX**", value = "trdb mag8ball Should I ....")
    await ctx.send(embed=em)

@help.command()
async def riddle(ctx):
    em = discord.Embed(title="Riddle", description="Displays a riddle", inline=False)
    em.add_field(name = "**SYNTAX**", value = "trdb riddle")
    await ctx.send(embed=em)

@help.command()
async def meter(ctx):
    em = discord.Embed(title="Meter", description="Displays a percentage", inline=False)
    em.add_field(name = "**SYNTAX**", value = "trdb meter how smart am I")
    await ctx.send(embed=em)

@help.command()
async def bucketlist(ctx):
    em = discord.Embed(title="Bucketlist", description="Displays an item you should add to your bucketlist", inline=False)
    em.add_field(name = "**SYNTAX**", value = "trdb bucketlist")
    await ctx.send(embed=em)

@help.command()
async def chucknorris(ctx):
    em = discord.Embed(title="Chucknorris", description="Displays a chuck norris joke", inline=False)
    em.add_field(name = "**SYNTAX**", value = "trdb chucknorris")
    await ctx.send(embed=em)

@help.command()
async def dadjoke(ctx):
    em = discord.Embed(title="Dadjoke", description="Displays a dad joke", inline=False)
    em.add_field(name = "**SYNTAX**", value = "trdb dadjoke")
    await ctx.send(embed=em)

@help.command()
async def hobbies(ctx):
    em = discord.Embed(title="Hobbies", description="Displays a hobby", inline=False)
    em.add_field(name = "**SYNTAX**", value = "trdb hobbies")
    await ctx.send(embed=em)

@help.command()
async def trivia(ctx):
    em = discord.Embed(title="Trivia", description="Displays a trivia", inline=False)
    em.add_field(name = "**SYNTAX**", value = "trdb trivia")
    await ctx.send(embed=em)

##client commands


@client.command()
async def joke(ctx):
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        await ctx.send(f"Here's a joke for you:\n{data['setup']}\n{data['punchline']}")
    else:
        await ctx.send("Oops, something went wrong. Please try again later.")

@client.command()
async def riddle(ctx):
    api_url = 'https://api.api-ninjas.com/v1/riddles'
    response = requests.get(api_url, headers={'X-Api-Key': 'yrrwohytFsUz2YCFNqL2Hw==MxUiXJFgFM8j35Np'})
    if response.status_code == requests.codes.ok:
        await ctx.send("Q: "+response.json()[0]["question"]+"\n"+
                      "A: "+response.json()[0]["answer"])
    else:
        await ctx.send("Error:", response.status_code, response.text)
    

@client.command()
async def bucketlist(ctx):
    api_url = 'https://api.api-ninjas.com/v1/bucketlist'
    response = requests.get(api_url, headers={'X-Api-Key': 'yrrwohytFsUz2YCFNqL2Hw==MxUiXJFgFM8j35Np'})
    if response.status_code == requests.codes.ok:
        await ctx.send(response.json()["item"])
    else:
        await ctx.send("Error:", response.status_code, response.text)

@client.command()
async def name(ctx):
    api_url = 'https://api.api-ninjas.com/v1/babynames?gender=neutral'
    response = requests.get(api_url, headers={'X-Api-Key': 'yrrwohytFsUz2YCFNqL2Hw==MxUiXJFgFM8j35Np'})
    if response.status_code == requests.codes.ok:
        await ctx.send(response.json()[0])
    else:
        await ctx.send("Error:", response.status_code, response.text)

@client.command()
async def fact(ctx):
    api_url = 'https://api.api-ninjas.com/v1/facts?limit=1'
    response = requests.get(api_url, headers={'X-Api-Key': 'yrrwohytFsUz2YCFNqL2Hw==MxUiXJFgFM8j35Np'})
    if response.status_code == requests.codes.ok:
        await ctx.send(response.json()[0]["fact"])
    else:
        await ctx.send("Error:", response.status_code, response.text)
@client.command()
async def meme(ctx):
    api_url = 'https://meme-api.com/gimme/1'
    response = requests.get(api_url, headers={'X-Api-Key': 'yrrwohytFsUz2YCFNqL2Hw==MxUiXJFgFM8j35Np'})
    await ctx.send(response.json()["memes"][0]["url"])
@client.command()
async def meter(ctx):
    await ctx.send(str(random.randint(0,100))+"%")
    
@client.command()
async def mag8ball(ctx):
    answers = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "Outlook not so good.",
        "My sources say no.",
        "Very doubtful."
    ]
    await ctx.send(random.choice(answers))

@client.command()
async def chucknorris(ctx):
    api_url = 'https://api.api-ninjas.com/v1/chucknorris?'
    response = requests.get(api_url, headers={'X-Api-Key': 'yrrwohytFsUz2YCFNqL2Hw==MxUiXJFgFM8j35Np'})
    await ctx.send(response.json()["joke"])

@client.command()
async def dadjoke(ctx):
    api_url = 'https://api.api-ninjas.com/v1/dadjokes?limit=1'
    response = requests.get(api_url, headers={'X-Api-Key': 'yrrwohytFsUz2YCFNqL2Hw==MxUiXJFgFM8j35Np'})
    await ctx.send(response.json()[0]["joke"])

@client.command()
async def hobbies(ctx):
    api_url = 'https://api.api-ninjas.com/v1/hobbies?category=general'
    response = requests.get(api_url, headers={'X-Api-Key': 'yrrwohytFsUz2YCFNqL2Hw==MxUiXJFgFM8j35Np'})
    count = 0
    await ctx.send(response.json()["hobby"]+response.json()["link"])

@client.command()
async def trivia(ctx):
    api_url = 'https://api.api-ninjas.com/v1/trivia?category=general'
    response = requests.get(api_url, headers={'X-Api-Key': 'yrrwohytFsUz2YCFNqL2Hw==MxUiXJFgFM8j35Np'})
    await ctx.send(response.json()[0]["question"]+"\n"+response.json()[0]["answer"])
    
#client events to snipe edited and deleted messages

@client.event
async def on_message_delete(message):
    global snipe_message_content
    global snipe_message_author
    global snipe_message_id
    snipe_message_content = message.content
    snipe_message_author = message.author.id
    snipe_message_id = message.id
    if(snipe_message_author != 728263722598137989):
        await message.channel.send("sniped: " + "`" + snipe_message_content + "`" + "\nFrom: " +   f'<@!{snipe_message_author}>')
    
@client.event
async def on_message_edit(message_before, message_after):
    author = message_before.author.id
    channel = message_before.channel
    if(author != 728263722598137989):
      await channel.send(f"""Pre-edit: `{message_before.content}`\nPost-edit: `{message_after.content}`\nAuthor: <@!{message_before.author.id}>""")


#runs the bot 24/7 for free

keep_alive()
try:
  client.run(TOKEN,)
except:
  print("yeeted lmao, restarting")
  os.system("kill 1")
  os.system("python restarter.py")
