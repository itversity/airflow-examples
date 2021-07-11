from datetime import datetime as dt
from datetime import timedelta as td
import yaml
import os


def get_conf(conf_file, env):
    conf = yaml.load(open(conf_file), Loader=yaml.FullLoader)
    return conf[env]


def get_prev_file_name(bookmark_dir, bookmark_file, baseline_file):
    if os.path.exists(f'{bookmark_dir}/{bookmark_file}'):
        prev_file = open(f'{bookmark_dir}/{bookmark_file}').read()
    else:
        prev_file = baseline_file
    return prev_file


def update_bookmark(bookmark_dir, bookmark_file, bookmark_contents):
    bookmark_file = open(f'{bookmark_dir}/{bookmark_file}', 'w')
    bookmark_file.write(bookmark_contents)
    bookmark_file.close()


def get_next_file_name(prev_file):
    dt_part = prev_file.split('.')[0]
    next_file = f"{dt.strftime(dt.strptime(dt_part, '%Y-%M-%d-%H') + td(hours=1), '%Y-%M-%d-%-H')}.json.gz"
    return next_file
