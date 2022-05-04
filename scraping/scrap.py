import json
import requests
from bs4 import BeautifulSoup

"""
task: parse the web page
"""

url_exmo = requests.get('https://eksmo.ru/sales/stock/')
print(f'status code - {url_exmo.status_code}')

code_exmo = BeautifulSoup(url_exmo.content, 'html.parser')
stock_books = code_exmo.find_all(class_ = 'book__link')

book_names = []
book_dict_loop = {}

for book in stock_books:
    book_name = book.find(class_ = 'book__name')
    book_author = book.find(class_ = 'book__author')
    book_link = book.get('href')
    book_names.append([book_name.string.strip() if book_name else None,
                       book_author.string.strip() if book_author else None,
                       book_link if book_link else None])

# print(book_names)

books_dict = []
for el in range(0, len(book_names)):
    books_dict.append({'id': el + 1,
                       'name': book_names[el][0],
                       'author': book_names[el][1],
                       'href': book_names[el][2]})

# print(books_dict)

with open('books.json', 'w', encoding='utf-8') as f:
    json.dump(books_dict, f, ensure_ascii=False, indent=2)
