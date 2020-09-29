import datetime
now = datetime.datetime.now()
starttime = float(now.strftime("0.%f")) + int(now.second) + int(int(now.day) * 86400) + int(int(now.hour) * 3600) + int(int(now.minute) * 60)
import calendar, os, discord, psutil, random, time, requests, asyncio, sys, youtube_dl, json, subprocess, googletrans, bs4
now = datetime.datetime.now()
importtime = float(now.strftime("0.%f")) + int(now.second) + int(int(now.day) * 86400) + int(int(now.hour) * 3600) + int(int(now.minute) * 60)
#global 

sys_token = 'NzYwNDkwNjYwNDQzODQ4NzM0.X3M0Hg.lTDx_AvmNNr1spqwUo1wqetaVlM'
sys_token2 = 'NjgwOTAxMTEyOTA3NTYzMDcx.XxLShg.NdGG5gd8gQ9_GGTqomBBqSfRC08'
sys_version = 'v3.2.10'
ready_log = 'infoコマンドのバグを修正'
ready_log2 = 'memoコマンドを追加'
ready_info = 'バグがある可能性があります。`Cn!report <バグ内容>`で報告してください！'
ready_send = 'f'
command_prefix = 'Cn!'
command_count = '17'
sys_module_count = '15'
sys_loop = 1
client = discord.Client()
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': "youtube/" + "%(id)s" + '.%(ext)s',
    'postprocessors': [
        {'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
         'preferredquality': '64'},
        {'key': 'FFmpegMetadata'},
    ],
}
ydl_opts2 = {
    'format': 'bestaudio/best',
    'outtmpl': "youtube/" + "%(id)s" + '.%(ext)s',
    'postprocessors': [
        {'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
         'preferredquality': '256'},
        {'key': 'FFmpegMetadata'},
    ],
}
ydl_opts3 = {
    'format': 'bestaudio/best',
    'outtmpl': "youtube/" + "%(id)s" + '.%(ext)s',
    'postprocessors': [
        {'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
         'preferredquality': '128'},
        {'key': 'FFmpegMetadata'},
    ],
}

def append_json_to_file(data: dict, path_file: str) -> bool:
    with open(path_file, 'ab+') as f:              # ファイルを開く
        f.seek(0,2)                                # ファイルの末尾（2）に移動（フォフセット0）  
        if f.tell() == 0 :                         # ファイルが空かチェック
            f.write(json.dumps([data]).encode())   # 空の場合は JSON 配列を書き込む
        else :
            f.seek(-1,2)                           # ファイルの末尾（2）から -1 文字移動
            f.truncate()                           # 最後の文字を削除し、JSON 配列を開ける（]の削除）
            f.write(' , '.encode())                # 配列のセパレーターを書き込む
            f.write(json.dumps(data).encode())     # 辞書を JSON 形式でダンプ書き込み
            f.write(']'.encode())                  # JSON 配列を閉じる
    return f.close() # 連続で追加する場合は都度 Open, Close しない方がいいかも

