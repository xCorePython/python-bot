#読み込み
import os
import discord
import time
import socket
import sys
import subprocess
import psutil
import random

from discord.ext import commands
#from .config import Config, ConfigDefaults

#変更場所
token = 'NjgwNzAwMzc4OTI4NjQ0MTE3.XlGwuA.gsmJ-n7-TItMUUuNZM8OAANGlZw'
bungeest2 = '>>> **BungeeCord** (Proxy Host) \n `Server is Offline`'
bungeest = '>>> **BungeeCord** (Proxy Host) \n `Server is Online`'
lobbyst2 = '>>> **Lobby Server** (BungeeCord Lobby) \n `Server is Offline`'
lobbyst = '>>> **Lobby Server** (BungeeCord Lobby) \n `Server is Online`'
skyblockst2 = '>>> **The Unusual SkyBlock v12.0.9 Server** (Spigot 1.10.2 Server) \n `Server is Offline`'
skyblockst = '>>> **The Unusual SkyBlock v12.0.9 Server** (Spigot 1.10.2 Server) \n `Server is Online`'
commandst2 = '>>> **Command Server** (Spigot 1.12.2 Server) \n `Server is Offline`'
commandst = '>>> **Command Server** (Spigot 1.12.2 Server) \n `Server is Online`'
survivalst2 = '>>> **Survival Server** (Spigot 1.15.2 Server) \n `Server is Offline`'
survivalst = '>>> **Survival Server** (Spigot 1.15.2 Server) \n `Server is Online`'
athleticst2 = '>>> **Athletic/Parkour Server** (Spigot 1.12.2 Server) \n `Server is Offline`'
athleticst = '>>> **Athletic/Parkour Server** (Spigot 1.12.2 Server) \n `Server is Online`'
pvpst2 = '>>> **PvP Server** (Spigot 1.8 Server) \n `Server is Offline`'
pvpst = '>>> **PvP Server** (Spigot 1.8 Server) \n `Server is Online`'
modskyblockst2 = '>>> **Skyblock in mod Server** (Forge 1.12.2 Server) \n `Server is Offline`'
modskyblockst = '>>> **Skyblock in mod Server** (Forge 1.12.2 Server) \n `Server is Online`'
twilightforestst2 = '>>> **Twilight Forest Server** (Forge 1.7.10 Server) \n `Server is Offline`'
twilightforestst = '>>> **Twilight Forest Server** (Forge 1.7.10 Server) \n `Server is Online`'
build = 'v2.1.60'
kousinnjyouhou = '```CommandsとStatusとInfoとMusic Botが実装されました```'
osirase = '```特になし```'
updatelog = 'f'

#help日本語化
class JapaneseHelpCommand(commands.DefaultHelpCommand):
    def __init__(self):
        super().__init__()
        self.commands_heading = ""
        self.no_category = "コマンド"
        self.command_attrs["help"] = "コマンド一覧と簡単な説明を表示"

    def get_ending_note(self):
        return (f"各コマンドの説明: s!help <コマンド名>\n"
                f"各カテゴリの説明: s!help <カテゴリ名>\n")

#関数置き場
shell = '>>> '
shell2 = '```'
a = ' is '
kaigyou = ' \n '
sikiri = ' | '
aa = 'Let\'s play Command Network!'
aaa = '**Status Bot Started**'
aaaa = 's!help'
aaaaa = 'Status Check Mode Now'
aaaaaa = ' このバージョンの更新内容: '
aaaaaaa = 'お知らせ :'
startstatus = shell + aaa + kaigyou + build + kaigyou + aaaaaa + kousinnjyouhou + kaigyou + aaaaa + kaigyou + aaaaaaa + osirase
customstatus = aaaa + sikiri + build
mode = 1
client = discord.Client()
bot = commands.Bot(command_prefix='s!', help_command=JapaneseHelpCommand())
mem = psutil.virtual_memory()
randomint = random.randint

#起動時の処理
@bot.event
async def on_ready():
    if updatelog == 'true':
        channel = bot.get_channel(683792670900224019)
        await channel.send(startstatus)
    await bot.change_presence(activity=discord.Game(name=customstatus))

