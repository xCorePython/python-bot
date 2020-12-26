import datetime
now = datetime.datetime.utcnow()
starttime = float(now.strftime("0.%f")) + int(now.second) + int(
    int(now.day) * 86400) + int(int(now.hour) * 3600) + int(
        int(now.minute) * 60)
import calendar, os, discord, psutil, random, requests, asyncio, sys, youtube_dl, googletrans, bs4
now = datetime.datetime.utcnow()
importtime = float(now.strftime("0.%f")) + int(now.second) + int(
    int(now.day) * 86400) + int(int(now.hour) * 3600) + int(
        int(now.minute) * 60)

sys_version = 'v6.0.1'
sys_commands = ['timer', 'check', 'time', 'stopwatch', 'search', 'random', 'translator','check', 'info', 'about', 'say', 'uploader', 'omikuji', 'ping', 'seen', 'downloader', 'reversetranslate', 'play', 'nowplaying', 'queue', 'remove', 'skip', 'report', 'request', 'shuffle', 'clear', 'volume', 'bassboost', 'about', 
]

ready_log = '''
helpコマンドの修正
aboutコマンドを追加
バージョン表示をa.b.cに変更
'''
ready_log2 = '''
docsコマンドを追加
'''
ready_log3 = '''
bassboostコマンドとequalizerコマンドを追加
checkコマンドにサーバーのサムネイルを追加
'''
ready_log = '\n・'.join(ready_log[:-1].split('\n'))[1:]
ready_log2 = '\n・'.join(ready_log2[:-1].split('\n'))[1:]
ready_log3 = '\n・'.join(ready_log3[:-1].split('\n'))[1:]
invite_link = 'https://discord.com/api/oauth2/authorize?client_id=761929481421979669&permissions=8&redirect_uri=https%3A%2F%2Fdiscord.gg%2FbSfDG7WRZS&scope=bot'
ready_info = 'バグがある可能性があります。`Cn!report <バグ内容>`で報告してください！'
command_prefix = 'c.'
command_count = len(sys_commands)
sys_module_count = '13'
sys_loop = 1
client = discord.Client()
vcch = 734217960222228490
vcch = 584262828807028746
color1 = 0x377EF0
color2 = 0xF8C63D
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': "youtube/" + "%(id)s" + '.%(ext)s',
    'ignoreerrors': True,
    'noplaylist': True,
    'postprocessors': [{
    	'key': 'FFmpegExtractAudio',
    	'preferredcodec': 'mp3',
        'preferredquality': '64'},
        {'key': 'FFmpegMetadata'},],
}
ydl_opts2 = {
    'format': 'bestaudio/best',
    'outtmpl': "youtube/" + "%(id)s" + '.%(ext)s',
    'ignoreerrors': True,
    'noplaylist': True,
    'postprocessors': [{
    	'key': 'FFmpegExtractAudio',
    	'preferredcodec': 'mp3',
        'preferredquality': '128'},
        {'key': 'FFmpegMetadata'},],
}

def now_month(mode):
	if mode == 'total':
		now = datetime.datetime.utcnow()
		if now.month == 1:
			a01 = 0
			for n in range(1):
				nowcalendar = str(
				    calendar.month(
				        int('{}'.format(now.year)), int('{}'.format(n))))
				a01 = a01 + int(nowcalendar[int(len(nowcalendar) -
				                                3):int(len(nowcalendar) - 1)])
			a01 = a01 + now.day
			return a01
		if now.month > 2:
			a01 = 0
			for n in range(1, now.month):
				nowcalendar = str(
				    calendar.month(
				        int('{}'.format(now.year)), int('{}'.format(n))))
				a01 = a01 + int(nowcalendar[int(len(nowcalendar) -
				                                3):int(len(nowcalendar) - 1)])
			a01 = a01 + now.day
			return a01
	if mode == 'month':
		now = datetime.datetime.utcnow()
		nowcalendar = str(
		    calendar.month(
		        int('{}'.format(now.year)), int('{}'.format(now.month))))
		a01 = int(
		    nowcalendar[int(len(nowcalendar) - 3):int(len(nowcalendar) - 1)])
		return a01


