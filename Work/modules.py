import os
import shutil
from tabulate import tabulate as tb

from env import BASE

print(os.name, os.environ['LOGNAME'])
print(os.getcwd())

CUR_LOC = os.path.basename(os.path.join(BASE, 'working_directory/python_files/Work'))
CUR_LOC_DIR = os.path.dirname(os.path.join(BASE, 'working_directory/python_files/Work/modules.py'))
print(CUR_LOC, CUR_LOC_DIR)
# isfile,isdir
print(os.path.isfile(CUR_LOC), os.path.isdir(CUR_LOC))
print(os.path.isfile(CUR_LOC_DIR), os.path.isdir(CUR_LOC_DIR))
# exists
print(os.path.exists(os.path.join(CUR_LOC, 'modules.py')))
# split
print(os.path.split(os.path.join(BASE, 'working_directory/python_files/Work/modules.py')))
# listdir
print(os.listdir(os.path.join(BASE, 'working_directory/python_files')))

#### tabulate
FILE = '../JimShapedCoding/items.csv'
lines_list = []
with open(FILE, 'r', encoding='utf-8') as file:
    parsed_file = file.readlines()
    for line in parsed_file:
        lines_list.append(tuple((line.strip().split(sep=','))))

print(tb(lines_list, headers='firstrow', tablefmt='pipe'))