@bot.command()
async def st(ctx, *, arg):
    """Command Networkのサーバーステータスを表示"""
    if arg == 'BungeeCord' or 'bungeecord':
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        bungeeport = sock.connect_ex(("60.112.154.214",25565))
        if bungeeport == 0:
            await ctx.send(bungeest)
        else:
            await ctx.send(bungeest2)
    if arg == 'Lobby' or 'lobby':
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        bungeeport = sock.connect_ex(("60.112.154.214",25566))
        if bungeeport == 0:
            await ctx.send(lobbyst)
        else:
            await ctx.send(lobbyst2)
    if arg == 'Skyblock''skyblock':
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        bungeeport = sock.connect_ex(("60.112.154.214",25567))
        if bungeeport == 0:
            await ctx.send(skyblockst)
        else:
            await ctx.send(skyblockst2)
    if arg == 'Command''command':
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        bungeeport = sock.connect_ex(("60.112.154.214",25568))
        if bungeeport == 0:
            await ctx.send(commandst)
        else:
            await ctx.send(commandst2)
    if arg == 'Survival''survival':
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        bungeeport = sock.connect_ex(("60.112.154.214",25569))
        if bungeeport == 0:
            await ctx.send(survivalst)
        else:
            await ctx.send(survivalst2)
    if arg == 'Athletic''athletic':
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        bungeeport = sock.connect_ex(("60.112.154.214",25570))
        if bungeeport == 0:
            await ctx.send(athleticst)
        else:
            await ctx.send(athleticst2)
    if arg == 'PvP''pvp':
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        bungeeport = sock.connect_ex(("60.112.154.214",25571))
        if bungeeport == 0:
            await ctx.send(pvpst)
        else:
            await ctx.send(pvpst2)
    if arg == 'Mod Skyblock''mod skyblock':
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        bungeeport = sock.connect_ex(("60.112.154.214",25572))
        if bungeeport == 0:
            await ctx.send(modskyblock)
        else:
            await ctx.send(modskyblock2)
    if arg == 'Twilight Forest''twilight forest':
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        bungeeport = sock.connect_ex(("60.112.154.214",25573))
        if bungeeport == 0:
            await ctx.send(twilightforestst)
        else:
            await ctx.send(twilightforestst2)
    else:
        await ctx.send('>>> **Info**\n `BungeeCord, Lobby, Skyblock, Command, Survival, Athletic, PvP, Mod Skyblock, Twilight Forest`\nのどれかを入力してください。\n (全部の文字が小文字でも反応します。誤字は反応しません。)')

@bot.command()
async def check(ctx, arg):
    """サーバーアドレスを入れるとオンラインか確認できます。"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    checkport = sock.connect_ex((arg,25565))
    if checkport == 0:
        await ctx.send('チェックしたサーバーは現在開いています。')
    else:
        await ctx.send('チェックしたサーバーは現在開いていません。')

@bot.command()
async def pick(ctx, arg, arg2, arg3):
    """タイマー"""
    if arg3 == 'none':
        a7194 = randomint(1, 3)
        if a7194 == 1:
            await ctx.send(arg)
        if a7194 == 2:
            await ctx.send(arg2)
        if a7194 == 3:
            await ctx.send(arg3)
    else:
        a7194 = randomint(1, 2)
        if a7194 == 1:
            await ctx.send(arg)
        if a7194 == 2:
            await ctx.send(arg2)

@bot.command()
async def random(ctx, arg, arg2):
    await ctx.send(randomint(int(arg),int(arg2)))

@bot.command()
async def say(ctx, *, arg):
    await ctx.send(arg)

@bot.command()
async def mode(ctx):
    """チャットモードに変更します。"""
    await ctx.send('チャットモードに変更しました。')
    mode = 1
    print('Quit Command: ecm')
    while mode == 1:
        sendmessage = input()
        await ctx.send(sendmessage)
        if sendmessage == 'ecm':
            print('Change Status Check Mode')
            continue
    await ctx.send('通常モードに変更しました。')


@bot.command()
async def info(ctx):
    """起動時のメッセージを再度表示します。"""
    await ctx.send(startstatus)

@bot.command()
async def status(ctx, *, arg):
    """ステータスを変更します。"""
    a1048 = arg + sikiri + customstatus
    await bot.change_presence(activity=discord.Game(name=a1048))

@bot.command()
async def shutdown(ctx):
    await ctx.send('Botをシャットダウンします。')
    sys.exit(code)

@bot.command()
async def commands(ctx, arg):
    log.info("This is Developing Event")

@bot.command()
async def invite(ctx):
    await ctx.send('Command Network: https://discord.gg/6yETYTK\nPlease read rules')

@bot.command()
async def performance(ctx, arg):
    if arg == 'Memory' or 'memory' or 'mem' or 'Mem':
        a173013 = str(mem.percent) + '%'
        await ctx.send(a173013)

@bot.command()
async def neta(ctx):
    a6193 = randomint(1, 3)
    if a6193 == 1:
        await ctx.send(file=discord.File('neta1.mp4'))
    if a6193 == 2:
        await ctx.send(file=discord.File('neta2.mp4'))
    if a6193 == 3:
        await ctx.send(file=discord.File('neta3.png'))

@bot.command()
async def calc(ctx, arg):
    await ctx.send(arg)

bot.run(token)
