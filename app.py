import discord
from discord.ext import commands
import google.generativeai as genai

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
conversation_history = []
genai.configure(api_key="AIzaSyAMEr1SgGlWcKPZA7VwmUy48XXwyC_74jM")
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=conversation_history)

bot = commands.Bot(command_prefix='!', description="Oweda Strikaaa daaaa", intents=intents)

@bot.event
async def on_ready():
    print("Bot pret !")


@bot.command()
async def t(ctx):
    await ctx.send("bot en fonctionnement...")


@bot.event
async def on_message(message):
    msg = message.content[1:].strip()
    conversation_history.append({"role": "user", "content": msg})
    if message.author == bot.user:
        return
    if message.content.startswith("go"):
        go = message
        print(go)
    if message.content.startswith("?"):
        response = chat.send_message(msg, stream=False)
        for chunk in response:
            await message.channel.send(f"{chunk.text}")
            conversation_history.append({"role": "bot", "content": chunk.text})

    await bot.process_commands(message)


bot.run('MTI4Njk5NzgwNzAwOTM2NjA5MA.GkzJSr.JiaSAkSMtW6juF_Qu8Oq-4JLKm4sMa82LTAO6k')