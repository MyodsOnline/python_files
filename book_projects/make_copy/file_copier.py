import os
import time
import shutil

PATH = os.getcwd()

FROM_PATH = os.path.join(PATH, 'files_to_copy')
TO_PATH = os.path.join(PATH, 'copyed_files')

FILE_PATH = os.path.join(FROM_PATH, 'test.txt')
with open(FILE_PATH, 'a') as f:
    log_date = time.strftime('%Y.%m.%d_%H:%M')
    f.write(f'\n{log_date}___another test string')

FILE_NAME = TO_PATH + os.sep + 'file_' + time.strftime('%Y%m%d_%H%M') + '.txt'
shutil.copy(FILE_PATH, FILE_NAME)
