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

#変更場所
token = 'NjgwNzAwMzc4OTI4NjQ0MTE3.XlGwuA.gsmJ-n7-TItMUUuNZM8OAANGlZw'
bungeest2 = '>>> **Command Network** \nIP: akitama.xyz, 60.112.154.214 \n `Server is Offline`'
bungeest = '>>> **Command Network** \nIP: akitama.xyz, 60.112.154.214 \n `Server is Online`'
build = 'v2.1.62'
kousinnjyouhou = '```Music Bot導入不可能だったためBot作成者オンライン時のみしか使えません。```'
osirase = '```一部機能に修正・削除があります```'
updatelog = 'f'

#help日本語化
class JapaneseHelpCommand(commands.DefaultHelpCommand):
    def __init__(self):
        super().__init__()
        self.commands_heading = ""
        self.no_category = "コマンド"
        self.command_attrs["help"] = "\n: コマンド一覧と簡単な説明を表示"
        self.command_attrs["play"] = "\n: Bot作成者がオンラインのときに使用できます。"
    
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
cpu = psutil.cpu_percent(interval=1)
randomint = random.randint
randomcho = random.choice

#起動時の処理
@bot.event
async def on_ready():
    if updatelog == 'true':
        channel = bot.get_channel(683792670900224019)
        await channel.send(startstatus)
    await bot.change_presence(activity=discord.Game(name=customstatus))

@bot.command()
async def st(ctx):
    """\n: Command Networkのサーバーステータスを表示"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    bungeeport = sock.connect_ex(("60.112.154.214",25565))
    if bungeeport == 0:
        await ctx.send(bungeest)
    else:
        await ctx.send(bungeest2)

@bot.command()
async def status(ctx):
    """\n: Command Networkのサーバーステータスを表示"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    bungeeport = sock.connect_ex(("60.112.154.214",25565))
    if bungeeport == 0:
        await ctx.send(bungeest)
    else:
        await ctx.send(bungeest2)

@bot.command()
async def check(ctx, arg, arg2):
    """<サーバーアドレス> <ポート>\n: サーバーアドレスを入れるとオンラインか確認できます。"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    checkport = sock.connect_ex((arg,int(arg2)))
    if checkport == 0:
        await ctx.send('チェックしたサーバーは現在開いています。')
    else:
        await ctx.send('チェックしたサーバーは現在開いていません。')

@bot.command()
async def pick(ctx, arg, arg2):
    """<1つ目の語句> <2つ目の語句>\n: 選択された語句からどちらかを選ぶ"""
    a6790135 = [ arg, arg2 ]
    await ctx.send(randomcho(a6790135))

@bot.command()
async def random(ctx, arg, arg2):
    """<始めの数字> <終わりの数字>\n: はじめと終わりの数字の間でランダムな数字を生成します。"""
    await ctx.send(randomint(int(arg),int(arg2)))

@bot.command()
async def say(ctx, *, arg):
    """<言わせたい文字>\n: 言わせたい文字の部分をいいます。"""
    await ctx.send(arg)

@bot.command()
async def info(ctx):
    """\n: このBotの情報を表示します。"""
    await ctx.send(startstatus)

@bot.command()
async def information(ctx):
    """\n: このBotの情報を表示します。"""
    await ctx.send(startstatus)

@bot.command()
async def activity(ctx, *, arg):
    """<表示させたい部分>\n: アクティビティを表示させたい部分を追加して変更します。"""
    a1048 = arg + sikiri + customstatus
    await bot.change_presence(activity=discord.Game(name=a1048))

@bot.command()
async def invite(ctx):
    """\n: 招待コードを表示します。"""
    await ctx.send('Command Network: https://discord.gg/6yETYTK\nPlease read rules')

@bot.command()
async def pfm(ctx, arg):
    """\n: パフォーマンス(ホストコンピューターの状態)を表示します。"""
    a173013 = 'Memory: ' + str(mem.percent) + '%' + ' (' + str(mem.used / 1024 / 1024) + ' / ' + str(mem.total / 1024 / 1024) + 'MB' + ')'
    await ctx.send(a173013)
    a124897 = 'CPU: ' + str(cpu) + '%'
    await ctx.send(a124897)

@bot.command()
async def neta(ctx):
    """\n: ネタをランダムで選び表示します。"""
    a79424 = [ neta1.mp4, neta2.mp4, neta3.png ]
    await ctx.send(file=discord.File(randomcho(a79424)))

@bot.command()
async def music(ctx):
    """\n: Botの作成者が現時点で気に入っている曲のYouTubeリンクをチャンネルにアップロードします。"""
    await ctx.send('PSYQUI, Mo∀ - Rainbow Dream')
    await ctx.send('https://www.youtube.com/watch?v=BCM423NDOE0')
    await ctx.send('(Music Botに挿入済, s!play Rainbow Dream.mp3)')

bot.run(token)
