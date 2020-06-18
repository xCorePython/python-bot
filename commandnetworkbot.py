import datetime
now = datetime.datetime.now()
starttime = float(now.strftime("0.%f")) + int(now.second) + int(int(now.day) * 86400) + int(int(now.hour) * 3600) + int(int(now.minute) * 60)
import os
import discord
client = discord.Client()
import psutil
import random
import time
import requests
import asyncio
now = datetime.datetime.now()
importtime = float(now.strftime("0.%f")) + int(now.second) + int(int(now.day) * 86400) + int(int(now.hour) * 3600) + int(int(now.minute) * 60)
global voice
global activityst
global uptime2
global readytime
global nowtime
global whileonoff




    
token = 'NjgwNzAwMzc4OTI4NjQ0MTE3.XsG6AQ.zkuCC2kX7vL6EFpnqIOFI9e13-g'
version = 'v3.1.06 beta'
updatelog = 'コマンドを増やしました。'
information = 'Beta版なのでバグがまだあります。`Cn!report <バグ内容>`で報告してください！'
updatelogsw = 'f'
prefix = 'Cn!'

@client.event
async def on_ready():
    if updatelogsw == 't':
        startupst = discord.Embed(title='Command Network Botがアップデートされました', description=version, colour=0x00ffff)
        now = datetime.datetime.now()
        startupst.set_footer(text=now.strftime("Time: %Y/%m/%d %H:%M:%S.%f"))
        startupst.add_field(name='更新内容', value=information, inline=False)
        startupst.add_field(name='お知らせ', value=updatelog, inline=False)
        channel = client.get_channel(707426067098501171)
        await channel.send(embed=startupst)
    now = datetime.datetime.now()
    readytime = float(now.strftime("0.%f")) + int(now.second) + int(int(now.day) * 86400) + int(int(now.hour) * 3600) + int(int(now.minute) * 60)
    activityst = prefix + 'help' + ' | ' + 'Startup Time : ' + str(float(readytime - starttime)) + 's | ' + 'Import Time : ' + str(float(importtime - starttime)) + 's | ' + version
    await client.change_presence(activity=discord.Game(activityst))