def now_date(mode, location):
	if mode == 'off':
		now = datetime.datetime.utcnow()
		return float(now.strftime("0.%f")) + int(now.second) + int(
		    int(int(now.month * 365) + int(now_month('month'))) * 86400) + int(int(now.day) * 86400) + int(int(now.hour) * 3600) + int(int(now.minute) * 60)
	if mode == 'on':
		now = datetime.datetime.utcnow()
		locationtime = location
		year = now.year
		hour = now.hour + locationtime
		day = now.day
		month = now.month
		if hour > 24:
			hour2 = hour / 24
			hour = hour - hour2 * 24
			day = day + 1
			if day > now_month('month'):
				month = month + 1
				if month > 12:
					month = month - 12
					year = year + 1
		a01 = datetime.datetime(year, month, day, hour, now.minute, now.second, int(now.strftime("%f")))
		return a01.strftime("%Y/%m/%d %H:%M:%S.%f")

def reverse(data):
	time = int(float(data))
	if time < 10:
		second = int(time)
		uptime = '0:0' + str(second)
		return uptime
	if time >= 60:
		if time < 3600:
			minute = int(time / 60)
			second = int(time - minute * 60)
			if second < 10:
				uptime = str(minute) + ':0' + str(second)
				return uptime
			else:
				uptime = str(minute) + ':' + str(second)
				return uptime
		else:
			hour = int(time / 3600)
			minute = int(int(time - hour * 3600) / 60)
			second = int(time - hour * 3600 - minute * 60)
			if minute < 10:
				if second < 10:
					uptime = str(hour) + ':0' + str(minute) + ':0' + str(
					    second)
					return uptime
				else:
					uptime = str(hour) + ':0' + str(minute) + ':' + str(second)
					return uptime
			else:
				if second < 10:
					uptime = str(hour) + ':' + str(minute) + ':0' + str(second)
					return uptime
				else:
					uptime = str(hour) + ':' + str(minute) + ':' + str(second)
					return uptime
	else:
		uptime = '0:' + str(time)
		return uptime


async def log(level, info):
	await client.get_channel(773053692629876757).send('[{0}] {1}'.format(
	    level, info))


async def messages(channelid):
	messages = await client.get_channel(channelid).history(limit=1).flatten()
	for message in messages:
		return message.content


async def send(channelid, content, mode):
	if mode == 9:
		await client.get_channel(channelid).send(embed=content)
	else:
		await client.get_channel(channelid).send(content)


async def status(content):
	await client.change_presence(activity=discord.Game(content))

