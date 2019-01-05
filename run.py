import fire
from tqdm import tqdm
from downloader import download_youtube


class Downloader:

    @staticmethod
    def from_file(text_file_path):
        with open(text_file_path, 'r') as r:
            for line in tqdm(r.readlines()):
                url, file_name = line.strip().split()
                # call download funciton
                download_youtube(url=url, file_name=file_name)


if __name__ == '__main__':
    fire.Fire(Downloader)
