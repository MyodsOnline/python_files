from urllib import request
from io import TextIOWrapper
import re

from settings import settings

x = request.urlopen(settings.URL_PATH)
lines = TextIOWrapper(x, encoding='utf-8')
for line in lines:
    if 'class="link right"' in line:
        match = re.search('>(.+?)<', line)
        print(line, match.group(1))