async def commands(command, message):
	arg = message.content.split(' ')[1:]
	if command == 'say':
		sendms = discord.Embed(
		    description=' '.join(arg), colour=0xF46900)
		sendms.set_author(
		    name=message.author.name, icon_url=message.author.avatar_url)
		await message.channel.send(embed=sendms)
	elif command == 'time':
		temp11 = now_date('on', 9)
		sendms = discord.Embed(
		    title='Time', description=temp11, colour=0x7ED6DE)
		await message.channel.send(embed=sendms)
	elif command == 'stopwatch':
		arg = ' '.join(arg)
		if arg == 'start':
			now = datetime.datetime.utcnow()
			nowtime = float(now.strftime("0.%f")) + int(now.second) + int(
			    int(int(now.month * 365) + int(now_month('total')))
			    * 86400) + int(int(now.day) * 86400) + int(
			        int(now.hour) * 3600) + int(int(now.minute) * 60)
			with open(
			    'stopwatch/{}.txt'.format(message.author.id),
			    'w',
			    encoding='utf_8') as f:
				f.write(str(nowtime))
			await message.channel.send('Stopwatch started')
		if arg == 'now':
			now = datetime.datetime.utcnow()
			nowtime = float(now.strftime("0.%f")) + int(now.second) + int(
			    int(int(now.month * 365) + int(now_month('total')))
			    * 86400) + int(int(now.day) * 86400) + int(
			        int(now.hour) * 3600) + int(int(now.minute) * 60)
			readms = open(
			    'stopwatch/{}.txt'.format(message.author.id),
			    'r',
			    encoding='utf_8')
			readtime = readms.read()
			currenttime = float(nowtime) - float(readtime)
			await message.channel.send(reverse(currenttime))
	elif command == 'timer':
		arg = int(' '.join(arg))
		try:
			await message.channel.send('Timer Started!')
			await asyncio.sleep(arg)
			await message.channel.send('Timer Finished!\n<@{}>'.format(message.author.id))
		except:
			await message.channel.send(':x: Failed starting timer')
	elif command == 'report':
		await message.channel.send('報告ありがとうございます。')
		await client.get_user(783669082641137664).send(
		    'Report: {0}({1}) | {2}'.format(message.author.name,message.author.id, ' '.join(arg)))
	elif command == 'request':
	    await message.channel.send(':white_check_mark: リクエストを正常に受け取りました')
	    await client.get_user(783669082641137664).send(
		    'Request: {0}({1}) | {2}'.format(message.author.name,message.author.id, ' '.join(arg)))
	elif command == 'ping':
		now = datetime.datetime.utcnow()
		beforesend = float(now.strftime("0.%f")) + int(now.second) + int(
		    int(int(now.month * 365) + int(now_month('total'))) * 86400) + int(
		        int(now.day) * 86400) + int(int(now.hour) * 3600) + int(
		            int(now.minute) * 60)
		editms = await message.channel.send('Pong!')
		now = datetime.datetime.utcnow()
		aftersend = float(now.strftime("0.%f")) + int(now.second) + int(
		    int(int(now.month * 365) + int(now_month('total'))) * 86400) + int(
		        int(now.day) * 86400) + int(int(now.hour) * 3600) + int(
		            int(now.minute) * 60)
		sendms = discord.Embed(title='Bot\'s Ping', colour=0x7ED6DE)
		temp11 = str(int(float(aftersend - beforesend) * 1000)) + 'ms'
		sendms.add_field(name="Response Time", value=temp11, inline=False)
		temp12 = await messages(770902347667996672)
		temp13 = temp12.split(',')
		sendms.add_field(name="Startup Time", value=temp13[0], inline=False)
		sendms.add_field(name="Import Time", value=temp13[1], inline=False)
		temp18 = str(psutil.cpu_percent()) + '%, ' + str(
		    psutil.cpu_count(logical=False)) + 'C' + str(
		        psutil.cpu_count()) + 'T, ' + str(
		            psutil.cpu_freq().current) + 'MHz'
		sendms.add_field(name='CPU', value=temp18, inline=False)
		temp19 = str(psutil.virtual_memory().percent) + '%'
		sendms.add_field(name='Memory Usage', value=temp19, inline=False)
		temp111 = 'Time : ' + now_date('on', 9)
		sendms.set_footer(text=temp111)
		await editms.edit(content=None, embed=sendms)
	elif command == 'check':
		arg = str(message.content[9:])
		data = requests.get("https://api.mcsrvstat.us/2/{}".format(arg)).json()
		if data['online'] == True:
			sendms = discord.Embed(
			    title="Minecraft Server Check",
			    description="This server is online!",
			    colour=0x7ED6DE)
			sendms.add_field(
			    name='Hostname', value=str(data['hostname']), inline=False)
			sendms.add_field(
			    name='IP Address', value=str(data['ip']), inline=False)
			sendms.add_field(
			    name='Port', value=str(data['port']), inline=False)
			sendms1 = str(data['players']['online']) + '/' + str(
			    data['players']['max'])
			sendms.add_field(name='Players', value=str(sendms1), inline=False)
			sendms.add_field(
			    name='Version', value=str(data['version']), inline=False)
			temp21 = 'Time : ' + now_date('on', 9)
			sendms.set_footer(text=temp21)
			await message.channel.send(embed=sendms)
		if data['ip'] == data['port']:
			sendms = discord.Embed(
			    title="Minecraft Server Check",
			    description="The server not found.",
			    colour=0x7ED6DE)
			temp21 = 'Time : ' + now_date('on', 9)
			sendms.set_footer(text=temp21)
			await message.channel.send(embed=sendms)
		if data['online'] == False:
			sendms = discord.Embed(
			    title="Minecraft Server Check",
			    description="This server is offline...",
			    colour=0x7ED6DE)
			sendms.add_field(
			    name='Hostname', value=str(data['hostname']), inline=False)
			sendms.add_field(
			    name='IP Address', value=str(data['ip']), inline=False)
			sendms.add_field(
			    name='Port', value=str(data['port']), inline=False)
			temp21 = 'Time : ' + now_date('on', 9)
			sendms.set_footer(text=temp21)
			await message.channel.send(embed=sendms)
	elif command == 'uploader':
		arg = message.content[10:]
		await message.channel.send(
		    file=discord.File('uploader/{}'.format(arg)))
	elif command == 'downloader':
		arg = message.content.split(' ')
		info = youtube_dl.YoutubeDL().extract_info(
		    arg[1], download=False, process=False)
		link = 'https://youtu.be/{}'.format(info['id'])
		if len(arg) == 2:
			ydl = youtube_dl.YoutubeDL(ydl_opts3)
			await message.channel.send('Downloading... (128kbps)')
			info_dict = ydl.extract_info(link, download=True, process=True)
			await message.channel.send(
			    file=discord.File('youtube/{0}.mp3'.format(info_dict['id'])))
		if arg[2] == 'low':
			ydl = youtube_dl.YoutubeDL(ydl_opts)
			await message.channel.send('Downloading... (64kbps)')
			info_dict = ydl.extract_info(link, download=True, process=True)
			await message.channel.send(
			    file=discord.File('youtube/{0}.mp3'.format(info_dict['id'])))
		if arg[2] == 'high':
			thumbnail = info['thumbnails'][(info['thumbnails']) - 1]['url']
			url = 'https://www.320youtube.com/v11/watch?v={}'.format(
			    info['id'])
			result = requests.get(url)
			soup = bs4.BeautifulSoup(result.text, 'html.parser')
			dllink = str(str(soup).split('href=')[8])[1:].split('" rel')[0]
			sendms = discord.Embed(color=0x7ED6DE)
			sendms.add_field(name='Title', value=info['title'], inline=False)
			sendms.add_field(
			    name='Channel', value=info['uploader'], inline=False)
			sendms.add_field(
			    name='Extractor', value=info['extractor'], inline=False)
			sendms.add_field(name='DL Link', value=dllink, inline=False)
			sendms.set_thumbnail(url=thumbnail)
			sendms.set_footer(
			    text='Powered by 320youtube | https://www.320youtube.com')
			await message.channel.send(embed=sendms)
		else:
			ydl = youtube_dl.YoutubeDL(ydl_opts3)
			await message.channel.send('Downloading... (128kbps)')
			info_dict = ydl.extract_info(link, download=True, process=True)
			await message.channel.send(
			    file=discord.File('youtube/{0}.mp3'.format(info_dict['id'])))
	elif command == 'search':
		arg = message.content[10:]
		result = requests.get(
		    'https://www.google.com/search?q={}/'.format(arg))
		soup = bs4.BeautifulSoup(result.text, 'html.parser')
		list = soup.findAll(True, {'class': 'BNeawe vvjwJb AP7Wnd'})
		a = str(list).strip('<div class="BNeawe vvjwJb AP7Wnd">')
		b = a.split('</div>, <div class="BNeawe vvjwJb AP7Wnd">')
		c = b[1].split('[<div class="BNeawe vvjwJb AP7Wnd">')
		if len(b) > 9:
			d = b[9].split('</div>]')
			e = c + b[2:8] + d
			temp51 = e[1] + '\n'
			for n in range(2, int(len(b) - 2)):
				temp51 = temp51 + e[int(n)] + '\n'
			sendms = discord.Embed(title='Search Results : {}'.format(arg),description=temp51,colour=0x7ED6DE)
			await message.channel.send(embed=sendms)
		else:
			e = c + b[2:8]
			temp51 = e[1] + '\n'
			for n in range(2, int(len(b) - 2)):
				temp51 = temp51 + e[int(n)] + '\n'
			sendms = discord.Embed(title='Search Results : {}'.format(arg),description=temp51,colour=0x7ED6DE)
			await message.channel.send(embed=sendms)
	elif command == 'seen':
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
	elif command == 'random':
		arg = message.content.split(' ')
		await message.channel.send(random.randint(int(arg[1]), int(arg[2])))
	elif command == 'translator':
		while sys_loop == 1:
			try:
				translator = googletrans.Translator()
				translator.translate('hello', dest='ja')
				break
			except:
				print('Retrying...')
		arg = message.content.split(' ')
		temp_trans = len(arg[1]) + len(arg[0]) + 2
		if arg[1].find('>') != -1:
			lang = arg[1].split('>')
			sendms = translator.translate(
			    message.content[temp_trans:], src=lang[1], dest=lang[2])
			await message.channel.send(sendms.text)
		if len(arg) == 2:
			await message.channel.send('引数の数を正しくしてください。')
		else:
			sendms = translator.translate(
			    message.content[temp_trans:], dest=arg[1])
			await message.channel.send(sendms.text)
	elif command == 'reversetranslate':
		while sys_loop == 1:
			try:
				translator = googletrans.Translator()
				translator.translate('hello', dest='ja')
				break
			except:
				print('Retrying...')
		arg = message.content.split(' ')
		temp_trans = len(arg[1]) + len(arg[0]) + 2
		language = [
		    'af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg',
		    'ca', 'ceb', 'ny', 'zh-cn', 'zh-tw', 'co', 'hr', 'cs', 'da', 'nl',
		    'en', 'eo', 'et', 'tl', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el',
		    'gu', 'ht', 'ha', 'haw', 'iw', 'he', 'hi', 'hmn', 'hu', 'is', 'ig',
		    'id', 'ga', 'it', 'ja', 'jw', 'kn', 'kk', 'km', 'ko', 'ku', 'ky',
		    'lo', 'la', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi',
		    'mr', 'mn', 'my', 'ne', 'no', 'or', 'ps', 'fa', 'pl', 'pt', 'pa',
		    'ro', 'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl',
		    'so', 'es', 'su', 'sw', 'sv', 'tg', 'ta', 'te', 'th', 'tr', 'uk',
		    'ur', 'ug', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu'
		]
		sendms4 = translator.translate(message.content[temp_trans:], dest=str(random.choice(language)))
		sendms3 = translator.translate(sendms4.text, dest='ja')
		print(sendms3)
		words = message.content[temp_trans:] + ' > ' + sendms3.text + ' > '
		if len(arg) > 2:
			for n in range(1, int(int(arg[1]) - 2)):
				sendms4 = translator.translate(
				    sendms4.text, dest=str(random.choice(language)))
				sendms2 = translator.translate(sendms4.text, dest='ja')
				print(sendms4)
				print(sendms2)
				words = words + sendms2.text + ' > '
		sendms4 = translator.translate(
		    sendms4.text, dest=str(random.choice(language)))
		ted = translator.translate(sendms4.text, dest='ja')
		print(ted)
		words = words + ted.text
		sendms = discord.Embed(
		    title='Result', description=words, colour=0x7ED6DE)
		await message.channel.send(embed=sendms)
	elif command == 'memo':
		arg = message.content.split(' ')
		#if arg[1] == 'add':
		#readms =
	elif command == 'info':
		sendms = discord.Embed(title="Information", colour=0x7ED6DE)
		sendms.add_field(name='使用プログラム言語', value='Python 3.8.3∼3.9.1', inline=False)
		info_temp = await messages(768764777756622878)
		sendms.add_field(name="デプロイ回数", value=info_temp, inline=False)
		sendms.add_field(name="Version", value=sys_version, inline=False)
		info_temp = str(psutil.cpu_percent()) + '%, ' + str(
		    psutil.cpu_count(logical=False)) + 'C' + str(
		        psutil.cpu_count()) + 'T, ' + str(
		            int(psutil.cpu_freq().current)) + 'MHz'
		sendms.add_field(name="CPU使用率", value=info_temp, inline=False)
		info_temp = str(psutil.virtual_memory().percent) + '%'
		sendms.add_field(name="メモリ使用率", value=info_temp, inline=False)
		sendms.add_field(
		    name="製作者", value="lkechukwuPython#5668", inline=False)
		sendms.add_field(name="コマンド数", value=command_count, inline=False)
		sendms.add_field(
		    name="サーバー数", value=len(client.guilds), inline=False)
		sendms.add_field(
		    name="使用モジュール数", value=sys_module_count, inline=False)
		info_temp = str(await messages(770904260715347988)).split('.')[0]
		sendms.add_field(name="アップデートした時刻", value=info_temp, inline=False)
		info_temp = await messages(770901834558603284)
		info_temp2 = int(float(now_date('off', 9)) - float(info_temp))
		info_temp3 = str(reverse(info_temp2))
		sendms.add_field(name="Uptime", value=info_temp3, inline=False)
		info_temp = await messages(772392566707847180)
		sendms.add_field(name="ビルド回数", value=info_temp, inline=False)
		sendms.add_field(
		    name="サイト", value="https://akitama.localinfo.jp/", inline=False)
		sendms.add_field(
		    name="言語", value="一部英語、基本は日本語", inline=False)
		await message.channel.send(embed=sendms)
	elif command == 'omikuji':
		omikuji = ['大吉', '中吉', '小吉', '吉', '末吉', '凶', '小凶', '中凶', '大凶']
		sendms = random.choice(omikuji)
		await message.channel.send(sendms)
	elif command == 'owner':
	    status = await messages(778387340485722113)
	    if status == 'school':
	        await message.channel.send('Owner is in school now')
	    if status == 'home':
	        await message.channel.send('Owner is at home now')
	elif command == 'command':
		sendms = discord.Embed(title='Command : {}'.format(' '.join(arg)), colour=color1)
		t1 = None
		t2 = 'None'
		t3 = None
		mode = None
		warn = None
		footer = None
		args = None
		if arg[0] ==  'help':
			t1 = 'ヘルプを表示します'
		if arg[0] == 'support':
			t1 = 'サポートになる情報を表示します'
		if arg[0] == 'about':
			t1 = 'Botの詳細を表示します'
		if arg[0] == 'ping':
			t1 = 'Botの遅延等を表示します'
		if arg[0] == 'timer':
			args = '秒数'
			t1 = '秒数を測ります'
		if arg[0] == 'check':
			args = 'サーバーアドレス'
			t1 = '引数に指定されたサーバーアドレスの状態を取得します'
			t3 = 'Minecraft Servers'
		if arg[0] == 'time':
			t1 = '現在の日本の時刻を表示します'
		if arg[0] == 'stopwatch':
			mode = 'start, now'
			args = 'モード'
			t1 = 'スタートしてからの時間を表示します'
			warn = '現在は毎日16時から17時の間にリセットされます'
		if arg[0] == 'search':
			args = '文'
			t1 = '引数に指定した文を検索します'
		if arg[0] == 'random':
			args = 'start, end'
			t1 = 'startとendの間で乱数を生成します'
			ex = 'c.random 1 200'
		if arg[0] == 'translator':
			t2 = 't, trans, tl'
			args = '変換先言語(元言語>変換先言語), 文'
			t1 = '引数に指定された言語に翻訳します'
		if arg[0] == 'downloader':
			mode = 'low(64kbps), high(320kbps), その他のものが指定された場合128kbps'
			warn = 'highはYouTubeのみ可能\n[対応サイト](https://ytdl-org.github.io/youtube-dl/supportedsites.html), [320kbpsに使用したサイト]( https://www.320youtube.com)'
			args = 'mode, url'
			t1 = '指定されたリンクの動画を音声だけにし、送信します'
		if arg[0] == 'play':
			t2 = 'p'
			t1 = '入力された動画をendless-playのキューに追加します'
			args = '動画リンク/動画タイトル'
			footer = 'デフォルト検索サイト: YouTube'
		if arg[0] == 'queue':
			t2 = 'q'
			t1 = 'endless-playのキューを表示します'
		if arg[0] == 'remove':
			t2 = 'r, del, delete, d'
			t1 = 'キューから指定された番号に該当するものを削除します'
			args = '番号'
		if arg[0] == 'nowplaying':
			t2 = 'n, np, now'
			t1 = 'endless-playで再生中の曲を表示します'
		if arg[0] == 'skip':
			t2 = 's'
			t1 = '何も指定されていない場合、再生中の曲をスキップします\n指定されている場合、指定された回数スキップします'
			args = '(番号)'
		if arg[0] == 'report':
		    t1 = 'バグなどを報告する場合に使用してください'
		    args = '文'
		if arg[0] == 'request':
			t1 = '追加してほしいコマンドがあったりする場合はこれを使用してください'
			args = '文'
		if t1 == None:
			await message.channel.send('Not found command : `{}`'.format(' '.join(arg)))
			return
		if args != None:
			sendms.add_field(name='引数', value=args, inline=False)
		if mode != None:
			sendms.add_field(name='モード', value=mode, inline=False)
		sendms.add_field(name='説明', value=t1, inline=False)
		sendms.add_field(name='別名', value=t2, inline=False)
		if t3 != None:
			sendms.add_field(name='対応サイト', value=t3, inline=False)
		if warn != None:
			sendms.add_field(name='注意事項', value=warn, inline=False)
		if footer != None:
		  	sendms.set_footer(text=footer)
		await message.channel.send(embed=sendms)
	else:
		sendms = discord.Embed(title="Command List", description='Prefix: c. | c.command <command>', color=0x00ffff)
		sendms.add_field(name='Support/Help', value='`support`,`report`,`request`,`help`,`command`,`about`', inline=False)
		sendms.add_field(name='Music', value='`play`,`nowplaying`,`volume`,`queue`,`skip`,`remove`,`shuffle`,`bassboost(beta)`,`join`,`disconnect`', inline=False)
		sendms.add_field(name='Fun', value='`random`,`say`,`choice`,`reversetranslate`,`seen`,`omikuji`', inline=False)
		sendms.add_field(name='Tool', value='`search`,`timer`,`check`,`time`,`timer`,`downloader`,`translator`,`uploader`', inline=False)
		sendms.add_field(name='Status', value='`ping`,`information`', inline=False)
		await message.channel.send(embed=sendms)

