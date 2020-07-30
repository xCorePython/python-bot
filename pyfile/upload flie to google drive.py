from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from time import sleep
import datetime

#Googleの認証を行う
gauth = GoogleAuth()
gauth.LocalWebserverAuth()

#Google Driveのオブジェクトを取得
drive = GoogleDrive(gauth)

f = drive.CreateFile({
	'title':'decode.jpg',
	'mimeType':'image/jpeg'
})
f.SetContentFile('decode.jpg')

print("Uploading...")
f.Upload()
print("Uploaded!")

#現在時刻を取得して表示
now = datetime.datetime.now()
print("now:" + str(now))

#ファイルIDを取得して表示
file_id = f['id']
print('id:' + file_id)

try:
	while True:
		sleep(3600)
		report = drive.CreateFile({
			'id':file_id
			})
		report.SetContentFile('/home/admarimoin/ドキュメント/report/毎日徹夜.odt')
		print("Uploading...")
		report.Upload()
		print("Uploaded!")
		now = datetime.datetime.now()
		print("now:" + str(now))
except KeyboardInterrupt: 
	print("\ncancel.")