def now_month(mode):
        if mode == 'total':
            now = datetime.datetime.now()
            if now.month == 1:
                a01 = 0
                for n in range(1):
                    nowcalendar = str(calendar.month(int('{}'.format(now.year)), int('{}'.format(n))))
                    a01 = a01 + int(nowcalendar[int(len(nowcalendar) - 3):int(len(nowcalendar) - 1)])
                a01 = a01 + now.day
                return a01
            if now.month == 2:
                a01 = 0
                for n in range(1, 2):
                    nowcalendar = str(calendar.month(int('{}'.format(now.year)), int('{}'.format(n))))
                    a01 = a01 + int(nowcalendar[int(len(nowcalendar) - 3):int(len(nowcalendar) - 1)])
                a01 = a01 + now.day
                return a01
            if now.month == 3:
                a01 = 0
                for n in range(1, 3):
                    nowcalendar = str(calendar.month(int('{}'.format(now.year)), int('{}'.format(n))))
                    a01 = a01 + int(nowcalendar[int(len(nowcalendar) - 3):int(len(nowcalendar) - 1)])
                a01 = a01 + now.day
                return a01
            if now.month == 4:
                a01 = 0
                for n in range(1, 4):
                    nowcalendar = str(calendar.month(int('{}'.format(now.year)), int('{}'.format(n))))
                    a01 = a01 + int(nowcalendar[int(len(nowcalendar) - 3):int(len(nowcalendar) - 1)])
                a01 = a01 + now.day
                return a01
            if now.month == 5:
                a01 = 0
                for n in range(1, 5):
                    nowcalendar = str(calendar.month(int('{}'.format(now.year)), int('{}'.format(n))))
                    a01 = a01 + int(nowcalendar[int(len(nowcalendar) - 3):int(len(nowcalendar) - 1)])
                a01 = a01 + now.day
                return a01
            if now.month == 6:
                a01 = 0
                for n in range(1, 6):
                    nowcalendar = str(calendar.month(int('{}'.format(now.year)), int('{}'.format(n))))
                    a01 = a01 + int(nowcalendar[int(len(nowcalendar) - 3):int(len(nowcalendar) - 1)])
                a01 = a01 + now.day
                return a01
            if now.month == 7:
                a01 = 0
                for n in range(1, 7):
                    nowcalendar = str(calendar.month(int('{}'.format(now.year)), int('{}'.format(n))))
                    a01 = a01 + int(nowcalendar[int(len(nowcalendar) - 3):int(len(nowcalendar) - 1)])
                a01 = a01 + now.day
                return a01
            if now.month == 8:
                a01 = 0
                for n in range(1, 8):
                    nowcalendar = str(calendar.month(int('{}'.format(now.year)), int('{}'.format(n))))
                    a01 = a01 + int(nowcalendar[int(len(nowcalendar) - 3):int(len(nowcalendar) - 1)])
                    a01 = a01 + now.day
                return a01
            if now.month == 9:
                a01 = 0
                for n in range(1, 9):
                    nowcalendar = str(calendar.month(int('{}'.format(now.year)), int('{}'.format(n))))
                    a01 = a01 + int(nowcalendar[int(len(nowcalendar) - 3):int(len(nowcalendar) - 1)])
                a01 = a01 + now.day
                return a01
            if now.month == 10:
                a01 = 0
                for n in range(1, 10):
                    nowcalendar = str(calendar.month(int('{}'.format(now.year)), int('{}'.format(n))))
                    a01 = a01 + int(nowcalendar[int(len(nowcalendar) - 3):int(len(nowcalendar) - 1)])
                a01 = a01 + now.day
                return a01
            if now.month == 11:
                a01 = 0
                for n in range(1, 11):
                    nowcalendar = str(calendar.month(int('{}'.format(now.year)), int('{}'.format(n))))
                    a01 = a01 + int(nowcalendar[int(len(nowcalendar) - 3):int(len(nowcalendar) - 1)])
                a01 = a01 + now.day
                return a01
            if now.month == 12:
                a01 = 0
                for n in range(1, 12):
                    nowcalendar = str(calendar.month(int('{}'.format(now.year)), int('{}'.format(n))))
                    a01 = a01 + int(nowcalendar[int(len(nowcalendar) - 3):int(len(nowcalendar) - 1)])
                a01 = a01 + now.day
                return a01
        if mode == 'month':
            now = datetime.datetime.now()
            nowcalendar = str(calendar.month(int('{}'.format(now.year)), int('{}'.format(now.month))))
            a01 = int(nowcalendar[int(len(nowcalendar) - 3):int(len(nowcalendar) - 1)])
            return a01
    