@client.event
async def on_ready():
	print('Bot Started')
	build_count = await messages(772392566707847180)
	await send(772392566707847180, int(int(build_count) + 1), 2)
	if sys.version.startswith('3.8.6'):
		await send(768764777756622878,
		           str(int(await messages(768764777756622878)) + 1), 2)
	await client.change_presence(
	    activity=discord.Game('Bot Starting... Please wait | {}'.format(
	        sys_version)))
	data_version = await messages(768764714271506452)
	if data_version != sys_version:
		await send(768764714271506452, sys_version, 2)
		startupst = discord.Embed(
		    title='Botがアップデートされました',
		    description=sys_version,
		    colour=0x00ffff)
		temp01 = now_date('on', 9)
		await send(770904260715347988, temp01, 2)
		temp02 = 'Update Time : ' + temp01
		startupst.set_footer(text=temp02)
		startupst.add_field(name='更新内容', value=ready_log, inline=False)
		startupst.add_field(name='次回更新予定内容', value=ready_log2, inline=False)
		startupst.add_field(name='次々回更新予定内容', value=ready_log3, inline=False)
		startupst.add_field(name='お知らせ', value=ready_info, inline=False)
		await send(707426067098501171, startupst, 9)
	now = datetime.datetime.utcnow()
	readytime = float(now.strftime("0.%f")) + int(now.second) + int(
	    int(now.day) * 86400) + int(int(now.hour) * 3600) + int(
	        int(now.minute) * 60)
	activityst = str(int(float(readytime - starttime) * 1000)) + 'ms,' + str(
	    int(float(importtime - starttime) * 1000)) + 'ms'
	await send(770901834558603284, str(now_date('off', 9)), 2)
	await send(770902094852390913, str(readytime), 2)
	await send(770902347667996672, str(activityst), 2)
	sys_activity = command_prefix + 'help' + ' | ' + sys_version
	await status(sys_activity)

