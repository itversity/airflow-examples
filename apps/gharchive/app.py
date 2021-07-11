import os
from download import download_file
from util import get_prev_file_name, \
    get_next_file_name, update_bookmark, \
    get_conf
from upload import upload_file


def main():
    conf_file_name = os.environ.get('CONF_FILE_NAME')
    environ = os.environ.get('ENVIRON')
    conf = get_conf(conf_file_name, environ)
    if environ == 'DEV':
        print(f'Running in {environ} environment')
    target_dir = conf.get('TARGET_DIR')
    bookmark_file = conf.get('BOOKMARK_FILE')
    bookmark_dir = conf.get('BOOKMARK_DIR')
    baseline_file = conf.get('BASELINE_FILE')
    prev_file_name = get_prev_file_name(bookmark_dir, bookmark_file, baseline_file)
    file_name = get_next_file_name(prev_file_name)
    download_res = download_file(file_name)
    if download_res.status_code == 404:
        print(f'Invalid file name or downloads caught up till {prev_file_name}')
    print(f'File {file_name} successfully processed')
    upload_file(download_res.content, target_dir, file_name)
    update_bookmark(bookmark_dir, bookmark_file, file_name)
    return


if __name__ == '__main__':
    main()
