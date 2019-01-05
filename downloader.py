from __future__ import unicode_literals
from configs import YDL_OPTS, YDL_MASTER_PATH
import youtube_dl
import os
import glob


def download_youtube(url, file_name):
    opts = {k: v for k, v in YDL_OPTS['default'].items()}
    outtmpl = os.path.join(YDL_MASTER_PATH, file_name)+'.%(ext)s'
    opts['outtmpl'] = outtmpl

    with youtube_dl.YoutubeDL(opts) as ydl:
        ydl.download([url])

    exists_file = len(glob.glob(outtmpl.split('.')[0]+'.*')) > 0

    return exists_file