import os
import shutil
import tarfile as tar
from datetime import datetime

# FUNCTION TO CREATE ARCHIVE
def tar_dir(src, name):
    with tar.open(name, 'w:gz') as tar_handle:
        for root, dirs, files in os.walk(src):
            for file in files:
                tar_handle.add(os.path.join(root, file))


now = datetime.now()    # GET CURRENT TIME
date_time = now.strftime("%m-%d-%Y_%H_%M_%S")   # FORMAT TIMESTAMP FROM CURRENT DATE AND TIME
tar_name = date_time + ".tar.gz"    # CREATE OUTPUT TAR FILENAME
temp_dir = '/home/pi/temp/'     # TEMP DIR

try:
    tar_dir('/home/pi/backup/', tar_name)  # CREATE SPECIFIED DIR TO CREATE BACKUP
except IOError:
    print('Error while creating backup!')
finally:
    print('Backup created successful!')
    if os.path.isfile(tar_name):
        shutil.move(tar_name, temp_dir)
        print('File moved to temp directory!')