@client.event
async def on_message(message):
    if message.content.startswith(prefix):
        if message.content == prefix + 'help':
            sendms = discord.Embed(title="コマンド一覧", description="Cn!help <コマンド名>で詳細が見れます", color=0x00ffff)
            sendms.set_footer(text="This bot created by Aquatic_Core")
            sendms.add_field(name="Tool", value='`timer`,`check`,`time`', inline=False)
            sendms.add_field(name="Status", value='`check`,`status`', inline=False)
            await message.channel.send(embed=sendms)
        if message.content.startswith('Cn!say '):
            sendms = discord.Embed(description=f"{message.content}"[7:], colour=0xF46900)
            sendms.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            now = datetime.datetime.now()
            await message.channel.send(embed=sendms)
        if message.content == prefix + 'time':
            now = datetime.datetime.now()
            sendms = discord.Embed(title='Time', description=now.strftime("%Y/%m/%d %H:%M:%S.%f"), colour=0x7ED6DE)
            await message.channel.send(embed=sendms)
        if message.content.startswith('Cn!stopwatch '):
            arg = message.content[13:]
            if arg == 'start':
                now = datetime.datetime.now()
                nowtime = float(now.strftime("0.%f")) + int(now.second) + int(int(now.day) * 86400) + int(int(now.hour) * 3600) + int(int(now.minute) * 60)
                with open('stopwatch/{}.txt'.format(message.author.id), 'w', encoding = 'utf_8') as f:
                    f.write(str(nowtime))
            if arg == 'now':
                now = datetime.datetime.now()
                nowtime = float(now.strftime("0.%f")) + int(now.second) + int(int(now.day) * 86400) + int(int(now.hour) * 3600) + int(int(now.minute) * 60)
                readms = open('stopwatch/{}.txt'.format(message.author.id), 'r', encoding = 'utf_8')
                readtime = readms.read()
                currenttime = float(nowtime) - float(readtime)
                if currenttime > 3600:
                    sw02 = int(currenttime / 3600)
                    sw01 = int(currenttime - 3600 * sw02)
                    sw00 = float(currenttime - 60 * sw01)
                    if sw00 < 10:
                        sendms = 'Now Time : ' + str(sw01) + ':0' + str(sw00)
                        await message.channel.send(sendms)
                    else:
                        sendms = 'Now Time : ' + str(sw01) + ':' + str(sw00)
                        await message.channel.send(sendms)
                if currenttime > 60:
                    sw01 = int(currenttime / 60)
                    sw00 = float(currenttime - 60 * sw01)
                    if sw00 < 10:
                        sendms = 'Now Time : ' + str(sw01) + ':0' + str(sw00)
                        await message.channel.send(sendms)
                    else:
                        sendms = 'Now Time : ' + str(sw01) + ':' + str(sw00)
                        await message.channel.send(sendms)
                else:
                    sw00 = float(currenttime)
                    if sw00 < 10:
                        sendms = 'Now Time : ' + str(sw00)
                        await message.channel.send(sendms)
                    else:
                        sendms = 'Now Time : ' + str(sw00)
                        await message.channel.send(sendms)
        if message.content.startswith('Cn!timer '):
            arg = int(message.content[9:])
            await asyncio.sleep(arg)
            await message.channel.send('Timer Finished!\n<@{}>'.format(message.author.id))
        if message.content.startswith('Cn!report '):
            arg = str(message.content[10:])
            savems = '内容 : ' + arg + '\n' + '報告者ID : ' + str(message.author.id) + '\n\n'
            await message.channel.send('報告ありがとうございます。')
            with open('bugreport/{}.txt'.format(message.author.name), 'a', encoding = 'utf_8') as f:
                f.write(savems)
        if message.content == 'Cn!ping':
            now = datetime.datetime.now()
            ping1 = float(now.strftime("0.%f")) + int(now.second) + int(int(now.day) * 86400) + int(int(now.hour) * 3600) + int(int(now.minute) * 60)
            await message.channel.send('Pong!')
            now = datetime.datetime.now()
            ping2 = float(now.strftime("0.%f")) + int(now.second) + int(int(now.day) * 86400) + int(int(now.hour) * 3600) + int(int(now.minute) * 60)
            sendms = str(float(float(ping2 - ping1) * 1000)) + 'ms'
            await message.channel.send(sendms)
        if message.content.startswith('Cn!check '):
            arg = str(message.content[9:])
            data = requests.get("https://api.mcsrvstat.us/2/{}".format(arg)).json()
            if data['online'] == True:
                sendms = discord.Embed(title="Minecraft Server Check", description="This server is online!", colour=0x7ED6DE)
                sendms.add_field(name='Hostname', value=str(data['hostname']), inline=False)
                sendms.add_field(name='IP Address', value=str(data['ip']), inline=False)
                sendms.add_field(name='Port', value=str(data['port']), inline=False)
                sendms1 = str(data['players']['online']) + '/' + str(data['players']['max'])
                sendms.add_field(name='Players', value=str(sendms1), inline=False)
                sendms.add_field(name='Version', value=str(data['version']), inline=False)
                now = datetime.datetime.now()
                sendms.set_footer(text=now.strftime("Time: %Y/%m/%d %H:%M:%S.%f"))
                await message.channel.send(embed=sendms)
            if data['ip'] == data['port']:
                sendms = discord.Embed(title="Minecraft Server Check", description="The server not found.", colour=0x7ED6DE)
                now = datetime.datetime.now()
                sendms.set_footer(text=now.strftime("Time: %Y/%m/%d %H:%M:%S.%f"))
                await message.channel.send(embed=sendms)
            if data['online'] == False:
                sendms = discord.Embed(title="Minecraft Server Check", description="This server is offline...", colour=0x7ED6DE)
                sendms.add_field(name='Hostname', value=str(data['hostname']), inline=False)
                sendms.add_field(name='IP Address', value=str(data['ip']), inline=False)
                sendms.add_field(name='Port', value=str(data['port']), inline=False)
                now = datetime.datetime.now()
                sendms.set_footer(text=now.strftime("Time: %Y/%m/%d %H:%M:%S.%f"))
                await message.channel.send(embed=sendms)
                
        if message.content.startswith('Cn!upload '):
            arg = message.content[10:]
            await message.channel.send(file=discord.File('uploader/{}'.format(arg)))
        if message.content == 'Cn!join':
            voice = await discord.VoiceChannel.connect(message.author.voice.channel)
        if message.content.startswith('Cn!music '):
            arg = message.content[9:]

            voice = await discord.VoiceChannel.connect(message.author.voice.channel)
            voice.play(discord.FFmpegPCMAudio('music/{}.mp3'.format(arg)))


        if message.content == 'Cn!dc':

            await voice.disconnect()
        if message.content == 'Cn!status':
            await message.channel.send(activityst)
    if message.content == 'おみくじ':
        omikuji = [ '大吉', '中吉', '小吉', '吉', '末吉', '凶', '小凶', '中凶', '大凶' ]
        sendms = random.choice(omikuji)
        await message.channel.send(sendms)
    if message.content.find('おみくじ') != -1:
        await message.channel.send('test')
    if message.content.find('よかったね') != -1:
        await message.channel.send('うんほんとによかった！')
    if message.content.find('良かったね') != -1:
        await message.channel.send('うんほんとによかった！')
    if message.content.find('kusa') != -1:
        await message.channel.send('www')
    if message.content.find('草') != -1:
        await message.channel.send('www')
    if message.content.find('くさ') != -1:
        await message.channel.send('www')
    if message.content.find('クサ') != -1:
        await message.channel.send('www')
    if message.content.find('ｸｻ') != -1:
        await message.channel.send('www')
    if message.content.find('KUSA') != -1:
        await message.channel.send('www')
    if message.content.find('いいね') != -1:
        await message.channel.send('いい！')
    if message.content.find('f**k') != -1:
        await message.channel.send('暴言！')
    if message.content.find('fuck') != -1:
        await message.channel.send('暴言！')
    if message.content.find('Fuck') != -1:
        await message.channel.send('暴言！')
    if message.content.find('F**k') != -1:
        await message.channel.send('暴言！')
    if message.content.find('fk') != -1:
        await message.channel.send('暴言！')
    if message.content.find('死ね') != -1:
        await message.channel.send('暴言！')
    if message.content.find('しね') != -1:
        await message.channel.send('暴言！')
    if message.content.find('tintin') != -1:
        await message.channel.send('ﾊﾊｯ!')
    if message.content.find('wwww') != -1:
        await message.channel.send('www')
    if message.content.find('ｗｗｗｗ') != -1:
        await message.channel.send('www')
    if message.content.find('じゃね？w') != -1:
        await message.channel.send('それなwww')
    if message.content.find('じゃね？ｗ') != -1:
        await message.channel.send('それなwww')
    if message.content.find('じゃね?w') != -1:
        await message.channel.send('それなwww')

client.run(token)
