import os
import logging


PATH = os.getcwd()
PATH = os.path.join(PATH, 'client.log')


log = logging.getLogger('app.schedule')

_formatter_file = logging.Formatter("%(asctime)s  %(levelname)-8s  %(module)-10s  %(message)s")

file_handler = logging.FileHandler(PATH, encoding='utf-8')
file_handler.setFormatter(_formatter_file)

log.addHandler(file_handler)
log.setLevel(logging.INFO)

if __name__ == '__main__':
    log.critical('Критическая ошибка')
    log.error('Ошибка')
    log.debug('Отладочное сообщение')
    log.info('Информационное сообщение')