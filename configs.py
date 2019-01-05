# youtube downloader configs
YDL_MASTER_PATH = './download/'
YDL_OPTS = {
    'default': {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '0',
        }],
    }
}