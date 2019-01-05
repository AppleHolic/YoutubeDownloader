import unittest
import os
from .downloader import download_youtube


class YoutubeDownloadTest(unittest.TestCase):

    def test_download(self):
        if os.path.exists('./download/test.mp3'):
            os.remove('./download/test.mp3')
        link = 'https://www.youtube.com/watch?v=HI_afSFJXAs'
        check_file = download_youtube(link, 'test')
        self.assertTrue(check_file)


if __name__ == '__main__':
    unittest.main()