def now_date(mode, location):
    if mode == 'off':
        now = datetime.datetime.utcnow()
        return float(now.strftime("0.%f")) + int(now.second) + int(int(int(now.month * 365) + int(now_month(month))) * 86400) + int(int(now.day) * 86400) + int(int(now.hour) * 3600) + int(int(now.minute) * 60)
    if mode == 'on':
        now = datetime.datetime.utcnow()
        locationtime = location
        year = now.year
        hour = now.hour + locationtime
        day = now.day
        month = now.month
        if hour > 24:
            hour2 = hour / 24
            hour1 = hour - hour2 * 24
            day = day + 1
            if day > nowmonth(month):
                month = month + 1
                if month > 12:
                    month = month - 12
                    year = year + 1
        a01 = datetime.datetime(year, month, day, hour, now.minute, now.second, int(now.strftime("%f")))
        return a01.strftime("%Y/%m/%d %H:%M:%S.%f")

def ready(mode):
    if mode == 'save':
        now = datetime.datetime.utcnow()
        readytime = float(now.strftime("0.%f")) + int(now.second) + int(int(int(now.month * 365) + int(now_month(month))) * 86400) + int(int(now.day) * 86400) + int(int(now.hour) * 3600) + int(int(now.minute) * 60)
        activityst = str(int(float(readytime - starttime) * 1000)) + 'ms,' + str(int(float(importtime - starttime) * 1000)) + 'ms'
        return activityst
    else:
        return readytime

#await channel.send('[Bot.1] [{0}] {1}'.format('', ''))
#'Startup Time : ' +  | '

@client.event
async def on_ready():
    if sys.version.startswith('3.8.3'):
        deploy_count = open('data/system/deploy/count.txt', 'r', encoding = 'utf_8').read()
        with open('data/system/deploy/count.txt', 'w', encoding = 'utf_8') as f:
            f.write(str(int(deploy_count) + 1))
    if ready_send == 't':
        startupst = discord.Embed(title='Command Network Botがアップデートされました', description=sys_version, colour=0x00ffff)
        temp01 = now_date('on', 9)
        with open('data/system/update/date.txt', 'w', encoding = 'utf_8') as f:
            f.write(temp01)
        temp02 = 'Update Time : ' + temp01
        startupst.set_footer(text=temp02)
        startupst.add_field(name='更新内容', value=ready_log, inline=False)
        startupst.add_field(name='次回更新予定内容', value=ready_log2, inline=False)
        startupst.add_field(name='お知らせ', value=ready_info, inline=False)
        channel = client.get_channel(707426067098501171)
        await channel.send(embed=startupst)
    now = datetime.datetime.now()
    activityst = command_prefix + 'help' + ' | ' + sys_version
    await client.change_presence(activity=discord.Game(activityst))

