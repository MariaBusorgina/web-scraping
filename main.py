import bs4
import requests
from fake_headers import Headers

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

URL = 'https://habr.com/ru/all/'

def parser(list_words, url):
    header = Headers().generate()
    response = requests.get(url, headers=header)
    text = response.text
    soup = bs4.BeautifulSoup(text, features="html.parser")
    article = soup.find_all('article')

    for item in article:
        item_text = item.text.lower()

        for word in list_words:
            if word in item_text:
                data = item.find("time")["title"].split(",")[0]
                title = item.find("h2").text
                href = item.find(class_="tm-article-snippet__title-link").attrs["href"]
                print(f"{data} - {title} - https://habr.com{href}")
                print(" ")

if __name__ == '__main__':
    parser(KEYWORDS, URL)