import discord
from discord.ext import commands

token = 'NjgwNzAwMzc4OTI4NjQ0MTE3.XsG6AQ.zkuCC2kX7vL6EFpnqIOFI9e13-g'
token2 = 'NjgwOTAxMTEyOTA3NTYzMDcx.XlGwzw.q8KueVIWhefOr4i-TdviLuQjs7Y'
build = 'v3.1.01 beta 1'
prefix = 'Cnt!'

#help日本語化
class JapaneseHelpCommand(commands.DefaultHelpCommand):
    def __init__(self):
        super().__init__()
        self.commands_heading = ""
        self.no_category = "コマンド"
        self.command_attrs["help"] = ": コマンド一覧と簡単な説明を表示"
        self.command_attrs["play"] = ": Bot作成者がオンラインのときに使用できます。"
    
    def get_ending_note(self):
        return (f"各コマンドの説明: s!cmd <コマンド名>\n")

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

@bot.command(aliases=["disconnect","bye"])
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

<<<<<<< HEAD
    ffmpeg_audio_source = discord.FFmpegPCMAudio("music/{}.mp3".format(arg))
    voice_client.play(ffmpeg_audio_source)

=======






    ffmpeg_audio_source = discordFFmpegPCMAudio("music/{}.mp3".format(arg))
    voice_client.play(ffmpeg_audio_source)




bot.run(token)




@bot.command()
async def status(ctx):
    """: Command Networkのサーバーステータスを表示"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    bungeeport = sock.connect_ex(("60.112.154.214",25565))
    if bungeeport == 0:
        await ctx.send(bungeest)
    else:
        await ctx.send(bungeest2)

@bot.command()
async def check(ctx, arg, arg2):
    """: サーバーアドレスを入れるとオンラインか確認できます。"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    checkport = sock.connect_ex((arg,int(arg2)))
    if checkport == 0:
        await ctx.send('チェックしたサーバーは現在開いています。')
    else:
        await ctx.send('チェックしたサーバーは現在開いていません。')

@bot.command()
async def pick(ctx, arg, arg2):
    """: 選択された語句からどちらかを選ぶ"""
    a6790135 = [ arg, arg2 ]
    await ctx.send(randomcho(a6790135))

@bot.command()
async def random(ctx, arg, arg2):
    """: はじめと終わりの数字の間でランダムな数字を生成します。"""
    await ctx.send(randomint(int(arg),int(arg2)))

@bot.command()
async def say(ctx, *, arg):
    """: 言わせたい文字の部分をいいます。"""
    await ctx.send(arg)

@bot.command()
async def info(ctx):
    """: s!informationと同様"""
    await ctx.send(startstatus)

@bot.command()
async def information(ctx):
    """: このBotの情報を表示します。"""
    await ctx.send(startstatus)

@bot.command()
async def activity(ctx, *, arg):
    """: アクティビティを表示させたい部分を追加して変更します。"""
    a1048 = arg + sikiri + customstatus
    await bot.change_presence(activity=discord.Game(name=a1048))

@bot.command()
async def invite(ctx):
    """: 招待コードを表示します。"""
    await ctx.send('Command Network: https://discord.gg/6yETYTK\nPlease read rules')

@bot.command()
async def pfm(ctx):
    """: s!performanceと同様"""
    mem = psutil.virtual_memory()
    cpu = psutil.cpu_percent(interval=1)
    a173013 = 'Memory: ' + str(mem.percent) + '%' + ' (' + str(mem.used / 1024 / 1024) + ' / ' + str(mem.total / 1024 / 1024) + 'MB' + ')'
    await ctx.send(a173013)
    a124897 = 'CPU: ' + str(cpu) + '%'
    await ctx.send(a124897)

@bot.command()
async def performance(ctx):
    """: パフォーマンス(ホストコンピューターの状態)を表示します。"""
    mem = psutil.virtual_memory()
    cpu = psutil.cpu_percent(interval=1)
    a173013 = 'Memory: ' + str(mem.percent) + '%' + ' (' + str(mem.used / 1024 / 1024) + ' / ' + str(mem.total / 1024 / 1024) + 'MB' + ')'
    await ctx.send(a173013)
    a124897 = 'CPU: ' + str(cpu) + '%'
    await ctx.send(a124897)

@bot.command()
async def seen(ctx):
    """: ネタをランダムで選び表示します。"""
    a47901 = randomint(1, 4)
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
        await ctx.send(' by ちゃ')

@bot.command()
async def time(ctx):
    now = datetime.datetime.now()
    sendms = discord.Embed(title='Time', description=now.strftime("%Y/%m/%d %H:%M:%S.%f"), colour=0x7ED6DE)
    sendms.set_footer(text=now.strftime("Time: %Y/%m/%d %H:%M:%S.%f"))
    await ctx.send(embed=sendms)

@bot.command()
async def math(ctx, *, arg):
    await ctx.send('{}'.format(arg))

@bot.command()
async def music(ctx):
    """: Botの作成者が現時点で気に入っている曲のYouTubeリンクをチャンネルにアップロードします。"""
    await ctx.send('PSYQUI, Mo∀ - Rainbow Dream')
    await ctx.send('https://www.youtube.com/watch?v=BCM423NDOE0')
    await ctx.sen





>>>>>>> parent of a581418... Update commandnetworkbotdiscordext.py
bot.run(token)