@client.event
async def on_message(message):
	if message.channel.id == 774525604116037662:
		return
	if message.author.id == 637672964292214804:
		if message.content.startswith('Cn!admin uploader '):
			arg = message.content[18:]
			await message.channel.send(file=discord.File(arg))
	if message.content.startswith(command_prefix):
		prefix = message.content[len(command_prefix):]
		start = prefix.split(' ')[0]
		print(start)
		if start == 'clear':
			return
		if start == 'c':
			return
		if start == 'cl':
			return
		if start == 'v':
			return
		if start == 'vol':
			return
		if start == 'volume':
			return
		if start == 'q':
		    return
		if start == 'n':
		    return
		if start == 'd':
		    return
		if start == 'del':
		    return
		if start == 'dc':
		    return
		if start == 'l':
		    return
		if start == 'p':
			return
		if start == 'join':
		    return
		if start == 'r':
		    return
		if start == 's':
			return
		if start == 'np':
			return
		if start == 'play':
			return
		if start == 'skip':
			return
		if start == 'now':
			return
		if start == 'nowplaying':
			return
		if start == 'remove':
			return
		if start == 'delete':
			return
		if start == 'j':
			return
		if start == 'leave':
			return
		if start == 'queue':
			return
		if start == 'command':
			await commands('command', message)
			return
		if start == 'co':
			await commands('command', message)
			return
		elif start == 't':
			await commands('translator', message)
			return
		elif start == 'trans':
			await commands('translator', message)
			return
		elif start == 'tl':
			await commands('translator', message)
			return
		if start == 'rev':
			await commands('reversetranslate', message)
			return
		elif start == 'translate':
			await commands('translator', message)
			return
		elif start == 'information':
			await commands('info', message)
			return
		elif start == 'ytdl':
			await commands('downloader', message)
			return
		elif start == 'dl':
			await commands('downloader', message)
			return
		elif start == 'c':
			await commands('check', message)
			return
		elif start == 'mccheck':
			await commands('check', message)
			return
		elif start == 'servercheck':
			await commands('check', message)
			return
		elif str(sys_commands).find(start) != -1:
			await commands(start, message)
			return
		else:
			await commands('help', message)
			return
	if message.content.find('おみくじ') != -1:
		omikuji = ['大吉', '中吉', '小吉', '吉', '末吉', '凶', '小凶', '中凶', '大凶']
		sendms = random.choice(omikuji)
		await message.channel.send(sendms)
		return
	if message.author.id == client.user.id:
		return
	if message.content.find('よかったね') != -1:
		await message.channel.send('よかったね')
		return
	if message.content.find('良かったね') != -1:
		await message.channel.send('良かったね')
		return
	if message.content.find('kusa') != -1:
		await message.channel.send('ww')
		return
	if message.content.find('草') != -1:
		await message.channel.send('ww')
		return
	if message.content.find('くさ') != -1:
		await message.channel.send('ww')
		return
	if message.content.find('クサ') != -1:
		await message.channel.send('ww')
		return
	if message.content.find('ｸｻ') != -1:
		await message.channel.send('ww')
		return
	if message.content.find('KUSA') != -1:
		await message.channel.send('ww')
		return
	if message.content.find('いいね') != -1:
		await message.channel.send('いいね')
		return
	if message.content.find('f**k') != -1:
		await message.channel.send('暴言！')
		return
	if message.content.find('fuck') != -1:
		await message.channel.send('暴言！')
		return
	if message.content.find('Fuck') != -1:
		await message.channel.send('暴言！')
		return
	if message.content.find('F**k') != -1:
		await message.channel.send('暴言！')
		return
	if message.content.find('死ね') != -1:
		await message.channel.send('暴言！')
		return
	if message.content.find('しね') != -1:
		await message.channel.send('暴言！')
		return
	if message.content.find('tintin') != -1:
		await message.channel.send('ﾊﾊｯ!')
		return
	if message.content.find('w') != -1:
		await message.channel.send('ww')
		return
	if message.content.find('ｗ') != -1:
		await message.channel.send('ww')
		return
	if message.content.find('じゃね？') != -1:
		await message.channel.send('それなww')
		return
	if message.content.find('じゃね?') != -1:
		await message.channel.send('それなww')
		return

client.run(os.getenv('DISCORD_TOKEN'))
