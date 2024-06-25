import os

base_path = f'/Users/diver.vlz/Documents/working_directory/python_files/'
# PATH = r"\\srv-smzu2-sz\CFRAS\FilesRegim\Good"


def scan_basedir(path: str) -> list:
    try:
        first_level_dirs = []
        with os.scandir(path) as base_dir:
            for sub_directory in base_dir:
                if sub_directory.is_dir():
                    first_level_dirs.append(sub_directory.name)
        return first_level_dirs
    except FileNotFoundError:
        print(f'Directory "{path}" does not exist.')
        return []
    except PermissionError:
        print(f'Permission denied to access {path}')
        return []


def scan_subdirectories(path, directory_name):
    subdir_path = os.path.join(path, directory_name)
    if os.path.isdir(subdir_path):
        try:
            with os.scandir(subdir_path) as directory:
                for entry in directory:
                    if entry.is_dir():
                        print(entry.name)
                    else:
                        print(f'\tOther files: {entry.name}')
        except FileNotFoundError:
            print(f'Directory "{subdir_path}" does not exist.')
    else:
        print(f'Directory {directory_name} does not exist in {path}')


def print_directories():
    first_level_dir = scan_basedir(base_path)
    if first_level_dir:
        for dir_name in first_level_dir:
            print(dir_name)
        user_input = input('Enter data: ')
        if user_input in first_level_dir:
            print(f'Subdirectories of {user_input}:')
            scan_subdirectories(base_path, user_input)
        else:
            print(f'Directory {user_input} not found')
    else:
        print(f'No first level directories found')


if __name__ == '__main__':
    print_directories()