@client.event
async def on_message(message):
    if message.author.id == 680700378928644117:
        return
    if message.author.id == 637672964292214804:
        if message.content.startswith('Cn!admin uploader '):
            arg = message.content[18:]
            await message.channel.send(file=discord.File(arg))
    if message.content.startswith(command_prefix):
        if message.content == 'Cn!help':
            sendms = discord.Embed(title="コマンド一覧", description="Cn!help <コマンド名>で詳細が見れます", color=0x00ffff)
            sendms.set_footer(text="This bot created by Core_Force_")
            sendms.add_field(name="Tool", value='`timer`,`check`,`time`,`stopwatch`,`google`,`random`,`translate`', inline=False)
            sendms.add_field(name="Status", value='`check`,`status`,`info`,`about`,`information`', inline=False)
            sendms.add_field(name="Other", value='`say`,`uploader`,`omikuji`,`ping`,`seen`', inline=False)
            await message.channel.send(embed=sendms)
        if message.content.startswith('Cn!say '):
            sendms = discord.Embed(description=message.content[7:], colour=0xF46900)
            sendms.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            now = datetime.datetime.now()
            await message.channel.send(embed=sendms)
        if message.content == 'Cn!time':
            temp11 = now_date('on', 9)
            sendms = discord.Embed(title='Time', description=temp11, colour=0x7ED6DE)
            await message.channel.send(embed=sendms)
        if message.content.startswith('Cn!stopwatch '):
            arg = message.content[13:]
            if arg == 'start':
                now = datetime.datetime.utcnow()
                nowtime = float(now.strftime("0.%f")) + int(now.second) + int(int(int(now.month * 365) + int(now_month('total'))) * 86400) + int(int(now.day) * 86400) + int(int(now.hour) * 3600) + int(int(now.minute) * 60)
                with open('stopwatch/{}.txt'.format(message.author.id), 'w', encoding = 'utf_8') as f:
                    f.write(str(nowtime))
                await message.channel.send('Stopwatch started')
            if arg == 'now':
                now = datetime.datetime.utcnow()
                nowtime = float(now.strftime("0.%f")) + int(now.second) + int(int(int(now.month * 365) + int(now_month('total'))) * 86400) + int(int(now.day) * 86400) + int(int(now.hour) * 3600) + int(int(now.minute) * 60)
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
            await message.channel.send('Timer Started!')
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
            now = datetime.datetime.utcnow()
            beforesend = float(now.strftime("0.%f")) + int(now.second) + int(int(int(now.month * 365) + int(now_month('total'))) * 86400) + int(int(now.day) * 86400) + int(int(now.hour) * 3600) + int(int(now.minute) * 60)
            await message.channel.send('Pong!')
            now = datetime.datetime.utcnow()
            aftersend = float(now.strftime("0.%f")) + int(now.second) + int(int(int(now.month * 365) + int(now_month('total'))) * 86400) + int(int(now.day) * 86400) + int(int(now.hour) * 3600) + int(int(now.minute) * 60)
            sendms = discord.Embed(title='Response Bot\'s Ping', colour=0x7ED6DE)
            temp11 = str(int(float(aftersend - beforesend) * 1000)) + 'ms'
            sendms.add_field(name="Response Time", value=temp11, inline=False)
            temp18 = str(psutil.cpu_percent()) + '%, ' + str(psutil.cpu_count(logical=False)) + 'C' + str(psutil.cpu_count()) + 'T, ' + str(psutil.cpu_freq().current) + 'MHz'
            sendms.add_field(name='CPU', value=temp12, inline=False)
            temp19 = str(psutil.virtual_memory().percent) + '%'
            sendms.add_field(name='Memory Usage', value=temp13, inline=False)
            temp111 = 'Time : ' + now_date('on', 9)
            sendms.set_footer(text=temp111)
            await message.channel.send(embed=sendms)
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
                temp21 = 'Time : ' + now_time('on', 9)
                sendms.set_footer(text=temp13)
                await message.channel.send(embed=sendms)
            if data['ip'] == data['port']:
                sendms = discord.Embed(title="Minecraft Server Check", description="The server not found.", colour=0x7ED6DE)
                now = datetime.datetime.now()
                temp21 = 'Time : ' + now_time('on', 9)
                sendms.set_footer(text=temp13)
                await message.channel.send(embed=sendms)
            if data['online'] == False:
                sendms = discord.Embed(title="Minecraft Server Check", description="This server is offline...", colour=0x7ED6DE)
                sendms.add_field(name='Hostname', value=str(data['hostname']), inline=False)
                sendms.add_field(name='IP Address', value=str(data['ip']), inline=False)
                sendms.add_field(name='Port', value=str(data['port']), inline=False)
                temp21 = 'Time : ' + now_time('on', 9)
                sendms.set_footer(text=temp13)
                await message.channel.send(embed=sendms)
        if message.content.startswith('Cn!uploader '):
            arg = message.content[10:]
            await message.channel.send(file=discord.File('uploader/{}'.format(arg)))
        if message.content.startswith('Cn!ytdl '):
            arg = message.content.split(' ')
            if len(arg) == 2:
                ydl = youtube_dl.YoutubeDL(ydl_opts3)
                await message.channel.send('Downloading... (128kbps)')
                info_dict = ydl.extract_info("{}".format(arg[1]), download=True, process=True)
                await message.channel.send(file=discord.File('youtube/{0}.mp3'.format(info_dict['id'])))
            if arg[2] == 'low':
                ydl = youtube_dl.YoutubeDL(ydl_opts)
                await message.channel.send('Downloading... (64kbps)')
                info_dict = ydl.extract_info("{}".format(arg[1]), download=True, process=True)
                await message.channel.send(file=discord.File('youtube/{0}.mp3'.format(info_dict['id'])))
            if arg[2] == 'high':
                ydl = youtube_dl.YoutubeDL(ydl_opts2)
                await message.channel.send('Downloading... (256kbps)')
                info_dict = ydl.extract_info("{}".format(arg[1]), download=True, process=True)
                await message.channel.send(file=discord.File('youtube/{0}.mp3'.format(info_dict['id'])))
            else:
                ydl = youtube_dl.YoutubeDL(ydl_opts3)
                await message.channel.send('Downloading... (128kbps)')
                info_dict = ydl.extract_info("{}".format(arg[1]), download=True, process=True)
                await message.channel.send(file=discord.File('youtube/{0}.mp3'.format(info_dict['id'])))
        if message.content == 'Cn!status':
            await message.channel.send(activityst)
        if message.content.startswith('Cn!google '):
                arg = message.content[10:]
                result = requests.get('https://www.google.com/search?q={}/'.format(arg))
                soup = bs4.BeautifulSoup(result.text, 'html.parser')
                list = soup.findAll(True, {'class' : 'BNeawe vvjwJb AP7Wnd'})
                a = str(list).strip('<div class="BNeawe vvjwJb AP7Wnd">')
                b = a.split('</div>, <div class="BNeawe vvjwJb AP7Wnd">')
                c = b[1].split('[<div class="BNeawe vvjwJb AP7Wnd">')
                if len(b) > 9:
                    d = b[9].split('</div>]')
                    e = c + b[2:8] + d
                    temp51 = e[1] + '\n'
                    for n in range(2, int(len(b) - 2)):
                        temp51 = temp51 + e[int(n)] + '\n'
                    sendms = discord.Embed(title='Search Results : {}'.format(arg), description=temp51, colour=0x7ED6DE)
                    await message.channel.send(embed=sendms)
                else:
                    e = c + b[2:8]
                    temp51 = e[1] + '\n'
                    for n in range(2, int(len(b) - 2)):
                        temp51 = temp51 + e[int(n)] + '\n'
                    sendms = discord.Embed(title='Search Results : {}'.format(arg), description=temp51, colour=0x7ED6DE)
                    await message.channel.send(embed=sendms)
        if message.content == 'Cn!seen':
            a47901 = random.randint(1, 8)
            if a47901 == 1:
                await message.channel.send(file=discord.File('neta/neta1.mp4'))
            elif a47901 == 2:
                await message.channel.send(file=discord.File('neta/neta2.mp4'))
            elif a47901 == 3:
                await message.channel.send(file=discord.File('neta/neta3.png'))
            elif a47901 == 4:
                await message.channel.send(file=discord.File('neta/neta4.mp4'))
            elif a47901 == 5:
                await message.channel.send(file=discord.File('neta/neta5.jpg'))
            elif a47901 == 6:
                await message.channel.send(file=discord.File('neta/neta6.png'))
            elif a47901 == 7:
                await message.channel.send(file=discord.File('neta/neta7.png'))
                await message.channel.send(file=discord.File('neta/neta8.png'))
                await message.channel.send(file=discord.File('neta/neta9.png'))
        if message.content.startswith('Cn!random '):
            arg = message.content.split(' ')
            await message.channel.send(random.randint(int(arg[1]),int(arg[2])))
        if message.content.startswith('Cn!translate '):
            arg = message.content.split(' ')
            if len(arg) == 3:
                translator = googletrans.Translator()
                sendms = translator.translate(arg[1] ,dest=arg[2])
                await message.channel.send(sendms.text)
            if len(arg) == 4:
                translator = googletrans.Translator()
                sendms = translator.translate(arg[1], src=arg[2] ,dest=arg[3])
                await message.channel.send(sendms.text)
            if len(arg) == 2:
                await message.channel.send('引数の数を正しくしてください。')
            if len(arg) > 5:
                await message.channel.send('引数の数を正しくしてください。')
        if message.content.startswith('Cn!memo '):
            arg = message.content.split(' ')
            #if arg[1] == 'add':
                #readms = 
        if message.content == 'Cn!info':
            sendms = discord.Embed(title="Information", colour=0x7ED6DE)
            info_temp = open('data/system/deploy/count.txt', 'r', encoding = 'utf_8').read()
            sendms.add_field(name="Deploy Count", value=info_temp, inline=False)
            sendms.add_field(name="Version", value=sys_version, inline=False)
            info_temp = str(psutil.cpu_percent()) + '%, ' + str(psutil.cpu_count(logical=False)) + 'C' + str(psutil.cpu_count()) + 'T, ' + str(psutil.cpu_freq().current) + 'MHz'
            sendms.add_field(name="CPU Usage", value=info_temp, inline=False)
            info_temp = str(psutil.virtual_memory().percent) + '%'
            sendms.add_field(name="Memory Usage", value=info_temp, inline=False)
            sendms.add_field(name="Owner", value="Core\_Force\_#5668", inline=False)
            sendms.add_field(name="Commands", value=command_count, inline=False)
            sendms.add_field(name="Servers", value=len(client.guilds), inline=False)
            sendms.add_field(name="Packages/Modules", value=sys_module_count, inline=False)
            info_temp = open('data/system/update/date.txt', 'r', encoding = 'utf_8').read()
            sendms.add_field(name="Update Time", value=info_temp, inline=False)
            sendms.add_field(name="Site", value="https://akitama.localinfo.jp/", inline=False)
            sendms.add_field(name="Language", value="English, Japanese", inline=False)
            await message.channel.send(embed=sendms)
        if message.content == 'Cn!omikuji':
            omikuji = [ '大吉', '中吉', '小吉', '吉', '末吉', '凶', '小凶', '中凶', '大凶' ]
            sendms = random.choice(omikuji)
            await message.channel.send(sendms)
    if message.content.find('おみくじ') != -1:
        omikuji = [ '大吉', '中吉', '小吉', '吉', '末吉', '凶', '小凶', '中凶', '大凶' ]
        sendms = random.choice(omikuji)
        await message.channel.send(sendms)
    if message.content.find('よかったね') != -1:
        await message.channel.send('よかったね')
    if message.content.find('良かったね') != -1:
        await message.channel.send('良かったね')
    if message.content.find('kusa') != -1:
        await message.channel.send('ww')
    if message.content.find('草') != -1:
        await message.channel.send('ww')
    if message.content.find('くさ') != -1:
        await message.channel.send('ww')
    if message.content.find('クサ') != -1:
        await message.channel.send('ww')
    if message.content.find('ｸｻ') != -1:
        await message.channel.send('ww')
    if message.content.find('KUSA') != -1:
        await message.channel.send('ww')
    if message.content.find('いいね') != -1:
        await message.channel.send('いいね')
    if message.content.find('f**k') != -1:
        await message.channel.send('暴言！')
    if message.content.find('fuck') != -1:
        await message.channel.send('暴言！')
    if message.content.find('Fuck') != -1:
        await message.channel.send('暴言！')
    if message.content.find('F**k') != -1:
        await message.channel.send('暴言！')
    if message.content.find('死ね') != -1:
        await message.channel.send('暴言！')
    if message.content.find('しね') != -1:
        await message.channel.send('暴言！')
    if message.content.find('tintin') != -1:
        await message.channel.send('ﾊﾊｯ!')
    if message.content.find('w') != -1:
        await message.channel.send('ww')
    if message.content.find('ｗ') != -1:
        await message.channel.send('ww')
    if message.content.find('じゃね？ww') != -1:
        await message.channel.send('それなww')
    if message.content.find('じゃね？ｗｗ') != -1:
        await message.channel.send('それなww')
    if message.content.find('じゃね?w') != -1:
        await message.channel.send('それなww')

client.run(sys_token)
