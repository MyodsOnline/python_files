import os
import shutil
import py7zr

base_dir = os.path.join(os.path.dirname(__file__), 'Good')
path_to_file = os.path.join(base_dir, '2024_06_23')
file_name = str('00_01_24.7z')
file = os.path.join(path_to_file, file_name)
extract_path = os.path.join(base_dir, 'files')


def create_directory(path: str) -> None:
    """
    Функция создает директорию, в которую будет извлекатося архив.
    :param path: путь к директории
    :return: None
    """
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Directory '{path}' created.")
    else:
        print(f"Directory '{path}' already exists.")


def clear_directory(extract_path: str) -> None:
    """
    Функция производит удаление всех дирекорий и файлов по заданному пути.
    :param extract_path: путь к директории
    :return: None
    """
    for filename in os.listdir(extract_path):
        file_path = os.path.join(extract_path, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')
    print(f"Directory '{extract_path}' cleared.")


def extract(file: str, extract_path: str) -> None:
    """
    Функция извлекает архив в заданную директорию.
    :param file: путь к 7z архиву
    :param extract_path: путь к директории, куда будет извлечен архив
    :return: None
    """
    create_directory(extract_path)
    clear_directory(extract_path)
    with py7zr.SevenZipFile(file, 'r') as archive:
        archive.extractall(path=extract_path)


if __name__ == '__main__':
    # extract(file, extract_path)
    clear_directory(extract_path)
