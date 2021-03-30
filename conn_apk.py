import discord
from config import settings
import requests
from dota import GetAccountInfo
import sqlite3
from database import BaseDiscord


message_winrate = [
    'винрейт',
    'мой винрейт',
    'win',
    'вин',
]

client = discord.Client()


@client.event
async def on_ready():
    print(f'Бот залогинился как {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    else:
        if message.id in BaseDiscord().get_users():
            if '!Мой ID :' in message.content:
                steam_id = (message.content).split(':')[1]
                print(steam_id)
                await message.channel.send(f'Твой ID {steam_id} зарегистрирован')

                await message.channel.send(f"""Привет {(message.author).split('#')[0]}, я вижу ты еще не зарегистрирован в моей базе, укажи свой Steam ID в формате -> !Мой ID: восьмизначный ID steam""")

        elif message.id:
            await message.channel.send(f"""Хей, я не нашел о тебе запись в базе данных, укажи свой стим id:  """)

        if (message.context).isdigit():
            if GetAccountInfo(message.context).get_profile() !=
            BaseDiscord.add_user(message.id, message.author, message.content, GetAccountInfo, '')


client.run(settings['token'])

