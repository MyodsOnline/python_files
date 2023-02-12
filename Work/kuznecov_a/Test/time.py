import datetime
import json

from Top_secret.gen_list import *
from First import csv_parse, all_status_apps
from Zero import current_smena


with open('all_apps.json', encoding='utf-8') as all_apps:
    APP = json.loads(all_apps.read())
    print(type(APP), APP)
