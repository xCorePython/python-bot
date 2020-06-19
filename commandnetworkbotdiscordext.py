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

@bot.command(aliases=["connect","summon"]) #connectやsummonでも呼び出せる
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

    ffmpeg_audio_source = discord.FFmpegPCMAudio("music/{}.mp3".format(arg))
    voice_client.play(ffmpeg_audio_source)

bot.run(token)
