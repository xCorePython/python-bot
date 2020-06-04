import discord

client = discord.Client()
token = 'NjgwNzAwMzc4OTI4NjQ0MTE3.XlGwuA.gsmJ-n7-TItMUUuNZM8OAANGlZw'

def _setup_logging():
        shandler = logging.StreamHandler(stream=sys.stdout)
        shandler.setFormatter(colorlog.LevelFormatter(
            fmt = {
                'DEBUG': '{log_color}[{levelname}:{module}] {message}',
                'INFO': '{log_color}{message}',
                'WARNING': '{log_color}{levelname}: {message}',
                'ERROR': '{log_color}[{levelname}:{module}] {message}',
                'CRITICAL': '{log_color}[{levelname}:{module}] {message}',

                'EVERYTHING': '{log_color}[{levelname}:{module}] {message}',
                'NOISY': '{log_color}[{levelname}:{module}] {message}',
                'VOICEDEBUG': '{log_color}[{levelname}:{module}][{relativeCreated:.9f}] {message}',
                'FFMPEG': '{log_color}[{levelname}:{module}][{relativeCreated:.9f}] {message}'
            },
            log_colors = {
                'DEBUG':    'cyan',
                'INFO':     'white',
                'WARNING':  'yellow',
                'ERROR':    'red',
                'CRITICAL': 'bold_red',

                'EVERYTHING': 'white',
                'NOISY':      'white',
                'FFMPEG':     'bold_purple',
                'VOICEDEBUG': 'purple',
        },
            style = '{',
            datefmt = ''
        ))
        logging.getLogger(__package__).addHandler(shandler)

        log.debug("Set logging level to {}")

        dlogger = logging.getLogger('discord')
        dlogger.setLevel(logging.DEBUG)
        dhandler = logging.FileHandler(filename='logs/discord.log', encoding='utf-8', mode='w')
        dhandler.setFormatter(logging.Formatter('{asctime}:{levelname}:{name}: {message}', style='{'))
        dlogger.addHandler(dhandler)

@client.event
async def on_ready():
    _setup_logging()

client.run(token)
