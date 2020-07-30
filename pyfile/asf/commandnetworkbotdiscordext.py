import discord, requests, asyncio, time, random
from discord.ext import commands

token = 'NjgwNzAwMzc4OTI4NjQ0MTE3.XsG6AQ.zkuCC2kX7vL6EFpnqIOFI9e13-g'
token2 = 'NjgwOTAxMTEyOTA3NTYzMDcx.XlGwzw.q8KueVIWhefOr4i-TdviLuQjs7Y'
build = 'v3.1.01 beta 1'
prefix = 'Cn!'

bot = commands.Bot(command_prefix=prefix, help_command=None)

bot.command(aliases=["connect","summon"]) #connectやsummonでも呼び出せる
async def join(ctx):
    """Botをボイスチャンネルに入室させます。"""
    voice_state = ctx.author.voice

    if (not voice_state) or (not voice_state.channel):
        await ctx.send("先にボイスチャンネルに入っている必要があります。")
        return

    channel = voice_state.channel

    await channel.connect()
    print("connected to:",channel.name)

@bot.command(aliases=["disconnect","bye","dc"])
async def leave(ctx):
    """Botをボイスチャンネルから切断します。"""
    voice_client = ctx.message.guild.voice_client

    if not voice_client:
        await ctx.send("Botはこのサーバーのボイスチャンネルに参加していません。")
        return

    await voice_client.disconnect()
    await ctx.send("ボイスチャンネルから切断しました。")

@bot.command()
async def music(ctx, arg):
    """指定された音声ファイルを流します。"""
    voice_client = ctx.message.guild.voice_client

    if not voice_client:
        await ctx.send("Botはこのサーバーのボイスチャンネルに参加していません。")
        return
    
    ffmpeg_audio_source = discord.FFmpegPCMAudio("music/{}.mp3".format(arg))
    voice_client.play(ffmpeg_audio_source)

@bot.command()
async def seen(ctx):
    """: ネタをランダムで選び表示します。"""
    a01 = random.randint(1, 5)
    if a47901 == 1:
        await ctx.send(file=discord.File('neta1.mp4'))
        await ctx.send(' by 敵を味方にするクラフト #4')
    elif a47901 == 2:
        await ctx.send(file=discord.File('neta2.mp4'))
        await ctx.send(' by 敵を味方にするクラフト #4')
    elif a47901 == 3:
        await ctx.send(file=discord.File('neta3.png'))
        await ctx.send(' by Google 翻訳')
    elif a47901 == 4:
        await ctx.send(file=discord.File('neta4.mp4'))
        await ctx.send(' by Twitter')
    elif a47901 == 5:
        await ctx.send(file=discord.File('neta5.png'))
        await ctx.send(' by taccharyi')

@bot.command()
async def random(ctx, arg, arg2):
    """: はじめと終わりの数字の間でランダムな数字を生成します。"""
    await ctx.send(randomint(int(arg),int(arg2)))

@bot.command(aliases=["pfm"])
async def performance(ctx):
    """: パフォーマンス(ホストコンピューターの状態)を表示します。"""
    mem = psutil.virtual_memory()
    cpu = psutil.cpu_percent(interval=1)
    a173013 = 'Memory: ' + str(mem.percent) + '%' + ' (' + str(mem.used / 1024 / 1024) + ' / ' + str(mem.total / 1024 / 1024) + 'MB' + ')'
    await ctx.send(a173013)
    a124897 = 'CPU: ' + str(cpu) + '%'
    await ctx.send(a124897)

@bot.command()
async def time(ctx):
    now = datetime.datetime.now()
    sendms = discord.Embed(title='Time', description=now.strftime("%Y/%m/%d %H:%M:%S.%f"), colour=0x7ED6DE)
    sendms.set_footer(text=now.strftime("Time: %Y/%m/%d %H:%M:%S.%f"))
    await ctx.send(embed=sendms)

bot.run(token)





#@bot.command()
#async def pick(ctx, arg, arg2):
#    """: 選択された語句からどちらかを選ぶ"""
#    a6790135 = [ arg, arg2 ]
#    await ctx.send(randomcho(a6790135))
