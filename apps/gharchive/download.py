import requests


def download_file(file):
    res = requests.get(f'https://data.gharchive.org/{file}')
    return res
