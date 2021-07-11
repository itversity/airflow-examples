def upload_file(body, target_dir, file):
    file_to_write = open(f'{target_dir}/{file}', 'wb')
    res = file_to_write.write(body)
    file_to_write.close()
    return res
