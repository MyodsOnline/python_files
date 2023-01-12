import logging
import os
import time, datetime

import logger.logger

FILE_PATH = 'C:\\Users\\PoorBrain\\Desktop'
FILE_NAME = os.path.join(FILE_PATH, 'save.txt')

LOG = logging.getLogger('app.schedule')


def user_system_time():
    with open(FILE_NAME, 'a') as file:
        log_date = time.strftime('%Y.%m.%d_%H:%M')
        try:
            file.write(f'\n{log_date}___ok')
            LOG.info(f'File {FILE_NAME} updated at {datetime.datetime.now()}')
        except PermissionError:
            LOG.error(f'Permission to {FILE_NAME} denied')
            raise PermissionError


if __name__ == '__main__':
    user_system_time()
