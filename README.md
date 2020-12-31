# Python Bot
このBotはPythonで作られたいろんな機能があるbotです。

## 使用方法
#### Python 3.8.6以上を[ダウンロード](https://www.python.org/downloads/)
#### FFmpegを[ダウンロード](https://ffmpeg.org/download.html)
#### このレポジトリを[ダウンロード](https://github.com/xCorePython/python-bot.git)
#### 環境変数を追加 (一応コードを書き換えることで代用可)
#####  DISCORD_TOKEN : DiscordのBotToken ([ここから作成](https://discord.com/developers))
#####  VCID : 音楽を流すボイスチャンネルのID
#####  QUEUEID : 音楽のキューを保存するためのチャンネルのID
#####  BOT_PREFIX : BotのPrefix(コマンドの先頭文字)
#### パッケージをインストール (レポジトリ内のinstall.batを実行するだけでok)
#### 実行 (MusicBotとBotだけにわかれています。)

## Herokuでの使用方法
#### このレポジトリを自分のレポジトリを作りインポートする。
#### 設定から以下のBuildpackを入れる。
#####  https://github.com/Crazycatz00/heroku-buildpack-libopus.git
#####  https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git
#### 設定から環境変数を追加(Reveal Config Vars)する (一応コードを書き換えることで代用可)
#####  DISCORD_TOKEN : DiscordのBotToken ([ここから作成](https://discord.com/developers))
#####  VCID : 音楽を流すボイスチャンネルのID
#####  QUEUEID : 音楽のキューを保存するためのチャンネルのID
##### BOT_PREFIX : BotのPrefix(コマンドの先頭文字)
#### 自分のレポジトリをHerokuに繋ぐ。
#### デプロイ(Deploy Branch)する。
#### 実行 (Procfileは自分もHerokuで使っているため既に入っています。)
